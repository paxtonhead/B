from googleplaces import GooglePlaces, types
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import  math


class Place:

  def __init__(self, k):
    self.key = k
    self.coor = {}
    self.search = None
    self.search_result = None


  def getMidPoint2(self, location1, location2):

    geolocator = Nominatim()

    geo_location1 = geolocator.geocode(location1)
    geo_location2 = geolocator.geocode(location2)

    smallerLat = min(geo_location1.latitude, geo_location2.latitude)
    mlat = (abs(geo_location1.latitude - geo_location2.latitude) / 2) + smallerLat

    smallerLon = min(geo_location1.longitude, geo_location2.longitude)
    mlon = (abs(geo_location1.longitude - geo_location2.longitude) / 2) + smallerLon

    self.coor = {'lat': mlat, 'lng': mlon}
    return self.coor

  def searchGoogle(self, r = 1000):
    self.search = GooglePlaces(self.key)
    self.search_result = self.search.nearby_search(lat_lng = self.coor, radius = r, types = [types.TYPE_RESTAURANT])


  def printSearchInfo(self):
    for place in self.search_result.places:
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


if __name__ == '__main__':

  API_KEY = 'AIzaSyBoE7AXEdbfic8WGVoSTyXRayhVQX1WXHg'


  test_location1 = 'Swem Library, Williamsburg, VA'
  test_location2 = 'Wawa, Williamsburg, VA'

  P = Place(API_KEY)
  P.getMidPoint2(test_location1, test_location2)
  P.searchGoogle()
  P.printSearchInfo()
