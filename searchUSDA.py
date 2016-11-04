#!/usr/bin/env python

import json
import urllib
import os
import readConfig


searchURITemplate='http://api.nal.usda.gov/ndb/search/?format=json&q={0}&sort=n&max=25&offset=0&api_key={1}'

def loadFile(filename):
  if(os.path.exsists(filename)):
    infile = open(filename, 'r')
    dataJSON = json.loads(infile.read())
    infile.close()
    return dataJSON
  else:
    return null

if __name__ == '__main__':

  # Get user's choice
  choice = ""
  while choice == "":
    choice = raw_input('Enter search term: ')

  choice.replace(' ', '%20')
  key = readConfig.readKey('configuration.cfg', 'api.data.key.gov')
  url = searchURITemplate.format(choice,key)
  print ('Call Url: ' + url)
  
  uriSocket = urllib.urlopen(url)
  if (uriSocket.getcode() == 200):
    data=uriSocket.read()
    dataJSON = json.loads(data)

    print("For search term: " + choice)
    print("Items Found: ")
    print(dataJSON['list']['end'])

    for item in dataJSON['list']['item']:
      print(item['ndbno'] + " : " + item['name'])

    # Write data to file
    outfile = open('usda.dat', 'w')
    print ('Writing to usda.dat: '+ str(len(data)) + ' bytes')
    outfile.write(json.dumps(dataJSON,indent=4))
    outfile.close()
  
    choice = raw_input('Output written to usda.dat.  View raw data (y/N)? ')
    if choice == 'y'.upper():
      print ('Key')
      for keys in dataJSON.keys():
        print keys
        print '====='
        print dataJSON[keys]
  else:
    print("Error in request: " + str(uriSocket.getcode()))
