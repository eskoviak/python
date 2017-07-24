from google.cloud import datastore
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
client = datastore.Client('spartan-thunder-130321', 'myhealth', credentials)
