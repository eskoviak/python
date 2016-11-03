#!/usr/bin/env python

import os

fp_default = 'configuration.cfg'

def readKey(fp, key):
  if (not os.path.exists(fp)):
    fp = fp_default

  inFile = open(fp, 'r')
  for line in inFile.readlines():
    if (line[0] == '#' or line.__len__ == 0):
      continue

    #print(line)
    (key,value) = line.split("=")
    print("Key: " + key + ", Value: " + value)

if __name__ == "__main__":
  readKey("configuration.cfg", "")

  
