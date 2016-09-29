#!/usr/bin/env python

import json
import urllib

# TODO Get Environment from user
ENVB = 'http://ap-karafb-dev:8181/api/policies/'

# Get Policy number; replace space with '+'
policyNumber = raw_input('Enter Policy Number: ').replace(' ', '+')

print ('Call Url: ' + ENVB+ policyNumber)
#exit(0)

# Dummy code for testing
#fp = open('users.json', 'r')

data = urllib.urlopen(ENVB+policyNumber).read()
outfile = open('output.dat', 'w')

print ('Writing to output.dat: '+ str(len(data)) + ' bytes')
outfile.write(json.dumps(json.loads(data),indent=4))
outfile.close()