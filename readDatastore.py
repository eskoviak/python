# File readDatastore.py
from google.cloud import datastore
import json



def create_client(project_id):
    return datastore.Client(project_id)

def get_obs(client):
    query = client.query(kind='data')

    return list(query.fetch())


if __name__ == '__main__':
    project_id = '5629499534213120'

    client = create_client(project_id)
    obs = get_obs(client)
    for item in obs:
        print json.loads(item)

        