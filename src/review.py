"""Self-review helper (CLAUDE.md rule 3): for a built day, (1) make a contact sheet of frames to LOOK at, and
(2) transcribe the final audio offline (pocketsphinx) and compare it with the script's spoken words.
Usage: python review.py N    -> writes build/day_XX/review_sheet.png and prints the transcript match."""
import difflib
import re
import subprocess
import sys

from PIL import Image

from common import *


def sheet(day, per_row=6):
    mp4 = VIDEOS / f"day_{day:02d}.mp4"
    t = load_timing(day)
    times = [(s["start"] + s["end"]) / 2 for s in t["scenes"]]            # middle of each scene
    out = day_dir(day) / "review_sheet.png"
    tiles = []
    for i, tm in enumerate(times):
        p = day_dir(day) / f"_f{i}.png"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{tm:.2f}", "-i", str(mp4), "-frames:v", "1",
                        "-vf", "scale=300:-1", str(p)], check=True)
        tiles.append(Image.open(p))
    rows = (len(tiles) + per_row - 1) // per_row
    w, h = tiles[0].size
    img = Image.new("RGB", (per_row * w, rows * h), (255, 255, 255))
    for i, im in enumerate(tiles):
        img.paste(im, ((i % per_row) * w, (i // per_row) * h))
    img.save(out)
    for i in range(len(tiles)):
        (day_dir(day) / f"_f{i}.png").unlink()
    return out


def transcribe(day):
    from pocketsphinx import Decoder, get_model_path  # noqa
    mp4 = VIDEOS / f"day_{day:02d}.mp4"
    raw = day_dir(day) / "_asr.raw"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp4), "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", str(raw)], check=True)
    dec = Decoder(samprate=16000)
    dec.start_utt()
    dec.process_raw(raw.read_bytes(), False, True)
    dec.end_utt()
    raw.unlink()
    return dec.hyp().hypstr if dec.hyp() else ""


def norm(s):
    return re.sub(r"[^a-z0-9' ]", "", s.lower().replace("-", " ").replace("$", " dollars ")).split()


def match(day):
    spoken = load_script(day)["voiceover"]
    hyp = transcribe(day)
    a, b = norm(spoken), norm(hyp)
    r = difflib.SequenceMatcher(a=a, b=b, autojunk=False).ratio()
    return r, hyp


if __name__ == "__main__":
    d = int(sys.argv[1])
    print("contact sheet:", sheet(d))
    r, hyp = match(d)
    print(f"transcript similarity {r:.2f} (pocketsphinx is a weak recognizer; >0.45 means the right words are being spoken)")
    print("heard:", hyp[:300])
