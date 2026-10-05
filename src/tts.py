"""Generate voiceover audio + word timings from script.json.

Writes shorts/day_XX/voice.wav and shorts/day_XX/timing.json.
Engines (config.json -> tts.engine):
  espeak  offline/free, robotic (used in the build sandbox)
  edge    free Microsoft neural voices via `pip install edge-tts` (no API key, needs internet)
  piper   free offline neural voice (needs a downloaded .onnx model)
Each narration line is synthesized separately so scenes line up exactly with speech.
"""
import asyncio
import json
import re
import sys
import wave

import numpy as np

from common import *


def read_wav(path):
    with wave.open(str(path)) as w:
        assert w.getsampwidth() == 2
        sr, ch = w.getframerate(), w.getnchannels()
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    return (a.reshape(-1, ch).mean(axis=1) if ch > 1 else a), sr


def write_wav(path, a, sr):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())


def to_wav(src, dst, sr=44100):
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-ac", "1", "-ar", str(sr), "-sample_fmt", "s16", str(dst)])


def trim(a, sr, thresh=0.008, pad=0.03):
    idx = np.where(np.abs(a) > thresh)[0]
    if len(idx) == 0:
        return a, 0.0
    s, e = max(0, idx[0] - int(pad * sr)), min(len(a), idx[-1] + int(pad * sr))
    return a[s:e], s / sr


# ------------------------------------------------------------------ engines
def synth_espeak(text, out, cfg):
    c = cfg["espeak"]
    run(["espeak-ng", "-v", c["voice"], "-s", str(c["speed_wpm"]), "-p", str(c["pitch"]), "-w", str(out), text])
    return None


def synth_edge(text, out, cfg):
    import edge_tts
    words = []

    async def go():
        com = edge_tts.Communicate(text, cfg["edge"]["voice"], rate=cfg["edge"]["rate"], boundary="WordBoundary")
        with open(str(out) + ".mp3", "wb") as f:
            async for ch in com.stream():
                if ch["type"] == "audio":
                    f.write(ch["data"])
                elif ch["type"] == "WordBoundary":
                    words.append((ch["text"], ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7))
    asyncio.run(go())
    to_wav(str(out) + ".mp3", out)
    return words


def synth_piper(text, out, cfg):
    run(["piper", "-m", str(ROOT / cfg["piper"]["model"]), "-f", str(out)], input=text)
    return None


_KOKORO = {}


def synth_kokoro(text, out, cfg):
    """Free offline neural voice (Kokoro-82M via kokoro-onnx). No API key; model files live in assets/voices."""
    import soundfile as sf
    from kokoro_onnx import Kokoro
    c = cfg["kokoro"]
    if "k" not in _KOKORO:
        _KOKORO["k"] = Kokoro(str(ROOT / c["model"]), str(ROOT / c["voices"]))
    a, sr = _KOKORO["k"].create(text, voice=c["voice"], speed=c["speed"], lang=c["lang"])
    sf.write(str(out), a, sr)
    return None


ENGINES = {"espeak": synth_espeak, "edge": synth_edge, "piper": synth_piper, "kokoro": synth_kokoro}


def find_gaps(a, sr, thresh=0.01, min_gap=0.09):
    """Internal silences (start, end) in seconds."""
    hop = int(0.01 * sr)
    n = len(a) // hop
    act = np.sqrt((a[:n * hop].reshape(n, hop) ** 2).mean(axis=1)) > thresh
    gaps, i = [], 0
    while i < n:
        if not act[i]:
            j = i
            while j < n and not act[j]:
                j += 1
            if j - i >= min_gap * 100 and i > 0 and j < n:
                gaps.append((i / 100, j / 100))
            i = j
        else:
            i += 1
    return gaps


def estimate_words(tokens, dur, audio=None, sr=44100):
    """Word timings from the audio itself (no ASR needed).
    1. Find where the voice is speaking (10 ms frames; micro-gaps < 60 ms count as speech).
    2. Match each punctuation break (, ; : . ? !) to the nearest real silence (>= 100 ms) around where it is
       expected, so a word can never straddle a pause.
    3. Inside each phrase, spread words by letter count over that phrase's speech-active frames only.
    Falls back to a global speech-active mapping, then to a plain proportional split."""
    weight = lambda t: (len(re.sub(r"[^A-Za-z]", "", t)) + 2 * len(re.sub(r"\D", "", t))
                        + (8 if "$" in t else 0) + (6 if "%" in t else 0) + 1.5)   # spoken length, not written length
    w = [weight(t) for t in tokens]
    tot = sum(w)
    cumw = np.concatenate([[0], np.cumsum(w)]) / tot
    if audio is None or len(audio) < sr * 0.2:
        return [(t, cumw[i] * dur, cumw[i + 1] * dur) for i, t in enumerate(tokens)]
    hop = int(0.01 * sr)
    n = len(audio) // hop
    act = np.sqrt((audio[:n * hop].reshape(n, hop) ** 2).mean(axis=1)) > 0.01
    i = 0
    while i < n:
        if not act[i]:
            j = i
            while j < n and not act[j]:
                j += 1
            if j - i < 6 and i > 0 and j < n:
                act[i:j] = True
            i = j
        else:
            i += 1
    cum = np.cumsum(act)
    first = int(np.argmax(act)); last = int(n - 1 - np.argmax(act[::-1]))
    gaps, i = [], first
    while i <= last:
        if not act[i]:
            j = i
            while j <= last and not act[j]:
                j += 1
            if j - i >= 10:
                gaps.append((i, j))
            i = j
        else:
            i += 1
    breaks = [k for k, t in enumerate(tokens[:-1]) if t[-1] in ",;:.?!"]
    total_act = cum[last] - (cum[first - 1] if first else 0)

    def to_time(p, side):                         # speech-active position -> frame
        return (np.searchsorted(cum, p, side=side)) / 100

    spans = None
    if breaks and gaps:
        chosen, used = [], set()
        for bk in breaks:
            exp_frame = np.searchsorted(cum, cumw[bk + 1] * total_act, side="left")
            cand = [(abs((g[0] + g[1]) / 2 - exp_frame), k) for k, g in enumerate(gaps) if k not in used]
            if not cand:
                chosen = None
                break
            d, k = min(cand)
            used.add(k); chosen.append(gaps[k])
        if chosen and all(chosen[x][0] < chosen[x + 1][0] for x in range(len(chosen) - 1)):
            cuts = [0] + [bk + 1 for bk in breaks] + [len(tokens)]
            edges = [first] + [e for g in chosen for e in g] + [last + 1]
            spans = [(edges[2 * x], edges[2 * x + 1], cuts[x], cuts[x + 1]) for x in range(len(cuts) - 1)]
            if any((e - s_) / 100 < 0.1 * (c1 - c0) for s_, e, c0, c1 in spans):
                spans = None
    out = []
    if spans:
        for s_, e, c0, c1 in spans:
            base = cum[s_ - 1] if s_ else 0
            pa = cum[e - 1] - base
            ph = tokens[c0:c1]
            pw = [weight(t) for t in ph]
            pc = np.concatenate([[0], np.cumsum(pw)]) / sum(pw)
            for k, t in enumerate(ph):
                st = np.searchsorted(cum, base + pc[k] * pa, side="right") / 100
                en = (np.searchsorted(cum, base + max(pc[k + 1] * pa, 1e-9), side="left") + 1) / 100
                out.append((t, min(max(st, s_ / 100), dur), min(max(en, st + 0.05), e / 100, dur)))
        return out
    for k, t in enumerate(tokens):                 # global mapping fallback
        p0, p1 = cumw[k] * total_act, cumw[k + 1] * total_act
        st = to_time(p0, "right"); en = to_time(max(p1, 1e-9), "left") + 0.01
        out.append((t, min(st, dur), min(max(en, st + 0.05), dur)))
    return out


SPOKEN = {"9/11": "nine eleven"}    # written form -> how it should be pronounced


def speak(text):
    for k, v in SPOKEN.items():
        text = text.replace(k, v)
    return text


def build(day, engine=None, speed_mult=1.0):
    cfg = config()["tts"]
    engine = engine or cfg["engine"]
    s = load_script(day)
    cfg = json.loads(json.dumps(cfg))              # local copy so retries can change the speed
    if engine == "kokoro":
        cfg["kokoro"]["speed"] *= speed_mult
    d = day_dir(day)
    tmp = d / "tts_tmp"
    tmp.mkdir(exist_ok=True)
    sr, gap, lead = 44100, cfg["line_gap_sec"], 0.12
    audio, lines, t = [np.zeros(int(lead * sr), dtype=np.float32)], [], lead
    for i, sc in enumerate(s["scenes"]):
        raw = tmp / f"line_{i:02d}.wav"
        words = ENGINES[engine](speak(sc["narration_line"]), raw, cfg)
        if engine != "edge":                            # edge already converted to 44.1 kHz mono
            to_wav(raw, tmp / "norm.wav")
            (tmp / "norm.wav").replace(raw)
        a, _ = read_wav(raw)
        a, off = trim(a, sr)
        dur = len(a) / sr
        toks = tokenize(sc["narration_line"])
        if words and len(words) == len(toks):          # engine gave real word timings
            w = [(tk, max(0, ws - off), max(0, we - off)) for tk, (_, ws, we) in zip(toks, words)]
            w = [(tk, a_, min(b_, dur)) for tk, a_, b_ in w]
        else:
            w = estimate_words(toks, dur, a, sr)
        lines.append({"idx": i, "start": t, "end": t + dur,
                      "words": [{"w": x, "start": round(t + a_, 3), "end": round(t + b_, 3)} for x, a_, b_ in w]})
        audio += [a, np.zeros(int(gap * sr), dtype=np.float32)]
        t += dur + gap
    audio.append(np.zeros(int(0.5 * sr), dtype=np.float32))   # tail so the last word isn't clipped
    voice = np.concatenate(audio)
    speech_end = lines[-1]["end"]
    tail = 0.5
    total = speech_end + tail

    # fit to the 49 s target by gentle time-stretching (keeps pitch via atempo)
    factor = 1.0
    if cfg.get("fit_to_target", True):
        target = config()["video"]["target_seconds"]
        factor = max(0.88, min(1.12, total / target))   # >1 = speed up
        if total / target > 1.12 and engine == "kokoro" and speed_mult == 1.0:   # too long: re-read a bit faster
            for p_ in tmp.glob("*"):
                p_.unlink()
            tmp.rmdir()
            return build(day, engine, speed_mult=min(1.25, total / target / 1.06))
    wav_path = d / "voice.wav"
    write_wav(tmp / "voice_raw.wav", voice, sr)
    if abs(factor - 1) > 0.01:
        run(["ffmpeg", "-y", "-v", "error", "-i", str(tmp / "voice_raw.wav"), "-filter:a", f"atempo={factor:.5f}", str(wav_path)])
    else:
        factor = 1.0
        (tmp / "voice_raw.wav").replace(wav_path)
    for ln in lines:
        ln["start"] = round(ln["start"] / factor, 3); ln["end"] = round(ln["end"] / factor, 3)
        for w in ln["words"]:
            w["start"] = round(w["start"] / factor, 3); w["end"] = round(w["end"] / factor, 3)
    total = round(ffprobe_duration(wav_path) + 0.0, 3)
    # pad the tail so video outlasts last word slightly
    scenes = [{"start": 0.0 if i == 0 else lines[i]["start"],
               "end": total if i == len(lines) - 1 else lines[i + 1]["start"]} for i in range(len(lines))]
    timing = {"engine": engine, "tempo_factor": round(factor, 4), "duration": total,
              "speech_end": lines[-1]["end"], "lines": lines, "scenes": scenes}
    (d / "timing.json").write_text(json.dumps(timing, indent=1))
    for p in tmp.glob("*"):
        p.unlink()
    tmp.rmdir()
    print(f"day {day:02d} tts[{engine}]: {total:.1f}s (tempo x{factor:.3f}), speech ends {timing['speech_end']:.1f}s")
    return timing


if __name__ == "__main__":
    build(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else None)
