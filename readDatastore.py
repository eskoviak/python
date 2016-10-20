# File readDatastore.py
from google.cloud import datastore

def create_client(project_id):
    return datastore.Client(project_id)

client = create_client('5629499534213120')

print(client)