# Address to Precinct

[Street ranges](ranges) answer an address with its precinct from small files, one for each zipcode. No database, no
server and no geocoder: any web host can serve them, and a typed address never leaves the browser. The
[California Precinct Lookup](https://lookup.usegis.org/) and the
[precinct-lookup](https://www.npmjs.com/package/precinct-lookup) library both read them.

Street ranges are only as good as the county data behind them. The [precinct shapefiles](precincts) say where each
precinct's lines are and how current they are, and the [address data](addresses) says which house numbers are where.
The closer both are to the county's own records, the more voters get the right answer.

With those in place, a county can now easily publish its own address-to-district page: add its
[district list](districts), and each address shows every district it votes in, from Congress down to school and fire.
