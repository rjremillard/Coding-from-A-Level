import folium
import pandas as pd
import os

states = os.path.join('us-states.json')
unemployment_data = os.path.join('us_unemployment.csv')
state_data = pd.read_csv(unemployment_data)

m = folium.Map(location=[48, -102], zoom_start=3)

# https://github.com/python-visualization/folium/blob/v0.2.0/folium/utilities.py#L104
# see also: https://python-visualization.github.io/folium/quickstart.html
# see also https://handsondataviz.org/design-choropleth.html

folium.Choropleth(
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment rate %'
    ).add_to(m)
folium.LayerControl().add_to(m)

m.save('usmap.html')
