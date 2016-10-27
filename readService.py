#!/usr/bin/env python

import json
import urllib

environments = { 'ENVA' : 'http://ap-karafa-dev:8181/api/policies/',
    'ENVB' : 'http://ap-karafb-dev:8181/api/policies/'}

def loadFile(filename):
  infile = open(filename, 'r')
  dataJSON = json.loads(infile.read())
  infile.close()
  return dataJSON

if __name__ == '__main__':

  # Get user's choice
  choice = raw_input('Enter (U)rl or (F)ile name: (U/f): ')
  if choice == "": 
    choice = 'U'

  if choice == 'U' or choice == 'u':
    while True:
      print('Choose environment:')
      for key in environments.keys():
        print(key)
      inKey = raw_input('--> ').upper()
      if (inKey in environments):
        break

    # Get Policy number; replace space with '+'
    policyNumber = raw_input('Enter Policy Number: ').replace(" ", "%20").upper()
    url = environments[inKey]+policyNumber;
    print ('Call Url: ' + url)
    data = urllib.urlopen(url).read()
    dataJSON = json.loads(data)

    # Write data to file
    outfile = open('output.dat', 'w')
    print ('Writing to output.dat: '+ str(len(data)) + ' bytes')
    outfile.write(json.dumps(dataJSON,indent=4))
    outfile.close()
    choice = raw_input('Output written to output.dat.  View raw data (y/N)? ')
    if choice == "y".upper():
      print ('Key')
      for keys in dataJSON.keys():
        print keys
        print '====='
        print dataJSON[keys]
  else:
    filename = raw_input('Enter filename: (./output.dat)')
    if filename == "":
      filename = "./output.dat"
    dataJSON = loadFile(filename)
   


