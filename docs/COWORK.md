# usegis.github.io - working notes

The UseGIS home page at https://usegis.org/: the logo over two cards, the precinct lookup at
https://lookup.usegis.org/ (its own repo, `usegis/precinct-lookup`) and the `precinct-lookup` npm package. This repo is public, so these notes cover only
the site itself.

## Files

- `index.html`: the logo, then a card for each project (title and a line of copy
  beside an image; stacked on a phone), then the footer, "© 2026 UseGIS | privacy". Plain HTML and CSS, no build step.
- `lookup.svg`: the lookup card's image, drawn by `bin/lookup_svg.py` (`python3 bin/lookup_svg.py > lookup.svg`):
  a P-shaped precinct (P for precinct, from Woodie's sketch: two blocks wide and three deep, every corner on an intersection, the bowl closed by a diagonal across one block) on city blocks in two-point perspective
  (Woodie, 2026-11-21): the streets along the P's left side and base meet at a square corner, cross streets above the
  base rise to the right, and side streets lean in toward a point high above the corner, so the base row is widest. A low view from Woodie's sketch: base blocks twice as wide as tall, rows shrinking fast going up.
  The outline runs down street centerlines and the frame is fitted around the precinct. Perspective, not isometric, keeps it apart
  from ArcGIS's look. A precise print version from real streets is planned. The npm card shows `npm install precinct-lookup` and `npx precinct-lookup fetch 41` instead of an image (2026-11-21).
- `grid.svg`: the faint background grid, a flat drawing of a floor fading toward a horizon near the top, pinned
  behind the page. It's a still image on purpose: a 3D CSS grid (2026-11-21) made card hovers glitch.
- `linkedin/banner.png`: the UseGIS LinkedIn cover (1128x191 at 2x), the grid's blue floor fading to a horizon at
  the top, drawn by `bin/banner_png.py` (`python3 bin/banner_png.py linkedin/banner.png`, needs Pillow) (2026-11-22). `x/header.png`: the same floor for X's 1500x500 header
  (`python3 bin/banner_png.py x/header.png 1500 500`); the account is @UseGISorg, since @usegis belongs to UseGIS
  Limited in Exeter, England. `linkedin/logo.png`: the bug (the logo's three sheets, no wordmark) at 400x400 on white, cropped close (Woodie, 2026-11-22),
  drawn from `usegis.svg` by `bin/logo_png.py`.
- `pages/` (2026-11-23): reference pages for county Elections and GIS staff, under usegis.org/tools/ (Woodie, 2026-11-24: `tools`,
  not `data`). `index.md` is /tools/ ("Lookup tools"); `precincts.md` ("Precinct shapefiles"),
  `addresses.md` ("Address data"), `districts.md` ("District lists") and `ranges.md` ("Street ranges", the file format)
  are /tools/precincts and so on. Written in plain Markdown so anyone can edit them. Conventions: `## 1. Live layer` is a
  numbered level with the anchor `#live-layer`, so an email can say "today you have this, we hope you'll consider
  that"; each level has **Method:** and **Result:**, then a paragraph starting `Kept by: `, the small line naming the office that keeps the data (label shown; the older `Who: `/`Source: ` drop it) (Woodie, 2026-11-26); a last line `[Back](./)` returns to
  the /tools/ index (`See also: ` still works for other pages); other `##` headings are notes. `bin/build.mjs` (markdown-it) renders them through
  `pages/template.html` (root-relative paths) and leaves a redirect at each old address (/precincts first, then /data/precincts), keeping any `#level`. Nothing county-specific here (Woodie: specifics go in the GitHub docs).
  Linked as "tools" in the home page footer (2026-11-24).
- `privacy.html`: no cookies or analytics; GitHub Pages may log requests. It covers this site only (Woodie,
  2026-11-21: keep focus on the site, not other sites).
- `usegis.svg`: Woodie's logo (layered map sheets over "UseGIS"). Since 2026-11-21 the sheets are open outlines,
  each line stopping where the sheet above covers it, so one file works on light and dark pages.
- `favicon.ico`: Woodie's 32x32 layered sheets. `apple-touch-icon.png`: the bug at 180x180 for phone home screens and
  Chrome's shortcut tiles (`python3 bin/logo_png.py usegis.svg apple-touch-icon.png 180`) (2026-11-25).
- `CNAME`: `usegis.org`.

## Publishing

GitHub Pages through `.github/workflows/pages.yml` (2026-11-23): on a push to `main` it runs `npm ci` and `npm run build`,
which copies the static files and renders `pages/*.md` into `_site/` (gitignored), then deploys that in its own job.
Custom domain usegis.org, HTTPS enforced. Live within a minute or two; GitHub caches pages for up to 10 minutes. Woodie
pushes, or says yes first. No local preview needed for the Markdown pages.

DNS at Network Solutions: A `@` 185.199.108.153, .109, .110 and .111; CNAME `www` usegis.github.io (GitHub redirects
www to usegis.org); CNAME `lookup` usegis.github.io for the lookup's repo. usegis.org is verified for Pages in the
`usegis` org.

## Copy

Fewest words that stay accurate; follow Woodie's wording. The page stays about UseGIS: links only to its own projects (the
lookup and the npm package).
