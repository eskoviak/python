#!/usr/bin/env python3

import json
import urllib.request
import os
import readConfig
import argparse


searchURITemplate='http://api.nal.usda.gov/ndb/search/?format=json&q={0}&sort=r&max=50&offset=0&api_key={1}'
reportURITemplate='http://api.nal.usda.gov/ndb/reports/?ndbno={0}&type=f&format=json&api_key={1}'
#debug = True

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

  uriSocket = urllib.request.Request(url)
  try:
    response = urllib.request.urlopen(uriSocket)
    respCode = response.status
    dataJSON = json.loads(str(response.read(), encoding='utf-8'))
    return(respCode, dataJSON)
  except urllib.error.HTTPError as e:
    print(e.code)
    return(e.code, "")

def reportUSDA(ndbno, type):
  key = readConfig.readKey('configuration.cfg', 'api.data.key.gov')
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

if __name__ == '__main__':

  # Parse command line arguments
  # TODO This doesn't work!
  debug = True
  parser=argparse.ArgumentParser(description='Searches USDA Database')
  parser.add_argument('-d', '--debug', action='store_true' )
  parser.parse_args()
  print(debug)

  # Get user's criteria
  choice = ""
  while choice == "":
    choice = input('Enter search term: ')
  
  (code, dataJSON) = searchUSDA(choice)
  if(debug):  
    print("For search term: " + choice)
    print("writing response to usda_search_response.json")
    outfile = open('usda_search_response.json', 'w')
    outfile.write(json.dumps(dataJSON, indent=4))
    outfile.close

  if(code == 200):
    
    try:
        for item in dataJSON['list']['item']:
          print(item['ndbno'] + " : " + item['name'])
        choice=input('Enter NDBNO to report: ')
        if(len(choice) > 0):
          (code, dataJSON) = reportUSDA(choice, 'f')
          if(code == 200):
            if(debug):
                outfile = open('usda_report_response.json', 'w')
                outfile.write(json.dumps(dataJSON, indent=4))
                outfile.close      
            try:
              for nutrient in dataJSON['report']['food']['nutrients']:
                print(nutrient['name'])
            except :
              print('report is empty')
    except KeyError as ke :
        print('No matching items found') 
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
  
