import folium
import pandas

#create HTML file with map.save("Map1.html")
#import folium to support open source map 
#Folium converts the python code into simple javascript and css code to render map on screen
#layers on map come from overstreet map service - give you layer that folium serves

data = pandas.read_csv("Volcanoes.txt")
# create lists from csv data to loop through later
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# define a color producing function to use later for the circle markers
def color_producer(elevation):
    if elevation < 1000:
        return 'pink'
    elif 1000 <= elevation < 3000:
        return 'red'
    else:
        return 'green'

# instatiate a folium map with an initial location and zoom level
map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles = "Stamen Terrain")

#fgv = feature group volcano
#fgp = feature group population

# create feature groups to add to map later
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

# looping through volcanos data and storing references for lat, long, and elevation
# zip three separate lists together and use that combined list for looping
# add circle marker inside loop with lat/long coordinates
# feed elevation into color_producer function which returns a cooresponding color value
# these markers are added to the volcanoes feature group
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ "m", 
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))
 
# add geo json data from world.json file with style lambda function to set fillColor based on POP2005 column
# this gets added to the population feature group
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# adding the two feature groups to the map
map.add_child(fgv)
map.add_child(fgp)
# add the layer controls to the map
map.add_child(folium.LayerControl())

# save the to the Map.html file
map.save("Map.html")
