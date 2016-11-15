#!/usr/bin/env python

import json
import urllib
import os

environments = {
    'ENVA' : 'http://ap-karafa-dev:8181/api/policies/',
    'ENVB' : 'http://ap-karafb-dev:8181/api/policies/',
    'localhost' : 'http://localhost:8181/api/policies/'
    'ESB' : 'http://esb2-dev.infarmbureau.com:9081/'}

def loadFile(filename):
  infile = open(filename, 'r')
  fileData = json.loads(infile.read())
  infile.close()
  return fileData

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
      inKey = raw_input('--> ')
      if (inKey in environments):
        break
      else:
        print("Not in list.  Try again")

    if inKey == 'ESB':
        try:
            req = loadFile('autoPolicyRq.xml')
        catch:
            print('Exception in ESB')
            
    # Get Policy number; replace space with '+'
    policyNumber = raw_input('Enter Policy Number: ').replace(" ", "%20").upper()
    url = environments[inKey]+policyNumber;
    print ('Call Url: ' + url)
    data = urllib.urlopen(url).read()
    fileData = json.loads(data)

    # Write data to file
    outfile = open('output.dat', 'w')
    print ('Writing to output.dat: '+ str(len(data)) + ' bytes')
    outfile.write(json.dumps(fileData,indent=4))
    outfile.close()
    choice = raw_input('Output written to output.dat.  View raw data (y/N)? ')
    if choice == "y".upper():
      print ('Key')
      for keys in fileData.keys():
        print keys
        print '====='
        print fileData[keys]
  else:
    filename = raw_input('Enter filename: (./output.dat)')
    if filename == "":
      filename = "./output.dat"
    fileData = loadFile(filename)
   


