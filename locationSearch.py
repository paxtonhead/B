from googleplaces import GooglePlaces, types
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import json, math


geolocator = Nominatim()


def getMidPoint(location1, location2):

  geo_location1 = geolocator.geocode(location1)
  geo_location2 = geolocator.geocode(location2)

  smallerLat = min(geo_location1.latitude, geo_location2.latitude)
  mlat = (abs(geo_location1.latitude - geo_location2.latitude) / 2) + smallerLat

  smallerLon = min(geo_location1.longitude, geo_location2.longitude)
  mlon = (abs(geo_location1.longitude - geo_location2.longitude) / 2) + smallerLon

  return {'lat': mlat, 'lng': mlon}
  

API_KEY = 'AIzaSyBoE7AXEdbfic8WGVoSTyXRayhVQX1WXHg'
google_places = GooglePlaces(API_KEY)

test_location1 = 'Swem Library, Williamsburg, VA'
test_location2 = 'Wawa, Williamsburg, VA'
coordinates = getMidPoint(test_location1, test_location2)

result = google_places.nearby_search(lat_lng=coordinates, radius=1000, types=[types.TYPE_RESTAURANT])

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

