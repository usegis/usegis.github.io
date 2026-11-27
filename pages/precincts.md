# Precinct shapefiles

Under Elections Code §12263, every California county elections office must provide its precinct map on request, at no
charge. A precinct map is a set of shapes, one for each precinct, each with its precinct number. Counties keep it as a
shapefile or GIS layer and redraw it before elections. A lookup turns it into a small GeoJSON file of precinct
outlines for each zipcode. Precinct maps are available four ways.

## 1. Live layer

The county publishes its precinct map on a GIS server, such as ArcGIS, and updates it after each redraw. A lookup
always reads the current lines, and no one has to send a file.

Publisher: GIS, from Elections

## 2. Download

The county posts a dated file, a shapefile or GeoJSON, on its website or GIS hub. The file is current until the next
redraw, when someone has to post a new one.

Publisher: Elections or GIS

## 3. On request

The elections office emails the file under §12263, and some counties require a signed form first. The file is
current when sent, but every requester has to ask again after every redraw.

Publisher: Elections

## 4. Statewide Database

The Statewide Database (SWDB) publishes every county's precinct map as GeoJSON, months after each election. The map is
useful by itself, but it misses any redraw since then.

Publisher: SWDB, from what counties send it

## What makes a precinct map useful

A useful precinct map has precinct numbers as the voter file writes them (registration precincts, not only
consolidated voting precincts), and the date or election the lines are for.

[Back](./)
