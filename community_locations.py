import pandas as pd

# Example data for community locations - replace these with your actual data
community_data = {
    'location_name': [
        'Sacred Heart CMI Public School',  
        'Amrita Hospital, Kochi',
        'Subhash Bose Park',
        'Indira Priyadarsini Childrens Park',
        'Fort Vypin Beach Park',
        'Aster Medcity',
        'Medical Trust Hospital'
        # Add more locations as needed
    ],
    'type': [
        'School',  
        'Hospital',
        'Park',
        'Park',
        'Park',
        'Hospital',
        'Hospital',
        # Corresponding types for each location
    ],
    'latitude': [
        9.94349,  
        10.0448,
        9.97281,
        9.97426,
        9.97397,
        10.04510,
        9.96434,
        # Add more latitude values as needed
    ],
    'longitude': [
        76.29914,  
        76.29501,
        76.27881,
        76.27826,
        76.24260,
        76.27818,
        76.28779,
        # Add more longitude values as needed
    ],
    'address': [
        'Pandit Karuppan Rd, Thevara, Kochi, Ernakulam, Kerala 682013',  
        'Ponekkara Rd, P. O, Edappally, Kochi, Ernakulam, Kerala 682041',
        'Park Ave, Marine Drive, Kochi, Ernakulam, Kerala 682011',
        'Marine Drive, Kochi, Ernakulam, Kerala 682011',
        'X6CR+XRX, Church Lane Number 4, Fort Vypin, Vypin, Kochi, Kerala 682508',
        'Kuttisahib Road Cheranelloor, South Chittoor, Kochi, Kerala 682027',
        'Mahatma Gandhi Rd, Pallimukku, Kochi, Ernakulam, Kerala 682016',  # Added missing comma
        # Add more addresses as needed
    ]
}

# Create DataFrame and save to CSV
community_df = pd.DataFrame(community_data)
community_df.to_csv('community_locations_kochi.csv', index=False)

print("Community locations CSV file has been created: community_locations_kochi.csv")
