# What a county can publish

A precinct lookup answers an address with its precinct, and the districts that precinct votes in. It works like this:

1. **The county publishes** its precinct map, its addresses and its district list.
2. **Street ranges are built** from them: small files, one for each zipcode, on any web host.
3. **Anyone can use them:** the [California Precinct Lookup](https://lookup.usegis.org/), the
   [precinct-lookup](https://www.npmjs.com/package/precinct-lookup) library in any app, or a county's own lookup page.

The better the county's data, the better every lookup built on it. Each page below lists the ways a county can provide
it, best first, so a county can see where it is today and what would help its voters most.

- [Precinct shapefiles](precincts): the precinct lines, and how current they are.
- [Address data](addresses): which house numbers are where.
- [District lists](districts): the districts each precinct is in.
- [Street ranges](ranges): the small files a lookup makes from them, with no database.
