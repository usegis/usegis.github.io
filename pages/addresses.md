# Address data

A precinct lookup needs to match house numbers to a precinct.
Public address information is turned into [street ranges](ranges)
for each street in a zipcode, with runs of house numbers with their precinct.
Address data comes four ways.

## 1. Street data

Each address with its precinct, from the elections office's own system, after each redraw.

**Method:** grouped into street ranges, each keeping the county's precinct.

**Result:** the most accurate answer for every address.

Publisher: Elections

## 2. Address points

Each address at its location: house number, street and zipcode.

**Method:** each point placed on the [precinct map](precincts),
then grouped into street ranges.

**Result:** right wherever the precinct map is current.

Publisher: GIS, Planning, Public Works or 911 addressing

## 3. Parcels

Parcel shapes, each with its site address.

**Method:** each parcel's center becomes an address point.
Only the site address and parcel number are used, never owner names.

**Result:** nearly as good as address points, missing homes with no site address on file.

Publisher: Assessor, GIS, IT or Public Works

## 4. Census ranges

Census TIGER's ranges of possible house numbers on each side of each block.

**Method:** each side placed on the precinct map.

**Result:** fine in towns, but often missing or wrong for rural addresses.

Publisher: [Census TIGER](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) (only where a county publishes no addresses)

## The result

The street ranges and precinct outlines are small files, one for each zipcode. The
[California Precinct Lookup](https://lookup.usegis.org/) reads them in the browser, and the
[precinct-lookup](https://www.npmjs.com/package/precinct-lookup) library does the same
in any app. A typed address never leaves the browser, and no voter data is used.

[Back](./)
