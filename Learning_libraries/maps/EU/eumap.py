import requests
import folium

# Get data
url = "https://gisco-services.ec.europa.eu/distribution/v2/countries/geojson/CNTR_BN_01M_2020_3035_INLAND.geojson"
data = requests.get(url).json()

# Make map
m = folium.Map(location=[48, 11], zoom_start=3)
folium.GeoJson(data).add_to(m)

# Save map
m.save("eumap.html")
