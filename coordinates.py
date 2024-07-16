from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Example usage
#address = "1600 Amphitheatre Parkway, Mountain View, CA"
address = "red fort"
lat, lng = get_coordinates(address)
print(f"Latitude: {lat}, Longitude: {lng}")
