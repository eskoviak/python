#!/usr/bin/env python

# File bloodPressure.py

import datetime
import json
import sys
sys.path.append('./healthFact')
import measurements

# class BloodPressure:

#   def __init__(self, systolic, diastolic, heartRate=None):
#     self.__systolic = systolic
#     self.__diastolic = diastolic
#     if(heartRate==None):
#       self.__heartRate = 0
#     else:
#       self.__heartRate = heartRate 

#   def toEntity(self):
#     d=dict
#     d["systolic"] = self.__systolic
#     d["diastolic"] = self.__diastolic
#     d["heartRate"] = self.__heartRate
#     return d

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

  w = measurements.Weight(100, 'lbm')
  
  print(w.__convert__('kg'))
  print(w.__convert__('lbm'))
  print(json.dumps(w.toEntity()))
  
