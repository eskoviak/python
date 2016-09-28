#!/usr/bin/env python

import json

# TODO Get Environment from user
url = 'http://ap_karafb_dev:8181/api/policies/'

# TODO Get Policy number

# Dummy code for testing
fp = open('users.json', 'r')

#print fp.read()
print json.dumps(json.loads(fp.read()),indent=4)

