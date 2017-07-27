#!/usr/bin/env python

import json
import urllib.request
import os
import readConfig


searchURITemplate='http://api.nal.usda.gov/ndb/search/?format=json&q={0}&sort=n&max=25&offset=0&api_key={1}'
reportURITemplate='http://api.nal.usda.gov/ndb/reports/?ndbno={0}&type=f&format=json&api_key={1}'
debug = True

def loadFile(filename):
  if(os.path.exsists(filename)):
    infile = open(filename, 'r')
    dataJSON = json.loads(infile.read())
    infile.close()
    return dataJSON
  else:
    return null

def searchUSDA(criteria):
  choice.replace(' ', '%20')
  key = readConfig.readKey('configuration.cfg', 'api.data.key.gov')
  url = searchURITemplate.format(choice,key)
  if(debug):
    print("Search URI: " + url)

  uriSocket = urllib.request.urlopen(url)
  respCode = uriSocket.getcode()
  if (respCode == 200):
    dataJSON = json.loads(uriSocket.read())
    return(respCode, dataJSON)
  else:
    return(respCode, "")

def reportUSDA(ndbno, type):
  key = readConfig.readKey('configuration.cfg', 'api.data.key.gov')
  url = reportURITemplate.format(ndbno,key)
  if(debug):
    print("Search URI: " + url)

  uriSocket = urllib.request.urlopen(url)
  respCode = uriSocket.getcode()
  if (respCode == 200):
    dataJSON = json.loads(uriSocket.read())
    return(respCode, dataJSON)
  else:
    return(respCode, "")

if __name__ == '__main__':

  # Get user's choice
  choice = ""
  while choice == "":
    choice = input('Enter search term: ')
  
  (code, dataJSON) = searchUSDA(choice)
  if(debug):  
    print("For search term: " + choice)
    print("Items Found: ")
    print(dataJSON['list']['end'])

  if(code == 200):
    for item in dataJSON['list']['item']:
      print(item['ndbno'] + " : " + item['name'])
    choice=input('Enter NDBNO to report: ')
    (code, dataJSON) = reportUSDA(choice, 'f')
    if(code == 200):
      #print(len(dataJSON['report']['food']['nutrients']))
      for nutrient in dataJSON['report']['food']['nutrients']:
        print(nutrient['name']) 
  else:
    print("Error in request: " + str(code))
    choice=input('Press \'Enter\' to continue...')
    exit(-1)

  if(debug):
    # Write data to file
    outfile = open('usda.dat', 'w')
    print ('Writing to usda.dat: '+ str(len(dataJSON)) + ' bytes')
    outfile.write(json.dumps(dataJSON,indent=4))
    outfile.close()
    choice=input('Press \'Enter\' to continue...')
  
