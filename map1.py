import folium
import pandas

#create HTML file with map.save("Map1.html")
#import folium to support open source map 
#Folium converts the python code into simple javascript and css code to render map on screen
#layers on map come from overstreet map service - give you layer that folium serves

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'pink'
    elif 1000 <= elevation < 3000:
        return 'red'
    else:
        return 'green'

map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles = "Stamen Terrain")
#map object that takes in lat and long cordinates on where to start on the map
#everything will spin around the folium map object 

#fgv = feature group volcano
#fgp = feature group population

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ "m", 
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))

#used python for loop to create multiple markers on the map  


fgp = folium.FeatureGroup(name="Population")
  
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#children of map pointing to folium markers which is a built in feature of the folium library
#adds pop ups and location if you pass in location parameter in the function



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
