#!/usr/bin/env python

# File bloodPressure.py

import datetime

if __name__ == '__main__':
    entry = dict()
    entry['observationDate']=datetime.datetime(2016,10,27,11,00,00)
    entry['source'] = 'Omron'
    entry['type'] = 'BloodPressure'
    
    for item in {'systolic', 'diastolic', 'heartrate'}:
	

    print(entry)
