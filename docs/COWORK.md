# usegis.github.io - working notes

The UseGIS home page at https://usegis.org/: the logo over two cards, the precinct lookup at
https://lookup.usegis.org/ (its own repo, `usegis/precinct-lookup`) and the `precinct-lookup` npm package. This repo is public, so these notes cover only
the site itself.

## Files

- `index.html`: the logo (`usegis-dark.svg` in dark mode), then a card for each project (title and a line of copy
  beside an image; stacked on a phone), then the footer, "© 2026 UseGIS | privacy". Plain HTML and CSS, no build step.
- `lookup.jpg`: the lookup card's image, a 360px square from precinct-lookup's `docs/41-46126.png` (Redwood City City
  Hall). The npm card shows `npm install precinct-lookup` instead of an image.
- `privacy.html`: no cookies or analytics; GitHub Pages may log requests. It covers this site only (Woodie,
  2026-11-21: keep focus on the site, not other sites).
- `usegis.svg`: Woodie's logo (layered map sheets over "UseGIS"), from his Illustrator export, with the viewBox
  cropped to the artwork. `usegis-dark.svg` is the same with the sheets filled #14161c and lighter text colors.
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
