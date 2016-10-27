#!/usr/bin/env python

# File updateDatastore.py

from google.cloud import datastore

# Setup credentials
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()


def create_client(project_id, namespace):
    return datastore.Client(project_id, namespace, credentials)

def get_obs(client):
    id=5654313976201216L
    #query = client.query(kind='healthFact')
    query = client.query(id=id)
    #query.filter('__key__ =', id)

    return list(query.fetch())


if __name__ == '__main__':
    project_id = 'spartan-thunder-130321'
    namespace = 'myhealth'
    id=5654313976201216L

    client = create_client(project_id, namespace)
    obs = get_obs(client)
    for item in obs:
	print('===')
	print(item)

        
