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

# [INSTATNCE VARIABLE]
project_id = 'spartan-thunder-130321'
stringValue = '{ "observation" : { "source" : {0}, "comments" : {1}, "value" : { {2} } } }' 
# [END INSTATNCE VARIABLE]

def __createClient(project_id, namespace='myhealth'):
    return datastore.Client(project_id, namespace, credentials=GoogleCredentials.get_application_default())

def createEntry():
    client = __createClient(project_id)
    incomplete_key = client.key('healthFact')
    return client, datastore.Entity(key=incomplete_key)

def makeBPEntry(date, systolic, diastolic, hr=None, source='Omron', comments=None):
    entityValue = measurements.BloodPressure(systolic, diastolic, hr)

    # create the client and entry objects
    (client, entity) = createEntry()

    # populate the entry object
    entity['observationDate']=date
    entity['type'] = u'BloodPressure'
#    entity['source'] = u'Omron'
#    entity['comments'] = str(comments)
    entity['value'] = stringValue.format(source, comments, json.dumps(entityValue.toEntity()))

    # write the datastore
    client.put(entity)


