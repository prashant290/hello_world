"""Generate royalty-free background music (pure synthesis -> no licensing issues).
Writes assets/music/ambient_1..3.wav (60 s, stereo, loopable-ish soft pads + plucks)."""
import wave
import numpy as np
from common import *

SR = 44100
NOTE = lambda m: 440.0 * 2 ** ((m - 69) / 12)
PROGS = {  # 4 chords x 15 s, midi notes
    1: [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]],
    2: [[50, 53, 57], [46, 50, 53], [53, 57, 60], [48, 52, 55]],
    3: [[52, 55, 59], [48, 52, 55], [45, 48, 52], [50, 54, 57]],
}


def pad(freq, n):
    t = np.arange(n) / SR
    y = sum(np.sin(2 * np.pi * freq * k * t + ph) * amp
            for k, amp, ph in ((1, 1, 0), (2, .35, 1), (3, .15, 2)))
    y += 0.6 * np.sin(2 * np.pi * freq * 1.003 * t)          # slight detune = warmth
    return y


def make(idx):
    seg = 15 * SR
    out = np.zeros((4 * seg + 4 * SR, 2))
    rng = np.random.default_rng(idx)
    for ci, chord in enumerate(PROGS[idx]):
        n = seg + 4 * SR
        env = np.minimum(np.linspace(0, 1, n) * (n / (3 * SR)), 1) * np.minimum(np.linspace(1, 0, n) * (n / (4 * SR)), 1)
        for ni, m in enumerate(chord):
            y = pad(NOTE(m), n) * env * 0.12
            pan = 0.35 + 0.3 * ni / 2
            out[ci * seg:ci * seg + n, 0] += y * (1 - pan)
            out[ci * seg:ci * seg + n, 1] += y * pan
        for beat in range(0, 15 * 2, 1):                      # soft pluck every 0.5 s
            m = chord[(beat * 7 + idx) % 3] + 12 * rng.integers(1, 2)
            start = ci * seg + int(beat * 0.5 * SR)
            L = int(1.2 * SR)
            tt = np.arange(L) / SR
            pl = np.sin(2 * np.pi * NOTE(m) * tt) * np.exp(-tt * 4) * 0.05
            out[start:start + L, 0] += pl; out[start:start + L, 1] += pl * 0.8
    out = out[:4 * seg]
    out /= np.abs(out).max() * 1.1
    return out


for i in (1, 2, 3):
    d = ASSETS / "music"
    d.mkdir(exist_ok=True)
    y = make(i)
    with wave.open(str(d / f"ambient_{i}.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((y * 32767).astype(np.int16).tobytes())
    print("wrote", d / f"ambient_{i}.wav")
