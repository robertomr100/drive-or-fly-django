import googlemaps
from datetime import datetime
import os

gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

def getLongAndLat(address):
  geocode_result = gmaps.geocode(address)
  return geocode_result



def getCarDuration(startLatLongDict, endLatLongDict):
  distance_matrix_result =gmaps.distance_matrix(startLatLongDict,endLatLongDict)
  return distance_matrix_result['rows'][0]['elements'][0]['duration']['value']
               
  