#!/usr/bin/env python

# File insertDatastore.py

from google.cloud import datastore
import datetime

# Setup credentials
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()


def create_client(project_id, namespace):
    return datastore.Client(project_id, namespace, credentials)

if __name__ == '__main__':
    project_id = 'spartan-thunder-130321'
    namespace = 'myhealth'

    client = create_client(project_id, namespace)
    incomplete_key = client.key('healthFact')
    entry = datastore.Entity(key=incomplete_key)

    entry.update({
        'obsDate' : datetime.datetime(2017,03,27,11,20),
        'source' : u'Aria',
        'type' : u'weight', 
        'observation' : u"{ 'weight' : 177.7, 'units' : 'lbm'}"
	})
    client.put(entry)
