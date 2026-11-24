# Address data

A precinct lookup needs to know which house numbers are in which precinct. Whatever a county publishes is turned into
**street ranges**: for each street in a zipcode, runs of house numbers and their precinct. The better the addresses,
the better the ranges, best first.

## 1. Street data

Each address with its precinct, from the elections office's own system, after each redraw.

**How it's used:** grouped into street ranges, each keeping the county's precinct.

**Result:** the county's own answer for every address.

Who: Elections

## 2. Address points

Each address at its location: house number, street and zipcode.

**How it's used:** each point placed on the [precinct map](precincts), then grouped into street ranges.

**Result:** right wherever the precinct map is current.

Who: GIS or addressing

## 3. Parcels

Parcel shapes with each parcel's site address and parcel number.

**How it's used:** each parcel's center stands in for an address point. Only the site address and parcel number are
read, never owner names or mailing addresses.

**Result:** nearly as good as address points, missing homes with no site address on file.

Who: Assessor or GIS

## 4. Census ranges

Census TIGER's ranges of possible house numbers on each side of each block.

**How it's used:** each side placed on the precinct map.

**Result:** fine in towns, but often missing or wrong for rural addresses.

Who: Census, when a county publishes no addresses

## The result

The street ranges and precinct outlines are small files, one for each zipcode. The
[California Precinct Lookup](https://lookup.usegis.org/) reads them in the browser, and the
[precinct-lookup](https://www.npmjs.com/package/precinct-lookup) library does the same in any app. A typed address
never leaves the browser, and no voter data is used.

See also: [Precinct shapefiles](precincts), [District lists](districts)
