#!/usr/bin/env python

# File bloodPressure.py

import datetime
import json
import sys
sys.path.append('./healthFact')
import measurements


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
  bp = measurements.BloodPressure(120,80)

  print(json.dumps(bp.toEntity()))

  w = measurements.Weight(172.7, 'lbm')

  try:
    w1=measurements.Weight(172.7, 'g')
  except AttributeError as ae:
    print (ae.message)
  
  try:
        print(w.convert(1.0, 'kg', 'lbm'))
        print(w.convert(1.0, 'lbm', 'kg'))
        print(w.convert(1.0, 'g', 'kg'))
  except KeyError as ke:
        print(ke.message)
    
  print(json.dumps(w.toEntity()))

  b = measurements.BodyFat(15.5)
  print(json.dumps(b.toEntity()))

  (lbm, bmr) = measurements.calcLBM(w,b)
  print lbm, bmr
  
