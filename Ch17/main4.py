import folium
import os

map = folium.Map(location=[37, 127], zoom_start=7)

marker = folium.Marker(location=[37.591427446, 127.028874720],
                       popup='고려대학교',
                       icon=folium.Icon(color='red'))

marker.add_to(map)

map_path = os.path.join(os.path.dirname(__file__), 'koreauniv_map.html')
map.save(map_path)
