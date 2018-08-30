# get-NutritionReport -- Accepts an USDA NDBNo from command line and gets
# the nutrients specified in the nurtientList
#

import sys
import json
import readConfig
import urllib.request
import io

debug = False

def loadfoodItemFile(filename):
    try:
        foodItem = json.load(io.open(filename))
        return (0, foodItem)
    except FileNotFoundError as fnf:
        return (fnf.errno, '')



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
    
def getCompositeNutrition(ingredientList):
    if len(ingredientList) >0:
        for ingredient in ingredientList:
            (ndbNo, measure) = ingredient
            (ret)

def getIntakeRecord(nutrients, ratio):
    intake = list()
    for value in nutrientList.values():
        nutrientDetail = getNutrientItem(nutrients, value)
        if(len(nutrientDetail) > 0):
            intake.append( (nutrientDetail['name'], float(nutrientDetail['value']) * ratio, nutrientDetail['unit']) )
    return intake           

# Globals
nutrientList = dict(Energy='208', Fat='204', Carbs='205', Protein='203')


if(__name__ == '__main__'):
    (ret, foodItem) = loadfoodItemFile("foodDiary8-29.json")
    if ret == 0:

        for ingredient in foodItem['ingredients']:
            if debug:
                print(ingredient['ndbNo'])
            (ret, foodItemReport) = reportUSDA(ingredient['ndbNo'], 'f')
            if debug:
                print(ret, json.dumps(foodItemReport))
            nutrients=foodItemReport['report']['food']['nutrients']   #should be the nutrients dict
            if ingredient['qtyMeasure'] == 'g':
                ratio = float(ingredient['qty'])/100.0
                measureFullName = 'g'
            else:
                measures = getNutrientMeasures(nutrients)
                found = False
                for measure in measures:
                    if ingredient['qtyMeasure'] in measure[0]:
                        measureFullName = measure[0]
                        if found == True:
                            print("found multiple measure matches--using first")
                            break
                        else:
                            ratio = float(measure[1])/100.0
                            found = True
            #(name, value, unit) = getIntakeRecord(nutrients, ratio)
            print(str('{0}; {1} {2}').format(  foodItemReport['report']['food']['name'],
                ingredient['qty'], measureFullName ))
            print(getIntakeRecord(nutrients, ratio))

    else:
        print('Error')



"""     
    #test_ndbno = '45057514'  # 
    #test_ndbno = '09040' #bananas, raw
    ingredientList = [('11457', 116), ('45198639', 214) ]
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
 """
  