import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Key')

# lat , lon
location  = gmaps.geocode('my current location')
now = datetime.now()
direction = gmaps.directions("my current location", mode="transit", departure_time=now)