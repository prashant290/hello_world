"""Recreate the channel brain logo (assets/logo.png, 800x800, transparent bg).
Replace assets/logo.png with your original file at any time -- the pipeline just resizes it."""
from PIL import Image, ImageDraw
from common import *

S, N = 4, 800
img = Image.new("RGBA", (N * S, N * S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
NAVY, SAGE, GOLD = (31, 45, 61, 255), (200, 217, 212, 255), (224, 164, 88, 255)
P = lambda p: (p[0] * S, p[1] * S)


def chaikin(pts, n=3, closed=False):
    for _ in range(n):
        out = []
        for a, b in zip(pts, pts[1:] + ([pts[0]] if closed else [])):
            out += [(0.75 * a[0] + 0.25 * b[0], 0.75 * a[1] + 0.25 * b[1]), (0.25 * a[0] + 0.75 * b[0], 0.25 * a[1] + 0.75 * b[1])]
        pts = out if closed else [pts[0]] + out + [pts[-1]]
    return pts


def stroke(pts, w=20, closed=False):
    pts = chaikin(pts, closed=closed)
    pts = pts + [pts[0]] if closed else pts
    q = [P(p) for p in pts]
    d.line(q, fill=NAVY, width=w * S, joint="curve")
    for p in ([q[0], q[-1]] if not closed else []):
        d.ellipse([p[0] - w * S / 2, p[1] - w * S / 2, p[0] + w * S / 2, p[1] + w * S / 2], fill=NAVY)


d.ellipse([100 * S, 100 * S, 700 * S, 700 * S], fill=SAGE)
outline = [(405, 215), (350, 205), (290, 215), (235, 262), (170, 285), (150, 340), (160, 420), (178, 440), (180, 480), (215, 508),
           (280, 498), (350, 520), (430, 505), (490, 527), (570, 492), (630, 497), (660, 440), (648, 385), (662, 335), (640, 285),
           (582, 248), (540, 208), (480, 195), (425, 205)]
d.polygon([P(p) for p in chaikin(outline, closed=True)], fill=SAGE)
stroke(outline, closed=True)
for s in ([(312, 245), (322, 280), (325, 305)], [(250, 322), (300, 325), (358, 308)],
          [(220, 400), (300, 392), (360, 405), (430, 392), (550, 392)], [(293, 457), (345, 450), (395, 445)],
          [(470, 445), (505, 440), (540, 436)], [(470, 270), (520, 268), (555, 282)], [(470, 325), (520, 335), (545, 350)],
          [(595, 320), (618, 350), (602, 385)], [(405, 225), (402, 290), (420, 365)],
          [(528, 497), (548, 530), (535, 585)], [(545, 520), (585, 540), (630, 498)]):
    stroke(s)
r = 15 * S
d.ellipse([406 * S - r, 296 * S - r, 406 * S + r, 296 * S + r], fill=GOLD)
out = ASSETS / "logo.png"
img.resize((N, N), Image.LANCZOS).save(out)
print("wrote", out)
