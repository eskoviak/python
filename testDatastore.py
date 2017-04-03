#!/usr/bin/env python
"""Module testDatastore

Used to test the healthFact.datastoreDAO module

Author:  eskoviak@gmail.com
Version: 0.9.0

"""

from google.cloud import datastore
import sys
sys.path.append('./healthFact')
import datastoreDAO


if __name__ == '__main__':

    client, entry = datastoreDAO.createEntry()

    print client,entry
