"""
  Module measurements

  Contains classes which represent the basic units used for recording health facts

"""
import standards

class BloodPressure:
    """Class BloodPressure.

    This class represents a Blood pressure measurement, which consists of three values::

        **Systolic Pressure:**  (the upper number)

        **Diastolic Pressure:** (the lower number)

        **Heart Rate:** The rate at which your heart is beating, in beats per minute (bpm).

    """
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
    """Class Weight

    This class represents a weight measurement

    """
    def __init__(self, weight, unitsId=None):
        self.__value = float(weight)
        if(unitsId==None):
            self.__units = 'lbm'
        if(unitsId in standards.dictWeight ):
            self.__units = unitsId
        else:
            raise AttributeError('Unknown attribute: ' + unitsId)
   
    def __getitem__(self, key):
        if(key == 'value'):
            return self.__value
        if(key == 'units'):
            return self.__units
        raise KeyError('Unknown key: ' + key)
    
    def convert(self, value, fromUnits, toUnits):
	try:
		return standards.convWeight(self, value, fromUnits, toUnits)
	except KeyError as ke:
		raise KeyError('Bad conversion: ' + ke.message)

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
  if (Weight['units'] == 'lbm'or Weight['units'] == 'lb') :
    factor = 9.8
  else:
    factor = 21.6

  LBM = Weight['value'] * (1 - (BodyFat['value']/100))
  BMR = LBM * factor + 370
  return (LBM, BMR)
