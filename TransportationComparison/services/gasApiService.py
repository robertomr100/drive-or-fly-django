import http.client
import os
import json


def getGasPricesByUSState():

  conn = http.client.HTTPSConnection("api.collectapi.com")
  
  headers = {
      'content-type': "application/json",
      'authorization': os.getenv("COLLECT_API_KEY")
      }
  
  conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)
  
  res = conn.getresponse()
  data = res.read()
  data_as_json = json.loads(data)

  return data_as_json['result']['state']['gasoline']
  