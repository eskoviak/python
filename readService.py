#!/usr/bin/env python

import json
import urllib

# TODO Get Environment from user
ENVB = 'http://ap-karafb-dev:8181/api/policies/'

# Get Policy number; replace space with '+'
policyNumber = raw_input('Enter Policy Number: ').replace(' ', '+')

if policyNumber != 'output.dat':
  print ('Call Url: ' + ENVB+ policyNumber)

  data = urllib.urlopen(ENVB+policyNumber).read()
  dataJSON = json.loads(data)

  # Write data to file for off line testing and begin exploring the DOM
  outfile = open('output.dat', 'w')
  print ('Writing to output.dat: '+ str(len(data)) + ' bytes')
  outfile.write(json.dumps(dataJSON,indent=4))
  outfile.close()
else:
  infile = open('output.dat', 'r')
  dataJSON = json.loads(infile.read())
  infile.close()

# What do we have?
print ('Key')
for keys in dataJSON.keys():
  print keys
  print '====='
  print dataJSON[keys]
  #for keys1 in (dataJSON[keys]).keys():
  #  print keys1
  #print ('  Children')
  #for key in keys:
    #print ('  ' + dataJSON[key])
    #print key
