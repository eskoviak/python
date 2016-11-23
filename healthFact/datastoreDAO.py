
# datastore DAO file

# [BEGIN IMPORTS]
import measurements
from google.cloud import datastore
import datetime
import json
# [END IMPORTS]

# Setup credentials
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()

def create_client(project_id, namespace='myhealth'):
    return datastore.Client(project_id, namespace, credentials=GoogleCredentials.get_application_default())

def makeBPEntry(date, systolic, diastolic, hr=None, source='Omron'):
    entryValue = measurements.BloodPressure(systolic, diastolic, hr)

    # create the entry object
    project_id = 'spartan-thunder-130321'
    client = create_client(project_id)
    incomplete_key = client.key('healthFact')
    entry = datastore.Entity(key=incomplete_key)

    # populate the entry object
    entry['observationDate']=date
    entry['source'] = u'Omron'
    entry['type'] = u'BloodPressure'
    entry['value'] = json.dumps(entryValue.toEntity())

    # write the datastore
    client.put(entry)


