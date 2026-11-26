# Address data

A precinct lookup needs to match house numbers to a precinct.
Public address information is turned into [street ranges](ranges),
which give each street in a zipcode runs of house numbers with their precinct.
Address data comes four ways.

## 1. Street data

The elections office exports each address with its precinct from its own system after each redraw.

**Method:** The addresses are grouped into street ranges, each keeping the county's precinct.

**Result:** Every address gets the most accurate answer.

Publisher: Elections

## 2. Address points

Each address point marks one address at its location, with its house number, street and zipcode.

**Method:** Each point is placed on the [precinct map](precincts),
then the points are grouped into street ranges.

**Result:** The answers are right wherever the precinct map is current.

Publisher: GIS, Planning, Public Works or 911 addressing

## 3. Parcels

Each parcel shape comes with its site address.

**Method:** Each parcel's center becomes an address point, which is placed
on the [precinct map](precincts) and grouped into street ranges.

**Result:** The answers are nearly as good as address points, but homes with no site address on file are missing.

Publisher: Assessor, GIS, IT or Public Works

## 4. Census ranges

Census TIGER gives ranges of possible house numbers on each side of each block.

**Method:** Each side is placed on the precinct map.

**Result:** The ranges work in towns but are often missing or wrong for rural addresses.

Publisher: [Census TIGER](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) (only where a county publishes no addresses)

## The result

The street ranges and precinct outlines are small files, one for each zipcode. The
[California Precinct Lookup](https://lookup.usegis.org/) reads them in the browser, and the
[precinct-lookup](https://www.npmjs.com/package/precinct-lookup) library does the same
in any app. A typed address never leaves the browser, and no voter data is used.

[Back](./)
