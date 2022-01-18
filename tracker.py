import googlemaps
from datetime import datetime
import requests
gmaps = googlemaps.Client(key='Key')

# lat , lon
location  = gmaps.geocode('my current location')
now = datetime.now()
direction = gmaps.directions("my current location", mode="transit", departure_time=now)

def Distance(location1,location):
    

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={location1[0]}%2C-{location1[1]}&destinations={location2[0]}%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=YOUR_API_KEY"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text
