from googleplaces import GooglePlaces, types

import json

API_KEY = 'AIzaSyBoE7AXEdbfic8WGVoSTyXRayhVQX1WXHg'

google_places = GooglePlaces(API_KEY)

result = google_places.nearby_search(lat_lng={'lat': 37.269766, 'lng': -76.716478}, radius=1000, types=[types.TYPE_PARK])

for place in result.places:
    # Returned places from a query are place summaries.
    print (place.name)
    # print (place.geo_location)
    # print (place.place_id)

    # The (following method has to make a further API call.
    # place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    # print (place.details) # A dict matching the JSON response from Google.
    # print (place.local_phone_number)
    # print (place.international_phone_number)
    # print (place.website)
    # print (place.url)

