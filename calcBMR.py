#!/usr/bin/env python

import sys

def calcBMR(weight, bodyFat):
  lbm = weight * ( 1.0 - bodyFat)
  bmr = lbm * 9.8 + 370.0
  return (lbm,bmr)

if __name__ == "__main__":
 
  if (len(sys.argv) == 3): 
    # assume arg[1] = weight in lbm,
    # arg[2] = body fat (##.# %)

    #weight = float(sys.argv[1])
    #bodyFat = float(sys.argv[2])/100.0

    (lbm, bmr) = calcBMR(float(sys.argv[1]), float(sys.argv[2])/100.0)
    print("Lean Body Mass: {0} (lbm), BMR: {1} (kCal/day)".format(lbm, bmr))

  else:
    print("Usage:  calcBMR.py <weight> <bodyFat>")
    
