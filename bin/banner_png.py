"""Draws a cover from the site's grid: a floor fading to a horizon. Usage: python3 bin/banner_png.py out.png [W H]"""
import sys
from PIL import Image, ImageDraw

# LinkedIn's cover (1128x191) by default; X's header is 1500 500. Drawn at 2x.
W, H = (int(sys.argv[2]) * 2, int(sys.argv[3]) * 2) if len(sys.argv) > 3 else (1128 * 2, 191 * 2)
K = 4                      # supersampling
TOP = -8                   # vanishing point, just above the top edge
SPACING = 96 * H / 382     # line spacing along the bottom edge, in step with the height
DEPTH = 0.25               # how fast the rows shrink toward the horizon
BLUE = (0x3d, 0x8c, 0xff)
ALPHA = 0.3                # line opacity at the bottom, fading to 0 at the top

w, h, top = W * K, H * K, TOP * K
lines = Image.new('L', (w, h), 0)
d = ImageDraw.Draw(lines)
cx = w / 2
for i in range(-200, 201):
    d.line([(cx, top), (cx + i * SPACING * K, h)], fill=255, width=2 * K)
k = 0
while True:
    y = top + (h - top) / (1 + DEPTH * k)
    if y - top < 6 * K:
        break
    d.line([(0, y), (w, y)], fill=255, width=2 * K)
    k += 1

fade = Image.linear_gradient('L').resize((w, h))
mask = Image.composite(lines, Image.new('L', (w, h), 0), fade).point(lambda v: int(v * ALPHA))
out = Image.new('RGB', (w, h), 'white')
out.paste(Image.new('RGB', (w, h), BLUE), mask=mask)
out.resize((W, H), Image.LANCZOS).save(sys.argv[1])
