"""Shared helpers for the Shorts pipeline."""
import csv
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "channel_kit"                   # logo, fonts, music, voice models, config.json
ASSETS = KIT                                  # (alias kept for older modules)
PLAN = ROOT / "plan"                          # topic review, content plan, calendar, tracker
SCRIPTS = ROOT / "scripts_and_sources"        # day_XX/script.json + sources.json + sources.md
BUILD = ROOT / "build"                        # temporary working files (voice, timing, captions) - not committed
VIDEOS = ROOT / "videos"                      # finished MP4s + thumbnails
OUTPUT = VIDEOS                               # (alias kept for older modules)
TRACKER = PLAN / "tracker.csv"
TRACKER_COLS = ["day", "topic", "title", "script_done", "video_done", "qc_passed",
                "scheduled_date", "uploaded", "notes"]


def config():
    return json.loads((KIT / "config.json").read_text())


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def day_dir(n):
    """Working directory for generated files (voice.wav, timing.json, captions...). Not committed."""
    d = BUILD / f"day_{int(n):02d}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def script_dir(n):
    return SCRIPTS / f"day_{int(n):02d}"


def load_script(n):
    return json.loads((script_dir(n) / "script.json").read_text())


def load_timing(n):
    return json.loads((day_dir(n) / "timing.json").read_text())


def load_topics():
    topics = {}
    for line in (PLAN / "topics_original.txt").read_text().splitlines():
        m = re.match(r"^(\d+)\.\s+(.*)$", line.strip())
        if m:
            topics[int(m.group(1))] = m.group(2)
    return topics


def load_topics_final():
    """Reviewed topic list (plan/topics_final.csv: day,topic,...) falling back to the original list."""
    f = PLAN / "topics_final.csv"
    if not f.exists():
        return load_topics()
    with f.open(newline="", encoding="utf-8") as fh:
        return {int(r["day"]): r["topic"] for r in csv.DictReader(fh)}


def tokenize(text):
    """Split narration into spoken words (keeps punctuation attached)."""
    return text.split()


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(map(str, cmd))}\n{r.stderr[-2000:]}")
    return r


def ffprobe_duration(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(path)])
    return float(r.stdout.strip())


# ---------------------------------------------------------------- tracker
def tracker_init(topics):
    if TRACKER.exists():
        return
    with TRACKER.open("w", newline="") as f:
        w = csv.DictWriter(f, TRACKER_COLS)
        w.writeheader()
        for d in sorted(topics):
            w.writerow({"day": d, "topic": topics[d], "title": "", "script_done": "FALSE",
                        "video_done": "FALSE", "qc_passed": "", "scheduled_date": "",
                        "uploaded": "FALSE", "notes": ""})


def tracker_update(day, **fields):
    with TRACKER.open(newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        if int(r["day"]) == int(day):
            for k, v in fields.items():
                r[k] = str(v)
    with TRACKER.open("w", newline="") as f:
        w = csv.DictWriter(f, TRACKER_COLS)
        w.writeheader()
        w.writerows(rows)
