import requests
from amadeus import Client, ResponseError
import os


amadeus = Client(
    client_id=os.getenv("AMADEUS_API_KEY"),
    client_secret=os.getenv("AMADEUS_API_SECRET")
)

def getFlights(startPlace, destination,  date):
  try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode=startPlace,
        destinationLocationCode=destination,
        departureDate=date,
        adults=1)
    print(response.data)
  except ResponseError as error:
    print(error)


def getAirports(lat, long):
  response =  amadeus.reference_data.locations.airports.get(
    longitude=long,
    latitude=lat
)
  return  response.data
#https://api.flightapi.io/roundtrip/6338e52003fdff3db04ceabd/LHR/LAX/2019-10-11/2019-10-15/2/0/1/Economy/USD



#https://api.flightapi.io/onewaytrip/6338e52003fdff3db04ceabd/LHR/LAX/2019-10-11/2/0/1/Economy/USD

