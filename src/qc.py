"""Automatic per-video quality checks. Logs pass/fail + issues to shorts/day_XX/qc.json and tracker.csv.

Checks: format (1080x1920, 30 fps, h264/aac), duration 45-52 s, caption sync vs. actual audio energy,
caption + on-screen-text safe zones (measured from rendered pixels), audio peak < -1 dB,
voice at least N dB louder than music.
"""
import json
import re
import subprocess
import sys
import wave

import numpy as np

from common import *


def probe(path):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=width,height,r_frame_rate,codec_name", "-of", "json", str(path)])
    return json.loads(r.stdout)["streams"][0]


def volumedetect(path):
    r = subprocess.run(["ffmpeg", "-i", str(path), "-vn", "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    mean = float(re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr).group(1))
    peak = float(re.search(r"max_volume: (-?[\d.]+) dB", r.stderr).group(1))
    return mean, peak


def read_mono(path):
    with wave.open(str(path)) as w:
        ch, sr = w.getnchannels(), w.getframerate()
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    return (a.reshape(-1, ch).mean(axis=1) if ch > 1 else a), sr


def caption_extents(day, dur, cfg):
    """Render the .ass on black (3 fps) and return the union bbox of caption pixels."""
    v = cfg["video"]
    d = day_dir(day)
    cmd = ["ffmpeg", "-v", "error", "-f", "lavfi", "-i", f"color=c=black:s={v['width']}x{v['height']}:r=3:d={dur:.2f}",
           "-vf", f"subtitles={d / 'captions.ass'}:fontsdir={ROOT / cfg['captions']['font_file_dir']},format=gray",
           "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    size = v["width"] * v["height"]
    x0, y0, x1, y1 = v["width"], v["height"], 0, 0
    while True:
        buf = p.stdout.read(size)
        if len(buf) < size:
            break
        m = np.frombuffer(buf, dtype=np.uint8).reshape(v["height"], v["width"]) > 60
        ys, xs = np.where(m.any(axis=1))[0], np.where(m.any(axis=0))[0]
        if len(ys):
            x0, y0, x1, y1 = min(x0, xs[0]), min(y0, ys[0]), max(x1, xs[-1]), max(y1, ys[-1])
    p.wait()
    return (int(x0), int(y0), int(x1), int(y1)) if x1 else None


def run_qc(day):
    cfg = config()
    v, sz, au = cfg["video"], cfg["safe_zone"], cfg["audio"]
    d = day_dir(day)
    mp4 = OUTPUT / f"day_{day:02d}.mp4"
    issues, m = [], {}

    # 1. format + duration
    st = probe(mp4)
    dur = ffprobe_duration(mp4)
    m.update(duration=round(dur, 2), resolution=f"{st['width']}x{st['height']}", fps=st["r_frame_rate"], codec=st["codec_name"])
    if (st["width"], st["height"]) != (v["width"], v["height"]):
        issues.append(f"resolution {st['width']}x{st['height']}")
    if eval(st["r_frame_rate"]) != v["fps"]:
        issues.append(f"fps {st['r_frame_rate']}")
    if not v["min_seconds"] <= dur <= v["max_seconds"]:
        issues.append(f"duration {dur:.1f}s outside {v['min_seconds']}-{v['max_seconds']}s")

    # 2. caption sync against actual audio energy
    voice, sr = read_mono(d / "voice_mix.wav")
    hop = int(0.05 * sr)
    n = len(voice) // hop
    rms = np.sqrt((voice[:n * hop].reshape(n, hop) ** 2).mean(axis=1))
    active = rms > 0.012
    caps = json.loads((d / "captions.json").read_text())
    act_idx = np.where(active)[0]
    if len(act_idx):
        speech_start, speech_end = act_idx[0] * 0.05, (act_idx[-1] + 1) * 0.05
        m["speech_start"], m["speech_end"] = round(speech_start, 2), round(speech_end, 2)
        if abs(caps[0]["start"] - speech_start) > 0.35:
            issues.append(f"first caption {caps[0]['start']:.2f}s vs speech start {speech_start:.2f}s")
        if abs(caps[-1]["end"] - speech_end) > 0.5:
            issues.append(f"last caption {caps[-1]['end']:.2f}s vs speech end {speech_end:.2f}s")
    silent = []
    for c in caps:
        a, b = int(c["start"] / 0.05), max(int(c["start"] / 0.05) + 1, int(c["end"] / 0.05))
        if active[a:b].mean() < 0.5:
            silent.append(c["text"])
    if silent:
        issues.append(f"{len(silent)} caption chunks over silence, e.g. {silent[0]!r}")
    if any(b["start"] < a["start"] for a, b in zip(caps, caps[1:])):
        issues.append("captions out of order")
    if caps[-1]["end"] > dur + 0.05:
        issues.append("captions run past end of video")

    # 3. safe zones (from rendered pixels)
    limit_y = v["height"] * (1 - sz["bottom_pct"] / 100)
    limit_x = v["width"] - sz["right_px"]
    ext = caption_extents(day, dur, cfg)
    m["caption_bbox"] = ext
    if ext is None:
        issues.append("no caption pixels rendered")
    else:
        if ext[3] > limit_y: issues.append(f"captions reach y={ext[3]} (> {limit_y:.0f})")
        if ext[2] > limit_x: issues.append(f"captions reach x={ext[2]} (> {limit_x})")
        if ext[0] < sz["left_px"]: issues.append(f"captions reach x={ext[0]} (< {sz['left_px']})")
    scenes = json.loads((d / "scenes.json").read_text())
    for s in scenes:
        bb = s["text_bbox"]
        if bb and (bb[3] > limit_y or bb[2] > limit_x or bb[0] < sz["left_px"] or bb[1] < sz["top_px"]):
            issues.append(f"on-screen text of scene {s['scene']} outside safe zone {[round(x) for x in bb]}")

    # 4. audio
    mean_all, peak = volumedetect(mp4)
    vm, _ = volumedetect(d / "voice_mix.wav")
    mm, _ = volumedetect(d / "music_mix.wav")
    m.update(peak_db=peak, voice_mean_db=vm, music_mean_db=mm, voice_over_music_db=round(vm - mm, 1))
    if peak > -1.0:
        issues.append(f"audio peak {peak} dB (> -1 dB)")
    if vm - mm < au["min_voice_over_music_db"]:
        issues.append(f"voice only {vm - mm:.1f} dB over music (< {au['min_voice_over_music_db']})")

    res = {"day": day, "passed": not issues, "issues": issues, "metrics": m}
    (d / "qc.json").write_text(json.dumps(res, indent=1))
    tracker_update(day, video_done="TRUE", qc_passed="TRUE" if not issues else "FALSE",
                   notes="; ".join(issues) if issues else "QC ok")
    print(f"day {day:02d} QC {'PASS' if not issues else 'FAIL'}: {m}")
    for i in issues:
        print("   -", i)
    return res


if __name__ == "__main__":
    run_qc(int(sys.argv[1]))
