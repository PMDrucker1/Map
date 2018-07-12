import folium

map = folium.Map(location=[42.5, -74], zoom_start=6, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[42.65, -73.75], popup="518!!!", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

