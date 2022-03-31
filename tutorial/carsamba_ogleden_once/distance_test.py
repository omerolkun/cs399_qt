from haver import calculate_distance
import random


point1 = (64.526, 174.548)
point2  = (23.478, 6.013)

point1 = (76.70056, 145.7372 )
point2  = (34.33361, 65.7025)
print("point1 :" , point1)
print("point2 : ", point2)


for x in range(20):
    lat1 = round(random.uniform(-90,90),3)
    lon1 = round(random.uniform(-180,180),3)
    lat2 = round(random.uniform(-90,90),3)
    lon2 = round(random.uniform(-180,180),3)
    print("lat1: ",lat1)
    print("lon1: ",lon1)
    print("lat2: ",lat2)
    print("lon2: ",lon2)
    p1 = lat1, lon1
    p2 = lat2, lon2
    print("distance = ",calculate_distance(p1,p2))    