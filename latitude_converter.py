import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_coordinates(address):
    api_key=os.getenv('api_key')
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": f'{api_key}'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            location = results[0].get('geometry').get('location')
            return location['lat'], location['lng']
        else:
            return None, None
    else:
        return None, None

# Example usage
#api_key = "YOUR_API_KEY"
#address = "1600 Amphitheatre Parkway, Mountain View, CA"
address = "red fort"
lat, lng = get_coordinates(address)
print(f"Latitude: {lat}, Longitude: {lng}")
