"""Branded vertical thumbnails (1080x1920): big headline + the day's key drawing + logo.
Writes shorts/day_XX/thumbnail.png and output/thumbnails/day_XX.png.   Usage: python thumbnails.py [A B]"""
import sys

from PIL import Image, ImageDraw, ImageFont

import visuals
from common import *

W, H = 1080, 1920


def fit_font(lines, maxw, start=190):
    for sz in range(start, 60, -4):
        f = ImageFont.truetype(visuals.FONT_B, sz)
        if max(f.getlength(l) for l in lines) <= maxw:
            return f, sz
    return f, sz


def build(day):
    s = load_script(day)
    style = config()["style"]
    bg, ink, acc = hex_rgb(style["background"]), hex_rgb(style["ink"]), hex_rgb(style["accent"])
    th = s["thumbnail"]
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    # key drawing (reuse the scene art, no on-screen text), scaled up
    sc = dict(s["scenes"][th["scene"]]); sc["on_screen_text"] = ""
    layer, _ = visuals.draw_scene(0, sc, style)
    k = 1.2
    lw, lh = layer.size
    layer = layer.resize((int(W * k), int((visuals.REGION_Y1 - visuals.REGION_Y0) * k)), Image.LANCZOS)
    img.paste(layer, (int((W - layer.width) / 2), 350), layer)

    # headline
    f, sz = fit_font(th["lines"], 940)
    y = 150
    for i, line in enumerate(th["lines"]):
        col = acc if i == th["accent_line"] else ink
        w = f.getlength(line)
        d.text(((W - w) / 2, y), line, font=f, fill=col)
        y += sz * 1.08
    d.rounded_rectangle([(W - 760) / 2, y + 10, (W + 760) / 2, y + 26], radius=8, fill=acc)

    # brand footer
    lg = Image.open(ASSETS / "logo.png").convert("RGBA").resize((150, 150), Image.LANCZOS)
    img.paste(lg, (70, 1710), lg)
    ft = ImageFont.truetype(visuals.FONT_B, 46)
    d.text((245, 1745), "THE PSYCHE", font=ft, fill=ink)
    d.text((245, 1795), "DISCOURSE", font=ft, fill=acc)
    d.text((W - 70 - ImageFont.truetype(visuals.FONT_B, 56).getlength(f"DAY {day}"), 1760), f"DAY {day}",
           font=ImageFont.truetype(visuals.FONT_B, 56), fill=ink)

    (OUTPUT / "thumbnails").mkdir(parents=True, exist_ok=True)
    img.save(day_dir(day) / "thumbnail.png")
    img.save(OUTPUT / "thumbnails" / f"day_{day:02d}.png")
    return img


if __name__ == "__main__":
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (1, 10)
    for dd in range(a, b + 1):
        if (day_dir(dd) / "script.json").exists():
            build(dd); print("thumbnail", dd)
