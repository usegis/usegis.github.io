# Address data

Under the California Public Records Act, the GIS data a county keeps,
such as its parcel map, is a public record, and the county must provide it
on request and cannot require licensing fees or impose distribution
restrictions. A precinct lookup matches house numbers to a precinct
by turning address data into [street ranges](ranges).
Address data comes four ways.

## 1. Street data

Most California counties' election systems already run this report: the street
index, `SGMJ001`, also called the street guide, street file or street data
extract. It lists each address with its house number, street, zipcode and
precinct, and no voter information.

Many counties sell it on request, for $19 to $45 a copy. Post it free instead, on
the county's GIS server or website, as a table or a download, and replace it after
each redraw: one posting saves answering each request. Choose each address over
address ranges where the report offers both.

The addresses are grouped into street ranges, each keeping the county's
precinct. Every address gets the most accurate answer.

Publisher: Elections

## 2. Address points

Each address point marks one address at its location, with its house number,
street and zipcode. Each point is placed on the [precinct map](precincts),
then the points are grouped into street ranges.  The answers are right wherever
the precinct map is current.

Publisher: GIS, Planning, Public Works or 911 addressing

## 3. Parcels

Each parcel shape comes with its site address. Each parcel's center becomes
an address point, which is placed on the [precinct map](precincts) and grouped
into street ranges. The answers are nearly as good as address points,
but homes with no site address on file are missing.

Publisher: Assessor, GIS, IT or Public Works

## 4. Census ranges

Census TIGER gives ranges of possible house numbers on each side of each block.
Each side is placed on the precinct map. The ranges work in towns but are often
missing or wrong for rural addresses.

Publisher: Census TIGER (only where a county publishes no addresses)

## The result

Whatever the source, the result is the same: [street ranges](ranges), one small file for each zipcode. The
[California Precinct Lookup](https://lookup.usegis.org/) and the
[precinct-lookup](https://www.npmjs.com/package/precinct-lookup) library both read them.

[Back](./)
