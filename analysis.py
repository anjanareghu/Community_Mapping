import pandas as pd

# Load the bus stops data
bus_stops_df = pd.read_csv('bus_stops_kochi.csv')

# Load the community locations data
community_df = pd.read_csv('community_locations_kochi.csv')

print(bus_stops_df)  # This should now display the bus stops data
print(community_df)  # This should display the community locations
