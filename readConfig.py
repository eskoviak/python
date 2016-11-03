#!/usr/bin/env python

import os

fp_default = configuration.cfg

def readKey(fp, key):
  if (! os.path.exists(fp):
    fp = fp_default

  inFile = open(fp, 'r')

  
