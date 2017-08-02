#!/usr/bin/env python

import json
import urllib.request
import os
import sys

environments = {
    'ENVA' : 'http://ap-karafa-dev:8181/api/policies/',
    'ENVB' : 'http://ap-karafb-dev:8181/api/policies/',
    'localhost' : 'http://localhost:8181/api/policies/',
    'QAG' : 'https://karaf-g.infarmbureau.com:8443/api/policies/',
    'ESB' : 'http://esb2-dev.infarmbureau.com:9081/',
    'RWSJAMS' : 'http://rwsjamswebcln/jams/get-api-agent'
    }

def loadFile(filename):
    try:
        infile = open(filename, 'r')
        fileData = json.loads(infile.read())
        infile.close()
        return fileData
    except IOError as ioe:
        print(ioe.message)

if __name__ == '__main__':

    # Get user's choice
    choice = input('Enter (U)rl or (F)ile name: (U/f): ')
    if choice == None:
        print('Using URL') 
        choice = 'U'

    if choice == 'U' or choice == 'u':
        while True:
            print('Choose environment:')
            for key in environments.keys():
              print(key)
            inKey = input('--> ')
            if (inKey in environments):
              break
    else:
        print("Not in list.  Try again")

    if inKey == 'ESB':
        try:
            req = loadFile('autoPolicyRq.xml')
        except:
            print('Exception in ESB')
            
    # Get Policy number; replace space with '%20'
    policyNumber = input('Enter Policy Number: ').replace(" ", "%20").upper()
    url = environments[inKey]+policyNumber;
    if(inKey == 'localhost'):
        # TODO add suffix based on policy type
        pass
        
    print ('Call Url: ' + url)
    response = urllib.request.urlopen(url).read()
    #print(response)
    
    #fileData = json.loads(response)

    # Write response to file
    outfile = open('output.html', 'w')
    print ('Writing to output.dat: '+ str(len(response)) + ' bytes')
    #outfile.write(json.dumps(fileData,indent=4))
    outfile.write(str(response))
    outfile.close()
    # choice = input('Output written to output.dat.  View file on console (y/N)? ')
    # if choice == "y".upper():
    #     pass
    # else:
    #     filename = input('Enter filename: (./output.dat)')
    #     if filename == "":
    #         filename = "./output.dat"
    #     fileData = loadFile(filename)
   


