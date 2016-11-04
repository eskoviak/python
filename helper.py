#!/usr/bin/env python

import readConfig

if __name__ == "__main__":
  print(readConfig.readKey("configuration.cfg", "api.data.key.gov"))
