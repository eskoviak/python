import pandas as pd
import numpy as np


s = pd.Series([1,2,3,5,8,13])
rate = np.zeros(s.shape)

print(rate)

for index,value in s.items():
    print(f"Items: {index}: Value: {value}")

    if index == 0:
        rate[0]=value
        prev = value
        continue
    rate[index] = value - prev
    prev = value

print(rate)
print(rate)