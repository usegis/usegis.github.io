# Lookup tools

With all required information available as public data, an address-to-precinct lookup is easy
and advantageous with [street ranges](ranges). It needs no database, server or geocoder.
Only static files need to be published, and a typed address never leaves the browser. The
[sample Lookup app](https://lookup.usegis.org/) and the associated
[open source library](https://www.npmjs.com/package/precinct-lookup) both read them.

Street ranges are only as good as the county data behind them. The [precinct shapefiles](precincts) say where each
precinct's lines are and how current they are, and the [address data](addresses) says which house numbers are where.
The closer both are to the county's own records, the more voters get the right answer.

With those in place, a county can now easily publish its own address-to-district page: add its
[district list](districts), and each address shows every district it votes in, from Congress down to special districts.
