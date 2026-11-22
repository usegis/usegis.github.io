"""Draws lookup.svg: a precinct on city blocks in perspective. Usage: python3 bin/lookup_svg.py > lookup.svg"""

# Map coordinates are in blocks: u to the right, v up, origin at the P's bottom-left intersection.
# That corner stays square on screen; side streets lean toward UP_VP, cross streets fan out from LEFT_VP.
STREET = 10 / 150    # street width as a share of a block
BLOCK_W = 180        # screen width of the block at the corner
BLOCK_H = 90         # screen height of the block at the corner
UP_VP = 360          # how far above the corner the side streets meet
LEFT_VP = 2400       # how far left of the corner the cross streets meet

A = -BLOCK_W / LEFT_VP
B = BLOCK_H / UP_VP


def screen(u, v):
    # the plane-to-screen homography: u heads away from LEFT_VP, v toward UP_VP
    w = 1 + A * u + B * v
    return (A * u * -LEFT_VP) / w, (B * v * -UP_VP) / w, w


def path(pts):
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'Z'


# The precinct, a P for precinct: two blocks wide, three tall, every corner on an intersection, the bowl closed by
# a diagonal across one block.
CELLS = [(0, 0), (0, 3), (2, 3), (2, 2), (1, 1), (1, 0)]
SHAPE = [screen(u, v)[:2] for u, v in CELLS]

# Frame the P with room around it.
xs, ys = [p[0] for p in SHAPE], [p[1] for p in SHAPE]
SIDE = max(max(xs) - min(xs), max(ys) - min(ys)) * 1.55
X0 = (min(xs) + max(xs) - SIDE) / 2
Y0 = (min(ys) + max(ys) - SIDE) / 2


def visible(pts):
    px, py = [p[0] for p in pts], [p[1] for p in pts]
    return max(px) > X0 and min(px) < X0 + SIDE and max(py) > Y0 and min(py) < Y0 + SIDE


blocks = []
h = STREET / 2
for v in range(-10, 40):
    for u in range(-10, 30):
        corners = [screen(u + h, v + h), screen(u + 1 - h, v + h), screen(u + 1 - h, v + 1 - h), screen(u + h, v + 1 - h)]
        if min(c[2] for c in corners) > 0.05:
            pts = [c[:2] for c in corners]
            if visible(pts):
                blocks.append(path(pts))

print(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0:.1f} {Y0:.1f} {SIDE:.1f} {SIDE:.1f}">
  <rect x="{X0:.1f}" y="{Y0:.1f}" width="{SIDE:.1f}" height="{SIDE:.1f}" fill="#fff"/>
  <path d="{''.join(blocks)}" fill="#f0efeb"/>
  <path d="{path(SHAPE)}" fill="#e7c357" fill-opacity="0.6" stroke="#7a7a7a" stroke-width="{SIDE / 150:.1f}" stroke-linejoin="round"/>
</svg>''')
