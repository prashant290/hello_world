"""Create one animated clip per scene: minimalist hand-drawn stickman with a 3-frame "boil" wobble.

Style (colors/line width/boil fps) comes from config.json -> style. Drawing is fully procedural
(Pillow), so it is free, offline and deterministic. Writes shorts/day_XX/scenes/scene_XX.mp4 and
scenes.json (on-screen-text bounding boxes used by QC).

Visual spec grammar (script.json -> scenes[].visual_spec):
    "pose/face/where ; prop:arg@slot ; prop:arg@slot"
    pose  : stand | think | shock | point | shrug | walk
    face  : neutral | smile | worry | shock
    where : L | C   (C centers the figure when there are no props)
    slots : TL TR R L C B
"""
import json
import math
import random
import subprocess
import sys
from multiprocessing import Pool

from PIL import Image, ImageDraw, ImageFont

from common import *

W, H = 1080, 1920
REGION_Y0, REGION_Y1 = 100, 1340           # logical y-range drawn each frame (text + stage)
S = 2                                      # supersampling
FONT_B = str(ROOT / "assets" / "fonts" / "LiberationSans-Bold.ttf")
SLOTS = {"TL": (300, 520), "TR": (730, 520), "R": (730, 780), "L": (300, 780), "C": (540, 780), "B": (730, 1080)}


def font(sz):
    return ImageFont.truetype(FONT_B, int(sz * S))


class Pen:
    def __init__(self, variant, style):
        self.v = variant
        self.n = 0
        self.ink = hex_rgb(style["ink"]) + (255,)
        self.acc = hex_rgb(style["accent"]) + (255,)
        self.bg = hex_rgb(style["background"]) + (255,)
        self.lw = style["line_width"]
        self.img = Image.new("RGBA", (W * S, (REGION_Y1 - REGION_Y0) * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    def _rng(self):
        self.n += 1
        return random.Random(self.v * 100003 + self.n * 7919)

    def px(self, p, off=(0, 0)):
        return ((p[0] + off[0]) * S, (p[1] + off[1] - REGION_Y0) * S)

    def line(self, pts, w=None, color=None, closed=False):
        r = self._rng()
        off = (r.uniform(-2.6, 2.6), r.uniform(-2.6, 2.6))
        pts = list(pts) + ([pts[0]] if closed else [])
        out = []
        for a, b in zip(pts, pts[1:]):                         # subdivide for a hand-drawn bend
            nx, ny = -(b[1] - a[1]), b[0] - a[0]
            ln = math.hypot(nx, ny) or 1
            k = r.uniform(-1.6, 1.6)
            for t in (0, .5):
                q = ((a[0] + (b[0] - a[0]) * t) + nx / ln * (k if t else 0), (a[1] + (b[1] - a[1]) * t) + ny / ln * (k if t else 0))
                out.append((q[0] + r.uniform(-.9, .9), q[1] + r.uniform(-.9, .9)))
        out.append((pts[-1][0] + r.uniform(-.9, .9), pts[-1][1] + r.uniform(-.9, .9)))
        P = [self.px(p, off) for p in out]
        w = (w or self.lw) * S
        c = color or self.ink
        self.d.line(P, fill=c, width=int(w), joint="curve")
        for p in (P[0], P[-1]):
            self.d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=c)

    def ellipse(self, c, rx, ry=None, fill=None, color=None, w=None, a0=0, a1=360):
        ry = ry or rx
        pts = [(c[0] + rx * math.cos(math.radians(a)), c[1] + ry * math.sin(math.radians(a)))
               for a in range(int(a0), int(a1) + 1, 12)]
        if fill:
            self.d.polygon([self.px(p) for p in pts], fill=fill)
        self.line(pts, w, color, closed=(a1 - a0 >= 360))

    def poly(self, pts, fill=None, color=None, w=None):
        if fill:
            self.d.polygon([self.px(p) for p in pts], fill=fill)
        self.line(pts, w, color, closed=True)

    def text(self, xy, s, size, color=None, anchor="mm"):
        r = self._rng()
        x, y = xy[0] + r.uniform(-1.8, 1.8), xy[1] + r.uniform(-1.8, 1.8)
        self.d.text(self.px((x, y)), s, font=font(size), fill=color or self.ink, anchor=anchor)

    def wrapped(self, xy, s, size, maxw, color=None, lh=1.12):
        lines, cur = [], ""
        for wd in s.split():
            t = (cur + " " + wd).strip()
            if font(size).getlength(t) / S <= maxw or not cur:
                cur = t
            else:
                lines.append(cur); cur = wd
        lines.append(cur)
        y0 = xy[1] - (len(lines) - 1) * size * lh / 2
        for i, ln in enumerate(lines):
            self.text((xy[0], y0 + i * size * lh), ln, size, color)
        return lines


# ---------------------------------------------------------------- figure
POSES = {   # (upper, lower) angles in degrees (0=east, 90=down); legs (left, right)
    "stand": dict(la=(112, 102), ra=(68, 78), legs=(100, 80)),
    "think": dict(la=(112, 102), ra=(28, -128), legs=(100, 80)),
    "shock": dict(la=(-150, -105), ra=(-30, -75), legs=(104, 76)),
    "point": dict(la=(112, 102), ra=(-6, -6), legs=(100, 80)),
    "shrug": dict(la=(150, -110), ra=(30, -70), legs=(100, 80)),
    "walk": dict(la=(75, 60), ra=(105, 120), legs=(122, 58)),
}


def seg(p, ang, ln):
    return (p[0] + ln * math.cos(math.radians(ang)), p[1] + ln * math.sin(math.radians(ang)))


def draw_figure(pen, x, feet, pose="stand", face="neutral", scale=1.0):
    P = POSES.get(pose, POSES["stand"])
    k = scale
    hip = (x, feet - 172 * k)
    neck = (x, hip[1] - 190 * k)
    head = (x, neck[1] - 66 * k)
    sh = (x, neck[1] + 26 * k)
    pen.line([neck, hip])
    for (u, l), sgn in ((P["la"], -1), (P["ra"], 1)):
        e = seg(sh, u, 66 * k)
        pen.line([sh, e, seg(e, l, 62 * k)])
    for a in P["legs"]:
        pen.line([hip, seg(hip, a, 172 * k)])
    pen.ellipse(head, 62 * k, fill=pen.bg)
    ex = 22 * k
    if face == "shock":
        for s_ in (-1, 1):
            pen.ellipse((head[0] + s_ * ex, head[1] - 10 * k), 8 * k, w=5)
        pen.ellipse((head[0], head[1] + 30 * k), 10 * k, 14 * k, w=5)
    else:
        for s_ in (-1, 1):
            pen.ellipse((head[0] + s_ * ex, head[1] - 10 * k), 3.5 * k, fill=pen.ink, w=3)
        if face == "smile":
            pen.ellipse((head[0], head[1] + 14 * k), 26 * k, 16 * k, a0=20, a1=160, w=6)
        elif face == "worry":
            pen.ellipse((head[0], head[1] + 44 * k), 22 * k, 12 * k, a0=200, a1=340, w=6)
            pen.line([(head[0] - ex - 12 * k, head[1] - 30 * k), (head[0] - ex + 12 * k, head[1] - 38 * k)], w=5)
            pen.line([(head[0] + ex + 12 * k, head[1] - 30 * k), (head[0] + ex - 12 * k, head[1] - 38 * k)], w=5)
        else:
            pen.line([(head[0] - 16 * k, head[1] + 28 * k), (head[0] + 16 * k, head[1] + 28 * k)], w=6)
    pen.line([(x - 150 * k, feet + 36 * k), (x + 150 * k, feet + 36 * k)], w=5)      # ground
    return head


# ---------------------------------------------------------------- props
def p_bubble(pen, c, arg, ctx):
    pen.ellipse((c[0], c[1]), 160, 92, fill=pen.bg)
    for off, r in (((-170, 120), 20), ((-215, 175), 11)):
        pen.ellipse((c[0] + off[0], c[1] + off[1]), r, fill=pen.bg, w=6)
    pen.wrapped(c, arg or "?", 40, 250)


def p_text(pen, c, arg, ctx):
    pen.wrapped(c, arg or "", 62, 330, color=pen.ink)
    pen.line([(c[0] - 150, c[1] + 98), (c[0] + 150, c[1] + 98)], w=10, color=pen.acc)


def p_waves(pen, c, arg, ctx):
    for i in range(3):
        y = c[1] - 80 + i * 80
        pen.line([(c[0] - 120 + j * 20, y + (14 if j % 2 else -14)) for j in range(13)], w=8, color=pen.acc)


def p_brain(pen, c, arg, ctx):
    pen.ellipse((c[0] - 60, c[1]), 120, 100, fill=pen.bg)
    pen.ellipse((c[0] + 60, c[1]), 120, 100, fill=pen.bg)
    for dx in (-110, -40, 40, 110):
        pen.line([(c[0] + dx, c[1] - 50), (c[0] + dx + 24, c[1] - 10), (c[0] + dx - 6, c[1] + 28), (c[0] + dx + 20, c[1] + 60)], w=5)
    if arg:
        pen.ellipse((c[0] + 30, c[1] + 50), 22, fill=pen.acc, color=pen.acc)
        pen.text((c[0] + 30, c[1] + 140), arg, 34, pen.acc)


def p_tag(pen, c, arg, ctx):
    pts = [(c[0] - 150, c[1]), (c[0] - 90, c[1] - 85), (c[0] + 150, c[1] - 85), (c[0] + 150, c[1] + 85), (c[0] - 90, c[1] + 85)]
    pen.poly(pts, fill=pen.bg)
    pen.ellipse((c[0] - 96, c[1]), 11, w=5)
    pen.text((c[0] + 22, c[1]), arg or "", 74 if len(arg or "") <= 6 else 46, pen.acc)


def p_bars(pen, c, arg, ctx):
    """bars:label=value%,label=value% -- values scale bars; unlabeled values use a short/tall default."""
    items = []
    for tok in (arg or "a,b").split(","):
        lab, _, val = tok.partition("=")
        items.append((lab.strip(), val.strip()))
    known = {"calm": 90, "emotional": 300, "room": 110, "door": 290}
    base = c[1] + 190
    for i, (lab, val) in enumerate(items):
        if val.endswith("%"):
            hh = float(val.rstrip("%")) / 100 * 560
        else:
            hh = known.get(lab, 120 if i == 0 else 300)
        x = c[0] - 90 + i * 190
        pen.poly([(x - 55, base), (x - 55, base - hh), (x + 55, base - hh), (x + 55, base)],
                 fill=pen.acc if i == len(items) - 1 else (210, 205, 195, 255))
        pen.text((x, base + 40), lab, 34)
        if val.endswith("%"):
            pen.text((x, base - hh - 32), "~" + val, 40, pen.acc)
    pen.line([(c[0] - 190, base), (c[0] + 190, base)], w=6)


def p_loop(pen, c, arg, ctx):
    pen.ellipse(c, 110, a0=40, a1=380, w=11, color=pen.acc)
    e = (c[0] + 110 * math.cos(math.radians(20)), c[1] + 110 * math.sin(math.radians(20)))
    pen.line([(e[0] - 40, e[1] - 40), e, (e[0] + 30, e[1] - 50)], w=11, color=pen.acc)


def p_lines(pen, c, arg, ctx):
    a, b = (arg or "a,b").split(",")
    pen.line([(c[0] - 170, c[1] - 170), (c[0] - 170, c[1] + 150), (c[0] + 170, c[1] + 150)], w=6)
    pen.line([(c[0] - 170, c[1] - 110), (c[0] + 170, c[1] - 120)], w=10, color=pen.acc)
    pen.line([(c[0] - 170, c[1] - 90), (c[0] - 20, c[1] - 20), (c[0] + 170, c[1] + 90)], w=10)
    pen.text((c[0] + 20, c[1] - 160), a, 36, pen.acc)
    pen.text((c[0] + 90, c[1] + 120), b, 36)


def p_crowd(pen, c, arg, ctx):
    n = int(arg or 4)
    cols = min(n, 5)
    for i in range(n):
        x = c[0] - (cols - 1) * 50 + (i % cols) * 100
        y = c[1] + (i // cols) * 150 - 40
        pen.ellipse((x, y), 26, fill=pen.bg, w=6)
        pen.line([(x, y + 26), (x, y + 90)], w=6)
        pen.line([(x - 28, y + 55), (x, y + 44), (x + 28, y + 55)], w=6)
        pen.line([(x, y + 90), (x - 20, y + 130)], w=6); pen.line([(x, y + 90), (x + 20, y + 130)], w=6)


def p_spotlight(pen, c, arg, ctx):
    fx = ctx["fig_x"]
    pen.poly([(fx - 40, 330), (fx + 40, 330), (fx + 210, 1150), (fx - 210, 1150)], fill=(255, 224, 150, 90), color=pen.acc, w=5)
    pen.ellipse((fx, 1150), 215, 38, color=pen.acc, w=5)


def p_tshirt(pen, c, arg, ctx):
    pts = [(c[0] - 70, c[1] - 130), (c[0] - 150, c[1] - 90), (c[0] - 115, c[1] - 30), (c[0] - 75, c[1] - 55),
           (c[0] - 75, c[1] + 130), (c[0] + 75, c[1] + 130), (c[0] + 75, c[1] - 55), (c[0] + 115, c[1] - 30),
           (c[0] + 150, c[1] - 90), (c[0] + 70, c[1] - 130), (c[0] + 30, c[1] - 105), (c[0] - 30, c[1] - 105)]
    pen.poly(pts, fill=pen.bg)
    pen.text((c[0], c[1] + 30), arg or "", 34, pen.acc)


def p_arrow(pen, c, arg, ctx):
    if arg == "down":
        pen.line([(c[0], c[1] - 110), (c[0], c[1] + 110)], w=14, color=pen.acc)
        pen.line([(c[0] - 55, c[1] + 55), (c[0], c[1] + 115), (c[0] + 55, c[1] + 55)], w=14, color=pen.acc)
    else:
        pen.line([(c[0] - 110, c[1]), (c[0] + 110, c[1])], w=14, color=pen.acc)
        pen.line([(c[0] + 55, c[1] - 55), (c[0] + 115, c[1]), (c[0] + 55, c[1] + 55)], w=14, color=pen.acc)


def p_clock(pen, c, arg, ctx):
    pen.ellipse(c, 120, fill=pen.bg)
    for a in range(0, 360, 30):
        pen.line([seg(c, a, 100), seg(c, a, 114)], w=5)
    pen.line([c, seg(c, -90, 80)], w=9); pen.line([c, seg(c, 20, 60)], w=9, color=pen.acc)


def p_door(pen, c, arg, ctx):
    pen.poly([(c[0] - 100, c[1] + 190), (c[0] - 100, c[1] - 170), (c[0] + 100, c[1] - 170), (c[0] + 100, c[1] + 190)], fill=(235, 230, 218, 255))
    pen.poly([(c[0] - 62, c[1] + 190), (c[0] - 62, c[1] - 130), (c[0] + 62, c[1] - 130), (c[0] + 62, c[1] + 190)], fill=pen.bg)
    pen.ellipse((c[0] + 38, c[1] + 30), 9, fill=pen.acc, color=pen.acc)


def p_notes(pen, c, arg, ctx):
    for dx, dy in ((-70, 30), (50, -20)):
        x, y = c[0] + dx, c[1] + dy
        pen.ellipse((x, y + 60), 32, 24, fill=pen.ink, color=pen.ink)
        pen.line([(x + 30, y + 55), (x + 30, y - 85), (x + 85, y - 55)], w=9)


def p_scale(pen, c, arg, ctx):
    pen.line([(c[0], c[1] + 190), (c[0], c[1] - 90)], w=10)
    pen.line([(c[0] - 150, c[1] - 55), (c[0] + 150, c[1] - 125)], w=10)
    for dx, dy, col in ((-150, -55, None), (150, -125, pen.acc)):
        pen.line([(c[0] + dx - 60, c[1] + dy + 80), (c[0] + dx, c[1] + dy), (c[0] + dx + 60, c[1] + dy + 80)], w=5)
        pen.ellipse((c[0] + dx, c[1] + dy + 82), 70, 14, fill=col or pen.bg)


def p_coin(pen, c, arg, ctx):
    pen.ellipse(c, 110, fill=(255, 235, 170, 255) if (arg or "").startswith("+") else pen.bg)
    pen.ellipse(c, 88, w=4)
    pen.text(c, arg or "$", 52 if len(arg or "$") <= 5 else 38, pen.acc if (arg or "").startswith("-") else pen.ink)


def p_wheel(pen, c, arg, ctx):
    pen.ellipse(c, 150, fill=pen.bg)
    for a in range(0, 360, 45):
        pen.line([c, seg(c, a, 150)], w=5)
    pen.ellipse(c, 52, fill=pen.bg)
    pen.text(c, arg or "", 56, pen.acc)
    pen.poly([(c[0] - 18, c[1] - 175), (c[0] + 18, c[1] - 175), (c[0], c[1] - 135)], fill=pen.acc, color=pen.acc)


def p_qmark(pen, c, arg, ctx):
    pen.text(c, "?", 300, pen.acc)


def p_check(pen, c, arg, ctx):
    pen.line([(c[0] - 90, c[1]), (c[0] - 30, c[1] + 70), (c[0] + 100, c[1] - 90)], w=24, color=pen.acc)


def p_cross(pen, c, arg, ctx):
    pen.line([(c[0] - 80, c[1] - 80), (c[0] + 80, c[1] + 80)], w=24, color=pen.acc)
    pen.line([(c[0] + 80, c[1] - 80), (c[0] - 80, c[1] + 80)], w=24, color=pen.acc)


def p_list(pen, c, arg, ctx):
    items = (arg or "a,b,c").split(",")
    h = 80 * len(items)
    pen.poly([(c[0] - 170, c[1] - h / 2 - 20), (c[0] + 170, c[1] - h / 2 - 20), (c[0] + 170, c[1] + h / 2 + 20), (c[0] - 170, c[1] + h / 2 + 20)], fill=pen.bg)
    for i, it in enumerate(items):
        y = c[1] - h / 2 + 40 + i * 80
        pen.poly([(c[0] - 140, y - 20), (c[0] - 100, y - 20), (c[0] - 100, y + 20), (c[0] - 140, y + 20)], w=5)
        if i % 2 == 0 and it.upper() != "TODO":
            pen.line([(c[0] - 136, y), (c[0] - 120, y + 14), (c[0] - 98, y - 24)], w=6, color=pen.acc)
        pen.text((c[0] + 20, y), it, 44)


def p_numbers(pen, c, arg, ctx):
    toks = (arg or "").split()
    for i, t in enumerate(toks):
        pen.text((c[0] + (i - (len(toks) - 1) / 2) * 120, c[1]), t, 130 if len(toks) <= 3 else 100, pen.ink if i < len(toks) else pen.acc)
    pen.line([(c[0] - 180, c[1] + 90), (c[0] + 180, c[1] + 90)], w=10, color=pen.acc)


def p_lightbulb(pen, c, arg, ctx):
    pen.ellipse((c[0], c[1] - 20), 80, fill=(255, 235, 170, 255))
    pen.poly([(c[0] - 34, c[1] + 50), (c[0] + 34, c[1] + 50), (c[0] + 26, c[1] + 100), (c[0] - 26, c[1] + 100)], fill=pen.bg)
    for a in (-150, -110, -70, -30, 180, 0):
        pen.line([seg((c[0], c[1] - 20), a, 105), seg((c[0], c[1] - 20), a, 140)], w=7, color=pen.acc)


def p_magnet(pen, c, arg, ctx):
    pen.ellipse(c, 100, a0=0, a1=180, w=34, color=pen.acc)
    pen.line([(c[0] - 100, c[1]), (c[0] - 100, c[1] - 90)], w=34, color=pen.acc)
    pen.line([(c[0] + 100, c[1]), (c[0] + 100, c[1] - 90)], w=34, color=pen.acc)
    pen.line([(c[0] - 100, c[1] - 95), (c[0] - 100, c[1] - 120)], w=34, color=pen.ink)
    pen.line([(c[0] + 100, c[1] - 95), (c[0] + 100, c[1] - 120)], w=34, color=pen.ink)


PROPS = {k[2:]: v for k, v in globals().items() if k.startswith("p_")}


def parse_spec(spec):
    parts = [p.strip() for p in spec.split(";") if p.strip()]
    pose, face, where = (parts[0].split("/") + ["neutral", "L"])[:3]
    props = []
    for p in parts[1:]:
        body, _, slot = p.partition("@")
        name, _, arg = body.partition(":")
        props.append((name.strip(), arg.strip(), (slot or "R").strip()))
    return pose, face, where, props


def draw_scene(variant, scene, style):
    pen = Pen(variant, style)
    pose, face, where, props = parse_spec(scene["visual_spec"])
    has_right = any(s in ("R", "TR", "B") for _, _, s in props)
    fig_x = 540 if (where == "C" and not has_right) else 300
    bbox = None
    ot = scene["on_screen_text"]
    if ot:
        fsz = 96
        lines = pen.wrapped((540, 300), ot, fsz, 780, color=pen.ink)
        f = font(fsz)
        wmax = max(f.getlength(l) / S for l in lines)
        hh = len(lines) * fsz * 1.12
        bbox = [540 - wmax / 2, 300 - hh / 2, 540 + wmax / 2, 300 + hh / 2]
        pen.line([(540 - wmax / 2, bbox[3] + 14), (540 + wmax / 2, bbox[3] + 14)], w=10, color=pen.acc)
    draw_figure(pen, fig_x, 1140, pose, face)
    ctx = {"fig_x": fig_x}
    for name, arg, slot in props:
        fn = PROPS.get(name)
        if fn is None:
            print("  ! unknown prop", name)
            continue
        c = SLOTS.get(slot, SLOTS["R"])
        if where == "C" and not has_right:
            c = (c[0], c[1])
        fn(pen, c, arg, ctx)
    return pen.img, bbox


_LOGO = {}


def logo():
    if "img" not in _LOGO:
        p = ASSETS / "logo.png"
        _LOGO["img"] = Image.open(p).convert("RGBA").resize((110, 110), Image.LANCZOS) if p.exists() else None
    return _LOGO["img"]


def to_frame(layer, bgrgb, progress=1.0):
    """Composite a (possibly popped-in) stage layer onto the background at 1x."""
    if progress < 1.0:
        sc = 0.9 + 0.1 * (1 - (1 - progress) ** 3)
        w, h = layer.size
        small = layer.resize((int(w * sc), int(h * sc)), Image.BILINEAR)
        lay = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        lay.paste(small, ((w - small.width) // 2, (h - small.height) // 2))
        a = lay.getchannel("A").point(lambda v: int(v * min(1.0, progress * 1.4)))
        lay.putalpha(a)
        layer = lay
    layer1 = layer.resize((W, REGION_Y1 - REGION_Y0), Image.LANCZOS)
    frame = Image.new("RGB", (W, H), bgrgb)
    frame.paste(layer1, (0, REGION_Y0), layer1)
    lg = logo()
    if lg is not None:
        frame.paste(lg, (46, 122), lg)
    return frame


def render_clip(args):
    day, i, scene, duration = args
    style = config()["style"]
    bgrgb = hex_rgb(style["background"])
    layers, bbox = [], None
    for v in range(3):
        img, bbox = draw_scene(v, scene, style)
        layers.append(img)
    fps = style["boil_fps"]
    n = max(1, round(duration * fps))
    pop = 6
    cache = {}
    out = day_dir(day) / "scenes" / f"scene_{i:02d}.mp4"
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps),
           "-i", "-", "-vf", f"fps={config()['video']['fps']},format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
           "-crf", "17", "-t", f"{duration:.3f}", str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for k in range(n):
        key = (k % 3, min(k, pop))
        if key not in cache:
            cache[key] = to_frame(layers[k % 3], bgrgb, (k + 1) / pop if k < pop else 1.0).tobytes()
        p.stdin.write(cache[key])
    p.stdin.close()
    if p.wait() != 0:
        raise RuntimeError(f"ffmpeg failed for day {day} scene {i}")
    return i, bbox


def build(day, only=None):
    s = load_script(day)
    t = load_timing(day)
    (day_dir(day) / "scenes").mkdir(exist_ok=True)
    jobs = [(day, i, sc, t["scenes"][i]["end"] - t["scenes"][i]["start"]) for i, sc in enumerate(s["scenes"])
            if only is None or i in only]
    with Pool(min(4, len(jobs))) as pool:
        res = dict(pool.map(render_clip, jobs))
    if only is None:
        manifest = [{"scene": i, "start": t["scenes"][i]["start"], "end": t["scenes"][i]["end"], "text_bbox": res[i]}
                    for i in range(len(jobs))]
        (day_dir(day) / "scenes.json").write_text(json.dumps(manifest, indent=1))
    print(f"day {day:02d} visuals: {len(jobs)} scene clips")


if __name__ == "__main__":
    build(int(sys.argv[1]))
