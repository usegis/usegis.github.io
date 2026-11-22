"""Draws lookup.svg: a precinct on city blocks in perspective. Usage: python3 bin/lookup_svg.py > lookup.svg"""
import math

# A floor of city blocks seen from above, running to a horizon near the top.
W = H = 512
HORIZON = 56
CAM = 430.0
F = 520.0
Z0 = 300.0
NEAR = 60.0
TILT = math.radians(-8)
BLOCK = 150          # street centerline spacing
STREET = 10          # street width
OX = 40              # where the street grid starts across
CENTER_Y = 0.64      # where the precinct's middle sits, as a share of the height
SHIFT = [0.0, 0.0]   # how far the floor slides across and away, to center the precinct
ZOOM = 1.7           # how far the frame closes in on the precinct


def to_ground(u, v):
    # map coordinates (u right, v down toward the camera), turned by TILT
    c, s = math.cos(TILT), math.sin(TILT)
    return u * c - v * s - SHIFT[0], -(u * s + v * c) - SHIFT[1]


def proj(x, z):
    Z = Z0 + z
    return W / 2 + F * x / Z, HORIZON + F * CAM / Z


def clip_near(pts):
    # keep the part of a ground polygon in front of the camera
    lim = NEAR - Z0
    out = []
    for i, (x1, z1) in enumerate(pts):
        x2, z2 = pts[(i + 1) % len(pts)]
        if z1 >= lim:
            out.append((x1, z1))
        if (z1 >= lim) != (z2 >= lim):
            t = (lim - z1) / (z2 - z1)
            out.append((x1 + (x2 - x1) * t, lim))
    return out


def screen(map_pts):
    ground = clip_near([to_ground(u, v) for u, v in map_pts])
    return [proj(x, z) for x, z in ground]


def path(pts):
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'Z'


def visible(pts):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    big = max(ys) - min(ys) > 1.2
    return pts and big and max(xs) > 0 and min(xs) < W and max(ys) > H * 0.14 and min(ys) < H


# The precinct, a P for precinct: two blocks wide, three deep, every corner on an intersection, the bowl closed by
# a diagonal across one block.
C, R = -1, -4                   # top-left block of the precinct
CELLS = [(0, 0), (2, 0), (2, 1), (1, 2), (1, 3), (0, 3)]
SHAPE = [(OX + (C + i) * BLOCK, (R + j) * BLOCK) for i, j in CELLS]

# Slide the floor under the camera until the precinct's outline is centered in the frame.
for _ in range(40):
    pts = screen(SHAPE)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    Zc = F * CAM / (cy - HORIZON)
    SHIFT[0] += 0.5 * (cx - W / 2) * Zc / F
    SHIFT[1] -= 0.5 * (cy - H * CENTER_Y) * Zc * Zc / (F * CAM)

blocks = []
half = STREET / 2
for row in range(-160, 12):
    for col in range(-80, 80):
        u0, v0 = OX + col * BLOCK + half, row * BLOCK + half
        u1, v1 = u0 + BLOCK - STREET, v0 + BLOCK - STREET
        pts = screen([(u0, v0), (u1, v0), (u1, v1), (u0, v1)])
        if len(pts) >= 3 and visible(pts):
            blocks.append(path(pts))

SIDE = W / ZOOM
FRAME = f'{(W - SIDE) / 2:.1f} {H * CENTER_Y - SIDE / 2:.1f} {SIDE:.1f} {SIDE:.1f}'

print(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{FRAME}">
  <defs>
    <linearGradient id="haze" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff"/>
      <stop offset="0.14" stop-color="#fff"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="frame"><rect width="{W}" height="{H}"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="#fff"/>
    <path d="{''.join(blocks)}" fill="#f0efeb"/>
    <path d="{path(screen(SHAPE))}" fill="#e7c357" fill-opacity="0.6" stroke="#7a7a7a" stroke-width="2" stroke-linejoin="round"/>
    <rect width="{W}" height="{H}" fill="url(#haze)"/>
  </g>
</svg>''')
