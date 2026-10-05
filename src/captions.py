"""Word-timed burned-in captions as an ASS file (highlights the current word).

Writes shorts/day_XX/captions.ass and shorts/day_XX/captions.json (chunk list used by QC).
Chunks of <=3 words are shown at a time, centered in the lower third, above the bottom-20% UI zone.
"""
import json
import sys

from common import *


def ass_color(hex_rgb_str):
    r, g, b = hex_rgb(hex_rgb_str)
    return f"&H00{b:02X}{g:02X}{r:02X}"


def ts(t):
    t = max(0, t)
    h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


_FONT = {}


def text_width(text, size):
    from PIL import ImageFont
    key = size
    if key not in _FONT:
        _FONT[key] = ImageFont.truetype(str(KIT / "fonts" / "LiberationSans-Bold.ttf"), size)
    return _FONT[key].getlength(text.upper())


def make_chunks(words, max_words, max_chars=18, size=82, max_px=700):
    """Group words into chunks: <=max_words, <=max_chars and narrow enough to stay inside the safe area
    (one line at the highlighted-word scale), breaking after punctuation."""
    chunks, cur = [], []
    for w in words:
        t = " ".join(x["w"] for x in cur + [w])
        if cur and (len(t) > max_chars or text_width(t, int(size * 1.08)) > max_px):
            chunks.append(cur); cur = []
        cur.append(w)
        if len(cur) >= max_words or w["w"][-1] in ".?!,:;":
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    return chunks


def build(day):
    cfg, cap = config(), config()["captions"]
    v = cfg["video"]
    timing = load_timing(day)
    words = [w for ln in timing["lines"] for w in ln["words"]]
    chunks = make_chunks(words, cap["max_words_per_chunk"], size=cap["font_size"])
    text_w = v["width"] - 2 * cap["side_margin"]

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {v['width']}
PlayResY: {v['height']}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{cap['font']},{cap['font_size']},{ass_color(cap['text_color'])},{ass_color(cap['text_color'])},{ass_color(cap['outline_color'])},&H00000000,-1,0,0,0,100,100,0,0,1,{cap['outline_px']},0,5,{cap['side_margin']},{cap['side_margin']},0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    hi, base = ass_color(cap["highlight_color"]), ass_color(cap["text_color"])
    events, manifest = [], []
    for ci, ch in enumerate(chunks):
        nxt = chunks[ci + 1][0]["start"] if ci + 1 < len(chunks) else timing["duration"]
        for wi, w in enumerate(ch):
            start = w["start"] if wi else (ch[0]["start"])
            end = ch[wi + 1]["start"] if wi + 1 < len(ch) else min(max(w["end"] + 0.12, w["end"]), nxt)
            parts = []
            for j, x in enumerate(ch):
                col = hi if j == wi else base
                scale = r"\fscx108\fscy108" if j == wi else ""
                parts.append(f"{{\\1c{col}{scale}}}{x['w'].upper()}")
            txt = " ".join(parts)
            full_w = text_width(" ".join(x["w"] for x in ch), int(cap["font_size"] * 1.08))
            fs = f"\\fs{int(cap['font_size'] * 700 / full_w)}" if full_w > 700 else ""
            events.append(f"Dialogue: 0,{ts(start)},{ts(end)},Cap,,0,0,0,,{{\\an5{fs}\\pos({v['width'] // 2},{cap['center_y']})}}{txt}")
        manifest.append({"start": ch[0]["start"], "end": ch[-1]["end"], "text": " ".join(x["w"] for x in ch)})
    (day_dir(day) / "captions.ass").write_text(header + "\n".join(events) + "\n")
    (day_dir(day) / "captions.json").write_text(json.dumps(manifest, indent=1))
    print(f"day {day:02d} captions: {len(chunks)} chunks, {len(events)} word events")


if __name__ == "__main__":
    build(int(sys.argv[1]))
