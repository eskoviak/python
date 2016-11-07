#!/usr/bin/env python

# File bloodPressure.py

import datetime
import json
import sys
sys.path.append('.')
import healthFact

def makeBPEntry(date, systolic, diastolic, hr):
    entry = dict()
    entry['observationDate']=date
    entry['source'] = u'Omron'
    entry['type'] = u'BloodPressure'

    values = dict()    
    values['systolic'] = {'value' : systolic,'units':'mmHg'}
    values['diastolic'] = {'value' : diastolic,'units':'mmHg'}
    values['heartRate'] = {'value': hr,'units':'bpm'} 

    entry['value'] = json.dumps(values)
    return entry

if __name__ == '__main__':
  bp = bloodPressure.BloodPressure()

  print(bp)
