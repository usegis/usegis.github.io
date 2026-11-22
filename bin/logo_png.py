"""Draws the logo's sheets alone (the bug) as a square PNG. Usage: python3 bin/logo_png.py usegis.svg out.png [size]"""
import re
import sys
from PIL import Image, ImageDraw

src, out = sys.argv[1:3]
N = int(sys.argv[3]) if len(sys.argv) > 3 else 400
K = 8          # supersampling
PAD = 0.065    # margin to the sheet lines, as a share of the side (the crop Woodie chose)

sheets = []
for d, color, width in re.findall(r'<path d="([ML0-9. Z]+)" fill="none" stroke="(#[0-9a-f]+)" stroke-width="([0-9.]+)"', open(src).read()):
    pts = [tuple(map(float, p.split())) for p in re.findall(r'[\d.]+ [\d.]+', d)]
    sheets.append((pts + [pts[0]] if d.strip().endswith('Z') else pts, color, float(width)))

xs = [x for pts, _, w in sheets for x, _ in pts]
ys = [y for pts, _, w in sheets for _, y in pts]
side = max(max(xs) - min(xs), max(ys) - min(ys))
s = N * K * (1 - 2 * PAD) / side
ox = (N * K - (max(xs) - min(xs)) * s) / 2 - min(xs) * s
oy = (N * K - (max(ys) - min(ys)) * s) / 2 - min(ys) * s

img = Image.new('RGB', (N * K, N * K), 'white')
draw = ImageDraw.Draw(img)
for pts, color, width in sheets:
    draw.line([(x * s + ox, y * s + oy) for x, y in pts], fill=color, width=round(width * s), joint='curve')
img.resize((N, N), Image.LANCZOS).save(out)
