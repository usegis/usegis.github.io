# Precinct shapefiles

A precinct map is a set of shapes, one for each precinct, each with its precinct number. Counties keep it as a
shapefile or GIS layer and redraw it before elections. A lookup can get it four ways, best first.

## 1. Live layer

The precinct map on the county's GIS server, such as ArcGIS, updated after each redraw. A lookup always reads the
current lines, and no one has to send a file.

Who: Elections, published by GIS

## 2. Download

A dated file, a shapefile or GeoJSON, on the county's website or GIS hub. Current until the next redraw, when someone
has to post the new one.

Who: Elections or GIS

## 3. On request

Emailed by the elections office, free under Elections Code §12263. Current when sent, but every requester has to ask,
after every redraw.

Who: Elections

## 4. Statewide Database

The Statewide Database (SWDB) publishes every county's precinct map as GeoJSON, months after each election. Useful by
itself, but any redraw since then is missing.

Who: SWDB, from what counties send it

## What makes a precinct map useful

Precinct numbers as the voter file writes them (registration precincts, not only consolidated voting precincts), and
the date or election the lines are for.

See also: [Address data](addresses), [District lists](districts), [Street ranges](ranges)
