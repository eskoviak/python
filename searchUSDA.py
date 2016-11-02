#!/usr/bin/env python

import json
import urllib

#environments = { 'ENVA' : 'http://ap-karafa-dev:8181/api/policies/',
#    'ENVB' : 'http://ap-karafb-dev:8181/api/policies/',
#     'localhost' : 'http://localhost:8181/api/policies/'

searchURITemplate='http://api.nal.usda.gov/ndb/search/?format=json&q={0}&sort=n&max=25&offset=0&api_key=bGE2B4vNAnAy0w6BvUmZTAsd5v8UM7PZQP4b7DGT'

def loadFile(filename):
  infile = open(filename, 'r')
  dataJSON = json.loads(infile.read())
  infile.close()
  return dataJSON

if __name__ == '__main__':

  # Get user's choice
  choice = ""
  while choice == "":
    choice = raw_input('Enter search term: ')

  choice.replace(' ', '%20')

  url = searchURITemplate.format(choice)
  print ('Call Url: ' + url)
  data = urllib.urlopen(url).read()
  dataJSON = json.loads(data)

    # Write data to file
  outfile = open('usda.dat', 'w')
  print ('Writing to usda.dat: '+ str(len(data)) + ' bytes')
  outfile.write(json.dumps(dataJSON,indent=4))
  outfile.close()
  choice = raw_input('Output written to usda.dat.  View raw data (y/N)? ')
  if choice == "y".upper():
    print ('Key')
    for keys in dataJSON.keys():
      print keys
      print '====='
      print dataJSON[keys]