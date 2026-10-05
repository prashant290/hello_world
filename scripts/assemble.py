"""Combine scene clips + voiceover + captions + low-volume music into output/day_XX.mp4 (ffmpeg)."""
import sys

from common import *


def build(day):
    cfg = config()
    a = cfg["audio"]
    d = day_dir(day)
    timing = load_timing(day)
    dur = timing["duration"]
    nscenes = len(timing["scenes"])
    # concat list
    (d / "scenes.txt").write_text("".join(f"file 'scenes/scene_{i:02d}.mp4'\n" for i in range(nscenes)))
    # audio stems (kept on disk so QC can measure voice vs music)
    run(["ffmpeg", "-y", "-v", "error", "-i", str(d / "voice.wav"), "-af",
         f"loudnorm=I={a['target_lufs']}:TP=-2.5:LRA=7,apad", "-ar", "44100", "-ac", "1", "-t", f"{dur:.3f}", str(d / "voice_mix.wav")])
    music = ASSETS / "music" / f"ambient_{day % 3 + 1}.wav"
    run(["ffmpeg", "-y", "-v", "error", "-stream_loop", "-1", "-i", str(music), "-t", f"{dur:.3f}", "-af",
         f"loudnorm=I={a['target_lufs']}:TP=-2.5,volume={a['music_gain_db']}dB,afade=t=in:d=1.2,afade=t=out:st={dur - 2:.2f}:d=2",
         "-ar", "44100", "-ac", "2", str(d / "music_mix.wav")])
    out = OUTPUT / f"day_{day:02d}.mp4"
    OUTPUT.mkdir(exist_ok=True)
    ceiling = 10 ** (a["peak_ceiling_db"] / 20)
    fonts = cfg["captions"]["font_file_dir"]
    run(["ffmpeg", "-y", "-v", "error",
         "-f", "concat", "-safe", "0", "-i", str(d / "scenes.txt"),
         "-i", str(d / "voice_mix.wav"), "-i", str(d / "music_mix.wav"),
         "-filter_complex",
         f"[0:v]fps={cfg['video']['fps']},subtitles={d / 'captions.ass'}:fontsdir={fonts},format=yuv420p[v];"
         f"[1:a][2:a]amix=inputs=2:normalize=0:duration=first,alimiter=limit={ceiling:.4f}:level=disabled[a]",
         "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", str(cfg["video"]["fps"]),
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)])
    print(f"day {day:02d} assembled -> {out.relative_to(ROOT)} ({ffprobe_duration(out):.2f}s)")
    return out


if __name__ == "__main__":
    build(int(sys.argv[1]))
