#!/usr/bin/env python

import os

fp_default = 'configuration.cfg'

def readKey(fp, searchKey):
  if (not os.path.exists(fp)):
    fp = fp_default

  inFile = open(fp, 'r')
  for line in inFile.readlines():
    if (line[0] == '#' or line.__len__ == 0):
      continue

    (key,value) = line.split("=")
    if ( key == searchKey):
      return value

if __name__ == "__main__":
  readKey("configuration.cfg", "")

  
