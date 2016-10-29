#!/usr/bin/env python

# File bloodPressure.py

import datetime
import json


def makeBPEntry(date, systolic, diasotlic, hr):
    entry = dict()
    entry['observationDate']=date
    entry['source'] = u'Omron'
    entry['type'] = u'BloodPressure'

    values = dict()    
    values['systolic'] = {'value':123,'units':'mmHg'}
    values['diastolic'] = {'value':76,'units':'mmHg'}
    values['heartRate'] = {'value':60,'units':'bpm'} 

    entry['value'] = json.dumps(values)
    print(entry)
if __name__ == '__main__':
