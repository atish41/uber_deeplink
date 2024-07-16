import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('api_key')
place="Burj Khalifa"
lat=25.2567
long=55.3643

def placetocoord(place, lat, long):

  autocomplete_url=f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={place}&origin={lat},{long}&key={api_key}"

  autocomplete_response = requests.get(autocomplete_url).json()

  if autocomplete_response["status"] == "OK" and autocomplete_response["predictions"]:
      place_id = autocomplete_response["predictions"][0]["place_id"]
      dist=autocomplete_response["predictions"][0]["distance_meters"]
      
      # Place Details request
      details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=geometry&key={api_key}"
      details_response = requests.get(details_url).json()
      
      if details_response["status"] == "OK":
          location = details_response["result"]["geometry"]["location"]
          latitude = location["lat"]
          longitude = location["lng"]
          return {"lat":latitude, "lng":longitude, "dist_meter":dist}
      else:
          return "Error fetching place details:", details_response["status"]
  else:
      return "Error in autocomplete:", autocomplete_response["status"]
  

if __name__=="__main__":
    res=placetocoord(place, lat, long)
    print(res)


