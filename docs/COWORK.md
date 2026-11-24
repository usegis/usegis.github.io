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
- `precincts.html` ("Precinct shapefiles") and `addresses.html` ("Address data") (2026-11-23): reference pages for county Elections and GIS staff, at
  usegis.org/precincts and usegis.org/addresses. Each names its levels, best first, as cards with anchors an email can link
  (`#live-layer`, `#download`, `#on-request`, `#swdb`; `#street-data`, `#address-points`, `#parcels`, `#census-ranges`), so
  an email can say "today you have this, we hope you'll consider that." Nothing county-specific here (Woodie: specifics go in
  the GitHub docs). Their styles follow the home page's in `style.css`. Links between them omit `.html`, which Pages serves.
- `privacy.html`: no cookies or analytics; GitHub Pages may log requests. It covers this site only (Woodie,
  2026-11-21: keep focus on the site, not other sites).
- `usegis.svg`: Woodie's logo (layered map sheets over "UseGIS"). Since 2026-11-21 the sheets are open outlines,
  each line stopping where the sheet above covers it, so one file works on light and dark pages.
- `favicon.ico`: Woodie's 32x32 layered sheets.
- `CNAME`: `usegis.org`.

## Publishing

GitHub Pages from `main` at the root, custom domain usegis.org, HTTPS enforced. A push to `main` is live within a
minute or two; GitHub caches pages for up to 10 minutes. Woodie pushes, or says yes first.

DNS at Network Solutions: A `@` 185.199.108.153, .109, .110 and .111; CNAME `www` usegis.github.io (GitHub redirects
www to usegis.org); CNAME `lookup` usegis.github.io for the lookup's repo. usegis.org is verified for Pages in the
`usegis` org.

## Copy

Fewest words that stay accurate; follow Woodie's wording. The page stays about UseGIS: links only to its own projects (the
lookup and the npm package).
