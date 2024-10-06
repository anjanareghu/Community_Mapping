import folium
import pandas as pd

# Load the bus stops and community locations data
bus_stops_df = pd.read_csv('bus_stops_kochi.csv')
community_df = pd.read_csv('community_locations_kochi.csv')

# Create a base map centered around Kochi
kochi_map = folium.Map(location=[9.966, 76.281], zoom_start=13)

# Add bus stops to the map
for _, row in bus_stops_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['stop_name'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(kochi_map)

# Add community locations to the map
for _, row in community_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['location_name'],
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(kochi_map)

# Save the map to an HTML file
kochi_map.save('kochi_bus_stops_community_map.html')

print("Map has been created and saved as: kochi_bus_stops_community_map.html")
