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
    # this lets google create key of kind 'healthFact'
    # key = client.key('healthFact')
    with client.transaction():
        incomplete_key = client.key('healthFact')
        entry = datastore.Entity(key=incomplete_key)

        entry.update({
            'observationDate' : datetime.datetime.utcnow(),
            'source' : 'Omron',
            'type' : 'BodyFat',
            'value' : { 'value' : 14.1, 'units' : '%' }
        })

        client.put(entry)
