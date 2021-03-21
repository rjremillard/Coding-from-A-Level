import os
import folium
import json

LAT = -36.852095
LONG = 174.7631803

MARKERS = [
	{"location": (-36.8836944, 174.7586604), "popup": "<strong>Mount Eden</strong>",
		"icon": folium.Icon(icon="glyphicon-picture", color="green")},
	{"location": (-36.8877, 174.7529), "popup": "<strong>One Tree Hill</strong>",
		"icon": folium.Icon(icon="glyphicon-picture")},
	{"location": (-36.88413619995117, 174.71563720703125), "popup": "<strong>Mount Albert</strong>",
		"icon": folium.Icon(icon="glyphicon-picture")}
]

mapObj = folium.Map((LAT, LONG), zoom_start=12)

for mark in MARKERS:
	folium.Marker(**mark).add_to(mapObj)

folium.CircleMarker((-36.8630714, 174.7207656), tooltip="<strong>Auckland Zoo</strong>", fill=True, fill_color="blue").add_to(mapObj)

with open("polygon.json", "r") as f:
	coordinates = json.load(f)

folium.GeoJson(coordinates, popup="<strong>Area</strong>").add_to(mapObj)

mapObj.save("Auckland.html")
