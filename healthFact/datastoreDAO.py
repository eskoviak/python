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

# [INSTATNCE VARIABLESs]
#   -- Defaults
project_id = 'spartan-thunder-130321'
namespace = 'myhealth'
# [END INSTATNCE VARIABLES]

def __createClient(project_id=project_id, namespace=namespace):
    return datastore.Client(project_id, namespace, credentials=GoogleCredentials.get_application_default())

def __createEntry():
    # use defaults
    client = __createClient()

    # build the basic entity
    entity = datastore.Entity(key=client.key('healthFact'))
    entity['observationDate'] = datetime.datetime.today()
    entity['type'] = None
    entity['value'] = None
    return client, entity

def makeBPEntry(date, systolic, diastolic, hr=None, source='Omron', comments=None):
    if (systolic < 60 or systolic > 200 or diastolic < 60 or diastolic > 200):
        raise AttributeError('observations out of range')
    else: 
        entityValue = measurements.BloodPressure(systolic, diastolic, hr)

    # create the client and entry objects
    (client, entity) = __createEntry()

    # populate the entry object
    entity['observationDate']=date
    entity['type'] = u'BloodPressure'

    # create the payload; write it to the entity as a JSON object
    payload = dict()
    payload['source'] = source
    payload['comments'] = comments
    payload['value'] = entityValue.toEntity()
    entity['value'] = json.dumps(payload)

    # write the datastore
    client.put(entity)

def makeWeightEntry(date, weight, units, bodyFat=None, source='Omron', comments=None):
    entityValueW = measurements.Weight(weight, units, bodyFat)
#    if bodyFat != None:
#        entityValueBF = measurements.BodyFat(bodyFat)
#    else:
#        entityValueBF = None

    # create the client and entry objects
    (client, entity) = createEntry()
     
    # populate the entry object
    entity['observationDate'] = date
    entity['type'] = u'Weight/BodyFat'
    payload = dict()
    payload['source'] = source
    payload['comments'] = comments
    payload['value'] = '{"weight" :' + entityValueW.toEntity() + ',' +' "bodyFat" : ' + entityValueBF.toEntity() + '}' 
    entity['value'] = json.dumps(payload)

    # write the datastore
    client.put(entity) 

