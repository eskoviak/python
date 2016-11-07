"""
  Class BloodPressure

  This class encapsulates a blood pressure reading.  It does not represent the temporal
  aspects of the reading (time of observation or method); that is left to the client to
  record.

  There is no provision for inputing the units or converting them--they are assumed to be
  mmHg for pressure and bpm (beats per minute) for the rate.

"""

Class BloodPressure:

  def __init__(self):
    self.__systolic = 0
    self.__diastolic = 0
    self.__heartRate = 0

  def __init__(self, systolic, diastolic):
    self.__systolic = systolic
    self.__diastolic = diastolic
    self.__heartRate = 0

  def __init__(self, systolic, diastolic, heartRate):
    self.__systolic = systolic
    self.__diastolic = diastolic
    self.__heartRate = 0 

  def toEntity():
    d["systolic"] = self.__systolic
    d["diastolic"] = self.__diastolic
    d["heartRate"] = self.__heartRate
    return d
