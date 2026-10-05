"""Build + validate shorts/day_XX/script.json from scripts/content/batch_*.py.

Usage: python write_scripts.py [A B]     (default: every day found in content files)
"""
import importlib
import json
import sys
from pathlib import Path

from common import *

SECTION = {"H": "hook", "E": "explanation", "T": "takeaway", "C": "cliffhanger"}
MIN_W, MAX_W = 125, 135


def load_content():
    days = {}
    for p in sorted((Path(__file__).parent / "content").glob("batch_*.py")):
        mod = importlib.import_module(f"content.{p.stem}")
        days.update(mod.DAYS)
    return days


def load_meta():
    meta, thumbs = {}, {}
    for p in sorted((Path(__file__).parent / "content").glob("meta_*.py")):
        mod = importlib.import_module(f"content.{p.stem}")
        meta.update(mod.META); thumbs.update(mod.THUMBS)
    return meta, thumbs


def build(day, d, topic):
    lines = [s[1] for s in d["scenes"]]
    voiceover = " ".join(lines)
    total = len(voiceover.split())
    target = config()["video"]["target_seconds"]
    scenes, acc = [], 0
    for sec, line, onscreen, vis, spec in d["scenes"]:
        n = len(line.split())
        scenes.append({
            "start_sec": round(acc / total * target, 2),
            "end_sec": round((acc + n) / total * target, 2),
            "section": SECTION[sec],
            "narration_line": line,
            "on_screen_text": onscreen,
            "visual_description": vis,
            "visual_spec": spec,
        })
        acc += n
    meta, thumbs = load_meta()
    m = meta.get(day, {})
    d = {**d, **m}
    out = {
        "day": day, "topic": topic, "title": d["title"],
        "voiceover": voiceover, "word_count": total,
        "estimated_duration_sec_note": "scene times are estimates; tts.py writes the real ones to timing.json",
        "scenes": scenes,
        "description": d["description"], "hashtags": d["hashtags"],
        "accuracy_note": d["accuracy_note"],
    }
    if day in thumbs:
        lines, acc, sc = thumbs[day]
        out["thumbnail"] = {"lines": lines, "accent_line": acc, "scene": sc}
    return out


def validate(s):
    errs = []
    if not MIN_W <= s["word_count"] <= MAX_W:
        errs.append(f"word count {s['word_count']} not in {MIN_W}-{MAX_W}")
    if len(s["title"]) >= 60:
        errs.append(f"title {len(s['title'])} chars")
    for sc in s["scenes"]:
        if len(sc["on_screen_text"].split()) > 6:
            errs.append(f"on-screen text >6 words: {sc['on_screen_text']!r}")
    h = [x.lower() for x in s["hashtags"]]
    if not 5 <= len(h) <= 8 or "#psychology" not in h or "#shorts" not in h:
        errs.append(f"hashtags invalid: {s['hashtags']}")
    if "Source:" not in s["description"]:
        errs.append("description lacks a Source reference")
    if s["scenes"][0]["section"] != "hook" or s["scenes"][-1]["section"] != "cliffhanger":
        errs.append("must start with hook and end with cliffhanger")
    return errs


if __name__ == "__main__":
    topics = load_topics()
    content = load_content()
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (1, 90)
    bad = 0
    for day in sorted(content):
        if not a <= day <= b:
            continue
        s = build(day, content[day], topics[day])
        errs = validate(s)
        print(f"day {day:02d}  words={s['word_count']:3d}  title({len(s['title'])})  {'OK' if not errs else errs}")
        if errs:
            bad += 1
            continue
        (day_dir(day) / "script.json").write_text(json.dumps(s, indent=2, ensure_ascii=False))
        tracker_update(day, title=s["title"], script_done="TRUE")
    sys.exit(1 if bad else 0)
