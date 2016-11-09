"""
  Module measurements

  Contains classes which represent the basic units used for recording health facts

"""
"""
  Class BloodPressure

  This class encapsulates a blood pressure reading.  It does not represent the temporal
  aspects of the reading (time of observation or method); that is left to the client to
  record.

  There is no provision for inputing the units or converting them--they are assumed to be
  mmHg for pressure and bpm (beats per minute) for the rate.

"""
class BloodPressure:

  def __init__(self, systolic, diastolic, heartRate=None):
    self.__systolic = systolic
    self.__diastolic = diastolic
    if(heartRate==None):
      self.__heartRate = 0
    else:
      self.__heartRate = heartRate 

  def toEntity(self):
    d=dict()
    d["systolic"] = self.__systolic
    d["diastolic"] = self.__diastolic
    d["heartRate"] = self.__heartRate
    return d

"""
  class Weight

  This class encapsulates a weight measurement.  It includes both the value and the units
  identifier.

"""
class Weight:

  def __init__(self, weight, unitsId=None):
    self.__value = float(weight)
    if(unitsId==None):
      self.__units = 'lbm'
    else:
      self.__units=str(unitsId)

  def __convert__(self, unitsId):
    if(unitsId == self.__units):
      return float(self.__value)
    elif (unitsId == 'kg' and self.__units == 'lbm'):
      return float(self.__value/2.204)
    elif (unitsId == 'lbm' and self.__units == 'kg'):
      return float(self.__value * 2.204)

  def toEntity(self):
    d = dict()
    d['value']=self.__value
    d['units']=self.__units
    return d