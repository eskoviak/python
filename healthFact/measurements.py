"""
  Module measurements

  Contains classes which represent the basic units used for recording health facts

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

class Weight:
  def __init__(self, weight, unitsId=None):
    self.__value = float(weight)
    if(unitsId==None):
      self.__units = 'lbm'
    else:
      self.__units=str(unitsId)

  def __getitem__(self, key):
    if(key == 'value'):
      return self.__value
    if(key == 'units'):
      return self.__units
    raise KeyError('Unknown key: ' + key)
    
  def __convert__(self, unitsId):
    if(unitsId == self.__units):
      return float(self.__value)
    elif (unitsId == 'kg' and self.__units == 'lbm'):
      return float(self.__value/2.204)
    elif (unitsId == 'lbm' and self.__units == 'kg'):
      return float(self.__value * 2.204)
    else:
      raise AttributeError('Unknown units identifier: '+unitsId)

  def toEntity(self):
    d = dict()
    d['value']=self.__value
    d['units']=self.__units
    return d

class BodyFat:
  def __init__(self, bodyFat):
    self.__units = '%'
    self.__value = bodyFat

  def __getitem__(self, key):
    if(key == 'value'):
      return self.__value
    if(key == 'units'):
      return self.__units
    return None
  
  def toEntity(self):
    d = dict()
    d['value']=self.__value
    d['units']=self.__units
    return d
    
def calcLBM(Weight, BodyFat):
  if Weight['units'] == 'lbm':
    factor = 9.8
  else:
    factor = 21.6

  LBM = Weight['value'] * (1 - (BodyFat['value']/100))
  BMR = LBM * factor + 370
  return (LBM, BMR)