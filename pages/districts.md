# District lists

A precinct lookup can tell a voter more than a precinct number: which districts that precinct is in, from Congress
down to school, fire and water. Only the county knows the local ones. A district list ties each precinct to its
districts, using the same precinct numbers as the [precinct map](precincts). Counties keep it three ways, best first.

## 1. District-by-precinct file

Each precinct with every district it's in, exported from the election system after each redraw. Many county systems
already produce one, such as DFM's district precinct file (PDMJ001).

**How it's used:** read as it is; each district is named once and each precinct lists its districts.

**Result:** every district on the ballot, exactly as Elections assigns them.

Source: Elections

## 2. Precinct map with district columns

The precinct map itself, with a column for each kind of district: congressional, senate, assembly, supervisor and so on.

**How it's used:** each precinct's columns become its list of districts.

**Result:** right for the districts it has columns for, often only the larger ones.

Source: Elections or GIS

## 3. District maps

A separate map for each kind of district, with no list by precinct.

**How it's used:** each precinct is laid over the district maps and takes the district that holds it.

**Result:** right where the district lines follow precinct lines, as they usually do; check precincts along the edges.

Source: GIS

## The result

One small file for the county: the districts, named once, and each precinct's list of them.

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
