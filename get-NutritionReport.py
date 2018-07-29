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
            if(nutrient['nutrient_id'] == nutrientId):
                return nutrient

    return ''

# Globals
nutrientList = dict(Energy='208', Fat='204', Carbs='205', Protein='203')


if(__name__ == '__main__'):
    test_ndbno = '45057514'
    (ret,jsonResp) = reportUSDA(test_ndbno, 'f')
    if(debug):
        print(json.dumps(jsonResp))

    print(jsonResp['report']['food']['name'])
    print(str.format("Per {0} grams:", 100))
    nutrientKeys = nutrientList.keys()
    nutrients=jsonResp['report']['food']['nutrients']   #should be the nutrients dict
    #print(getNutrientItem(nutrients, '208'))
    print('Nutrient\tValue\tUnits')
    for key in nutrientKeys:
        nutrientDetail = getNutrientItem(nutrients, nutrientList[key])

        if(len(nutrientDetail) > 0):
            print(str.format("{0}\t\t{1}\t{2}",
                nutrientDetail['name'],
                nutrientDetail['value'],
                nutrientDetail['unit']))

  