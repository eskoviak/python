#
# get-NutritionReport -- Accepts an USDA NDBNo from command line and gets
# the nutrients specified in the nurtientList
#

import sys
import json
import readConfig
import urllib.request

debug = False

def reportUSDA(ndbno, type):
  key = readConfig.readKey('configuration.cfg', 'api.data.key.gov')
  reportURITemplate = readConfig.readKey('configuration.cfg', 'reportURITemplate')
  url = reportURITemplate.format(ndbno,key)
  if(debug):
    print("Search URI: " + url)

  uriSocket = urllib.request.Request(url)
  try:
    response = urllib.request.urlopen(uriSocket)
    respCode = response.status
    dataJSON = json.loads(str(response.read(), encoding='utf-8'))
    return(respCode, dataJSON)
  except urllib.error.HTTPError as e:
    return(e.code, "")

def getNutrientItem(nutrients, nutrientId):
    if(len(nutrients) > 0):
        for nutrient in nutrients:
            if(int(nutrient['nutrient_id']) == int(nutrientId)):
                return nutrient
    return ''

def getNutrientMeasures(nutrients):
    measuresList = []
    if(len(nutrients) > 0):
        nutrient = nutrients[0]
        for measure in nutrient['measures']:
            measuresList.append((measure['label'],measure['eqv']))
    return measuresList
    
# Globals
nutrientList = dict(Energy='208', Fat='204', Carbs='205', Protein='203')


if(__name__ == '__main__'):
    #test_ndbno = '45057514'
    test_ndbno = '09040' #bananas, raw
    ratio = .32
    (ret,jsonResp) = reportUSDA(test_ndbno, 'f')
    if(debug):
        print(json.dumps(jsonResp))

    print(jsonResp['report']['food']['name'])
    print(str.format("Per {0} grams:", 100 * ratio))
    nutrients=jsonResp['report']['food']['nutrients']   #should be the nutrients dict
    if(debug):
        print(nutrients)
    #print(getNutrientItem(nutrients, '208'))
    print('Nutrient\tValue\tUnits')
    for value in nutrientList.values():
        nutrientDetail = getNutrientItem(nutrients, value)

        if(len(nutrientDetail) > 0):
            print(str.format("{0}\t\t{1}\t{2}",
                nutrientDetail['name'],
                float(nutrientDetail['value']) * ratio,
                nutrientDetail['unit']))
    print(getNutrientMeasures(nutrients))

  