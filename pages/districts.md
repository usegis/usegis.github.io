# District lists

A precinct lookup can tell a voter more than a precinct number: which districts that precinct is in, from Congress
down to school, fire and water. Only the county knows the local ones. A district list ties each precinct to its
districts, using the same precinct numbers as the [precinct map](precincts). Counties keep it three ways, best first.

## 1. District-by-precinct file

The election system exports each precinct with every district it's in after each redraw. Many county systems already
produce this file, such as DFM's district precinct file (PDMJ001).

**Method:** The file is read as it is; each district is named once, and each precinct lists its districts.

**Result:** Every district on the ballot comes out exactly as Elections assigns it.

Publisher: Elections

## 2. Precinct map with district columns

The precinct map itself has a column for each kind of district: congressional, senate, assembly, supervisor and so on.

**Method:** Each precinct's columns become its list of districts.

**Result:** The lists are right for the districts with columns, often only the larger ones.

Publisher: Elections or GIS

## 3. District maps

Each kind of district has its own map, with no list by precinct.

**Method:** Each precinct is laid over the district maps and takes the district that holds it.

**Result:** The answers are right where district lines follow precinct lines, as they usually do; precincts along the
edges need a check.

Publisher: GIS

## The result

The result is one small file for the county: the districts, named once, and each precinct's list of them.

```
{
  "names": {
    "D1": ["United States Congress", "7th Congressional District"],
    "D4": ["Supervisorial district", "1st Supervisorial District"]
  },
  "precincts": {
    "1037501": ["D1", "D4"]
  }
}
```

With the [address data](addresses), a lookup can answer any address with its precinct and every district it votes in.

[Back](./)
