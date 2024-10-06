import pandas as pd

# Sample data for bus stops (replace with your actual data)
bus_stops_data = {
    'stop_name': [
        'Ernakulam North',  # Add more bus stop names
        'Ernakulam South',
        'MG Road',
        'Kochi Fort',
        'Vyttila',
        # ... Add more stop names as needed
    ],
    'latitude': [
        9.9652,  # Replace with actual latitude values
        9.9486,
        9.9826,
        9.9563,
        9.9753,
        # ... Add more latitude values as needed
    ],
    'longitude': [
        76.2861,  # Replace with actual longitude values
        76.2814,
        76.2995,
        76.2758,
        76.2846,
        # ... Add more longitude values as needed
    ]
}

# Create DataFrame and save to CSV
bus_stops_df = pd.DataFrame(bus_stops_data)
bus_stops_df.to_csv('bus_stops_kochi.csv', index=False)

print("Bus stops CSV file has been created: bus_stops_kochi.csv")
