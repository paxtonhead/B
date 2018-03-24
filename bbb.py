import math
from geopy.distance import great_circle
from geopy.geocoders import Nominatim


geolocator = Nominatim()
location1 = geolocator.geocode(input())
location2 = geolocator.geocode(input())

smallerLat = min(location1.latitude, location2.latitude)
mlat = (abs(location1.latitude - location2.latitude) / 2) + smallerLat

smallerLon = min(location1.longitude, location2.longitude)
mlon = (abs(location1.longitude - location2.longitude) / 2) + smallerLon

finalString = str(mlat) + ", " + str(mlon)