import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])

map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    map.add_child(folium.Marker(location=[lt, ln], popup="Hi, You are here!", icon=folium.Icon(color='pink')))
map.add_child(fg)


map.save("Map1.html")
