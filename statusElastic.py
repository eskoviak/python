#!/usr/bin/env python3

import readConfig

elasticURITemplate = "{0}{1}"

def getElasticURI():
  return readConfig.readKey('configuration.cfg', 'elastic.url')

if __name__ == '__main__':
  print( getElasticURI() )
