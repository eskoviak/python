import math

lat1 = 39.7684
long1 = -86.1581
lat2 = 42.35281
long2 = -71.05516
R = 6.371e3

phi1 = math.radians(lat1)
phi2 = math.radians(lat2)
delphi = math.radians(lat2 - lat1)
dellambda = math.radians(long2 - long1)
print(phi1, phi2, delphi, dellambda)

a = math.sin(delphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dellambda/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
print(R * c)
