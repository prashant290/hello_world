"""Build + validate scripts_and_sources/day_XX/{script.json, sources.json, sources.md} from
scripts_and_sources/_authoring/batch_*.py.   Usage: python write_scripts.py [A B]

Authoring format (see batch_01.py):
    SOURCES = {id: dict(authors, year, title, venue, url, verified, note)}
    DAYS[n] = dict(title, description_core, primary=[source ids], hashtags, caveats, thumb=(lines, accent_idx, scene_idx),
                   scenes=[(section, [(sentence, [source ids]), ...], on_screen_text, visual_description, visual_spec)])

Rule 1 (CLAUDE.md) is enforced here: every sentence needs >=1 source id that exists and is marked verified.
The id "PLAN" is allowed ONLY for questions (hooks / teasers): they assert nothing, so they carry no factual claim.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

from common import *

SECTION = {"H": "hook", "E": "explanation", "T": "takeaway", "C": "cliffhanger"}
MIN_W, MAX_W = 120, 142
CTA = "New psychology short every day on The Psyche Discourse."
CHANNEL_TAG = "#thepsychediscourse"
REQUIRED_SRC = ("authors", "year", "title", "venue", "url", "verified")


def _load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_content():
    sources, days = {}, {}
    for p in sorted((SCRIPTS / "_authoring").glob("batch_*.py")):
        mod = _load(p)
        for k, v in mod.SOURCES.items():
            sources[k] = v
        days.update(mod.DAYS)
    return sources, days


def cite(src):
    return f"{src['authors']} ({src['year']}). {src['title']}. {src['venue']}."


def build(day, d, topic, SRC):
    target = config()["video"]["target_seconds"]
    lines, rows = [], []
    for si, (sec, sents, onscreen, vis, spec) in enumerate(d["scenes"]):
        lines.append(" ".join(s for s, _ in sents))
        for s, ids in sents:
            ids = [x.strip() for x in ids.split(",")] if isinstance(ids, str) else ids
            rows.append({"scene": si, "sentence": s, "cites": ids,
                         "sources": [{"id": i, **SRC[i]} for i in ids if i in SRC]})
    voiceover = " ".join(lines)
    total = len(voiceover.split())
    scenes, acc = [], 0
    for (sec, sents, onscreen, vis, spec), line in zip(d["scenes"], lines):
        n = len(line.split())
        scenes.append({"start_sec": round(acc / total * target, 2), "end_sec": round((acc + n) / total * target, 2),
                       "section": SECTION[sec], "narration_line": line, "on_screen_text": onscreen,
                       "visual_description": vis, "visual_spec": spec})
        acc += n
    prim = " ".join(f"Source: {cite(SRC[i])}" for i in d["primary"][:2])
    out = {
        "day": day, "topic": topic, "title": d["title"], "voiceover": voiceover, "word_count": total,
        "scenes": scenes,
        "description": f"{d['description_core']} {CTA} {prim}",
        "hashtags": d["hashtags"] + ([CHANNEL_TAG] if CHANNEL_TAG not in d["hashtags"] else []),
        "accuracy_note": d["caveats"],
        "thumbnail": {"lines": d["thumb"][0], "accent_line": d["thumb"][1], "scene": d["thumb"][2]},
    }
    return out, rows


def validate(s, rows, SRC):
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
    if s["scenes"][0]["section"] != "hook" or s["scenes"][-1]["section"] != "cliffhanger":
        errs.append("must start with hook and end with cliffhanger")
    if not re.match(r"Tomorrow", s["scenes"][-1]["narration_line"]) or not s["scenes"][-1]["narration_line"].rstrip().endswith("?"):
        errs.append("closing line must be a 'Tomorrow: ...?' teaser question")
    for r in rows:
        ids = r["cites"]
        if not ids:
            errs.append(f"UNCITED sentence: {r['sentence']!r}")
        for i in ids:
            if i == "PLAN":
                if not r["sentence"].rstrip().endswith("?"):
                    errs.append(f"PLAN cite only allowed on questions: {r['sentence']!r}")
            elif i not in SRC:
                errs.append(f"unknown source id {i!r} in {r['sentence']!r}")
            else:
                miss = [k for k in REQUIRED_SRC if not SRC[i].get(k)]
                if miss:
                    errs.append(f"source {i} missing {miss}")
                elif not str(SRC[i]["url"]).startswith("https://"):
                    errs.append(f"source {i} url must be https")
    return errs


def write(day, s, rows):
    d = script_dir(day)
    d.mkdir(parents=True, exist_ok=True)
    (d / "script.json").write_text(json.dumps(s, indent=2, ensure_ascii=False))
    (d / "sources.json").write_text(json.dumps({"day": day, "sentences": rows}, indent=2, ensure_ascii=False))
    md = [f"# Day {day}: {s['title']} — source table", "", f"Topic: {s['topic']}  ", f"Words: {s['word_count']}", "",
          "| # | Sentence (spoken) | Source(s) | How it was checked |", "|---|---|---|---|"]
    for n, r in enumerate(rows, 1):
        if r["cites"] == ["PLAN"]:
            src_txt, chk = "— (question; makes no claim)", "n/a"
        else:
            src_txt = "<br>".join(f"{x['authors']} ({x['year']}). *{x['title']}*. {x['venue']}. [link]({x['url']})" for x in r["sources"])
            chk = "<br>".join(x["verified"] for x in r["sources"])
        md.append(f"| {n} | {r['sentence']} | {src_txt} | {chk} |")
    md += ["", "## Caveats / contested points", "", s["accuracy_note"], ""]
    (d / "sources.md").write_text("\n".join(md))


if __name__ == "__main__":
    SRC, content = load_content()
    topics = load_topics_final()
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (1, 90)
    bad = 0
    for day in sorted(content):
        if not a <= day <= b:
            continue
        s, rows = build(day, content[day], topics.get(day, content[day].get("topic", "")), SRC)
        errs = validate(s, rows, SRC)
        print(f"day {day:02d}  words={s['word_count']:3d}  sentences={len(rows):2d}  {'OK' if not errs else ''}")
        for e in errs:
            print("    -", e)
        if errs:
            bad += 1
            continue
        write(day, s, rows)
        tracker_update(day, title=s["title"], script_done="TRUE")
    sys.exit(1 if bad else 0)
