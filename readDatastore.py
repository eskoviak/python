# File readDatastore.py
from google.cloud import datastore
import json



def create_client(project_id, namespace):
    return datastore.Client(project_id,namespace)

def get_obs(client):
    query = client.query(kind='data')

    return list(query.fetch())


if __name__ == '__main__':
    project_id = 'spartan-thunder-130321'
    namespace= 'myhealth'

    client = create_client(project_id, namespace)
    obs = get_obs(client)
    for item in obs:
        print json.loads(item)

        
