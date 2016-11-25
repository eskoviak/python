#!/usr/bin/env python

# File readDatastore.py

from google.cloud import datastore
import json

# Setup credentials
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()


def create_client(project_id, namespace):
    return datastore.Client(project_id, namespace, credentials)

def get_obs(client):
    query = client.query(kind='healthFact')
    query.order=('observationDate')

    return list(query.fetch())


if __name__ == '__main__':
    project_id = 'spartan-thunder-130321'
    namespace = 'myhealth'

    client = create_client(project_id, namespace)
    obs = get_obs(client)
    for item in obs:
	print('===')
	print(item)

        
