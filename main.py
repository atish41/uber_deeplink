import urllib.parse

def generate_uber_deeplink(client_id, pickup_lat, pickup_lng, pickup_nickname, dropoff_lat, dropoff_lng, dropoff_nickname):
    base_url = "https://m.uber.com/"
    
    # Define parameters
    params = {
        'action': 'setPickup',
        'client_id': client_id,
        'pickup[latitude]': pickup_lat,
        'pickup[longitude]': pickup_lng,
        'pickup[nickname]': pickup_nickname,
        'dropoff[latitude]': dropoff_lat,
        'dropoff[longitude]': dropoff_lng,
        'dropoff[nickname]': dropoff_nickname
    }
    
    # Encode parameters
    encoded_params = urllib.parse.urlencode(params, safe='[]')
    
    # Construct full URL
    deeplink_url = f"{base_url}?{encoded_params}"
    
    return deeplink_url

# Example usage
'''client_id = "ozYFgFCbquB7cYJF9rW_3_0e5vhxcHmi"
pickup_lat = 28.6562
pickup_lng = 77.2410
pickup_nickname = "red fort"
dropoff_lat = 28.5535
dropoff_lng = 77.2588
dropoff_nickname = "lotus temple"
#https://m.uber.com/ul/?client_id=<CLIENT_ID>&action=setPickup&pickup[latitude]=37.775818&pickup[longitude]=-122.418028&pickup[nickname]=UberHQ&pickup[formatted_address]=1455%20Market%20St%2C%20San%20Francisco%2C%20CA%2094103&dropoff[latitude]=37.802374&dropoff[longitude]=-122.405818&dropoff[nickname]=Coit%20Tower&dropoff[formatted_address]=1%20Telegraph%20Hill%20Blvd%2C%20San%20Francisco%2C%20CA%2094133&product_id=a1111c8c-c720-46c3-8534-2fcdd730040d
deeplink = generate_uber_deeplink(client_id, pickup_lat, pickup_lng, pickup_nickname, dropoff_lat, dropoff_lng, dropoff_nickname)
print(deeplink)'''
