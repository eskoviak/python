
# Dictionaries

# Weight
dictWeight = dict()
dictWeight['kg']= 1.0
dictWeight['lbm']=0.4537
dictWeight['lb']=0.4537

def convWeight(self, inValue, fromUnits, toUnits):
    unitsList = dictWeight.keys()
    if( fromUnits in unitsList and toUnits in unitsList):
        # convert inUnits to standard (kg)
        return float(inValue * (dictWeight[fromUnits]/dictWeight[toUnits]))
    else:
        raise KeyError('weight units')

# Length
dictLength = dict()
dictLength['m']= 1.0
dictLength['cm']=0.01


