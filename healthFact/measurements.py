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

    This class represents a weight measurement.   A weight measurement has both the body weight 
    component, in various (specfied) units, and a body fat measurement in percent (0#.#).  Either
    may be null (None), but at least one must be specified.

    """
    def __init__(self, weight=None, unitsId=None, bodyFat=None):
        if (weight == None and bodyFat == None):
            raise SyntaxError('either weight or body fat must be specified')
        
        if( weight != None):
            self.__weight = float(weight)
        else:
            self.__weight = None

        if(unitsId==None):
            self.__units = 'lbm'
        elif(unitsId in standards.dictWeight ):
            self.__units = unitsId
        else:
            raise AttributeError('bad weights unit specified' + unitsId)

        if(bodyFat != None ):
          self.__bodyFat = float(bodyFat)
        else:
          self.__bodyFat = None

   
    def __getitem__(self, key):
        if(key == 'weight'):
            return self.__weight
        if(key == 'units'):
            return self.__units
        if(key == 'bodyFat'):
            return self.__bodyFat
        raise KeyError('Unknown key: ' + key)
    
    def convert(self, value, fromUnits, toUnits):
        """method convert
 
        This only makes sense for weight, if weight is defined (not None)

        """
        if (self.__weight != None ):
            try:
                return standards.convWeight(self, fromUnits, toUnits)
            except KeyError as ke:
                raise KeyError('Bad conversion: ' + ke.message)

    def toEntity(self):
        d = dict()
        d['weight']=self.__weight
        d['units']=self.__units
        d['bodyFat']=self.__bodyFat
        return d

def calcLBM(Weight):
  if (Weight['weight'] == None or Weight['bodyFat'] == None):
    raise SytaxError('both weight and bodyfat must exsit')

  if (Weight['units'] == 'lbm'or Weight['units'] == 'lb') :
    factor = 9.8
  else:
    factor = 21.6

  LBM = Weight['weight'] * (1 - (Weight['bodyFat']/100))
  BMR = LBM * factor + 370
  return (LBM, BMR)
