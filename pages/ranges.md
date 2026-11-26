# Street ranges

A precinct lookup doesn't need a database, a server or a geocoder. Everything it needs fits in small static files,
one for each zipcode, that any web host can serve and any browser can read.

## One file for each zipcode

The file lists each street in the zipcode, with runs of house numbers and the precinct they're in. A run covers one side of the
street, so both ends are odd or both are even.

```
{
  "LAUREL ST": [
    [300, 998, "4144013"],
    [401, 999, "4144013"],
    [1000, 1198, "4144033"],
    [1001, 1399, "4144014"]
  ]
}
```

To look up 701 Laurel St in 94025: open `94025.json`, find `LAUREL ST`, and take the run that includes 701 on the
odd side, 401 to 999. The answer is precinct 44013 (the first two digits are the county).

## How they're made

The [address data](addresses) is placed on the [precinct map](precincts). House numbers next to each other on the same
side of a street, in the same precinct, become one run. Where the county has no address for a stretch, Census TIGER's
ranges fill in. Street names are written one way everywhere (`LAUREL ST`, never `Laurel Street`), and the lookup reads
a typed address the same way.

## Outlines

A second small file for each zipcode holds the outline of each precinct in it, so the lookup can show the precinct on a
map. The [district list](districts), one file for the county, adds the districts each precinct is in.

## Small enough to copy

Every street range in California is about 1.6 million runs in 2,059 zipcode files, about 12 MB compressed. A county's
files can sit on its own website. A typed address never leaves the browser, and no voter data is used.

[Back](./)
