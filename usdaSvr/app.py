import io
import json
from json import dumps
import readConfig
from flask import Flask
import urllib.request
app = Flask(__name__)

@app.route('/search/upc/<upc>')
def seachUPC(upc):
  try:
    # key = readConfig.readKey('configuration.cfg', 'api.data.key.gov')
    url = (readConfig.readKey('configuration.cfg', 'usdaBaseUrl')+readConfig.readKey('configurtion.cfg', 'usdaGetSearchUri'))
    filter = ('/?api_key='+readConfig.readKey('configuration.cfg', 'api.data.key.gov') + '&query=' + upc)

    uriSocket = urllib.request.Request(url+filter) 
    try:
      response = urllib.request.urlopen(uriSocket)
      respCode = response.status
      dataJSON = json.loads(str(response.read(), encoding='utf-8'))
      return('{ "fdcId" : ' + str(dataJSON['foods'][0]['fdcId']) + '}')
    except urllib.error.HTTPError as e:
      return(e.code, "")    
  except FileNotFoundError as fnf:
        return (fnf.errno, '')

@app.route('/food/<fdcId>')
def queryFdcid(fdcId):
  try:
    url = readConfig.readKey('configuration.cfg', 'usdaBaseUrl') + 'v1/food/' + fdcId  + '/?api_key='+readConfig.readKey('configuration.cfg', 'api.data.key.gov')
    uriSocket = urllib.request.Request(url) 
    try:
      response = urllib.request.urlopen(uriSocket)
      respCode = response.status
      dataJSON = json.loads(str(response.read(), encoding='utf-8'))
      #foodNutrients = dataJSON['foodNutrients']
      
      description = dataJSON['description']
      #records = []
      #for foodNutrient in foodNutrients:
      #  id = foodNutrient['id']
      #  name = foodNutrient['nutrient']['name']
      #  units = foodNutrient['nutrient']['unitName']
      #  amount = foodNutrient['amount']
      #  records.append(dict(id = id, name=name, units=units, amount=amount))
      #return('{ "' +str(ingredient) +'": ' + json.dumps(records) + '}')
    except urllib.error.HTTPError as e:
      return(e.reason)
    except:
      return('{"message":"in other exception"}')
  except FileNotFoundError as fnf:
    return (fnf.errno, '') 