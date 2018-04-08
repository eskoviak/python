"""Module datastoreDAO

This module represents the Data Access Object for accessing the Google Cloud Datastore
object which contains the data for the the TrackMyHealthData application.

"""
# [IMPORTS]
import measurements
from google.cloud import datastore
import datetime
import json
from oauth2client.client import GoogleCredentials

# [MODULE LEVEL VARIABLES]
credentials = GoogleCredentials.get_application_default()
"""The credentials for access

These default to the application default
"""
project_id = 'spartan-thunder-130321'
"""The default project id
"""
namespace = 'myhealth'
"""The default namespace
"""

def __createClient(project_id=project_id, namespace=namespace):
    """The internal createClient function.

    This function is similar to the traditional DAO open connection function:  It returns
    an object which is connected to the cloud datastore and is the root for all operations.

    Args:
        project-id (string):  The Google project ID.
        namespace (string):  The namespace (or ancestor namespace)

    Returns:
        datastore.Client:  The client object

    """

    return datastore.Client(project_id, namespace, credentials=GoogleCredentials.get_application_default())

def createEntry():
    """The internal createEntry function

    This function first creates the client, using the defaults.  It creates a empty
    entry object object.

    Args:
        None

    Returns:
      (client, entry): The current client and entry objects.

    """

    # use defaults
    client = __createClient()

    # build the basic entity
    entity = datastore.Entity(key=client.key('healthFact'))
#    entity['observationDate'] = datetime.datetime.today()
#    entity['type'] = None
#    entity['value'] = None
    return client, entity

def makeBPEntry(date, systolic, diastolic, hr=None, source='Omron', comments=None):
    if (systolic < 60 or systolic > 200 or diastolic < 60 or diastolic > 200):
        raise AttributeError('observations out of range')
    else: 
        entityValue = measurements.BloodPressure(systolic, diastolic, hr)

    # create the client and entry objects
    (client, entity) = __createEntry()

    # populate the entry object
    entity['obsDate']=date
    entity['type'] = u'bp'

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

if __name__ == '__main__':
    print 'This module should not be called directly.  It is intended to be used as an\nimported module'

