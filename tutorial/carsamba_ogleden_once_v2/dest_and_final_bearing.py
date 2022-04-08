import math
import random
import haver

'''
lat1 = round(random.uniform(-90,90),4)
lon1 = round(random.uniform(-180,180),4)
spoint = lat1, lon1
lat2 = round(random.uniform(-90,90),4)
lon2 = round(random.uniform(-180,180),4)

distance = round(random.uniform(0,6000),0)
bearing = round(random.uniform(0,180),0)
'''



#parameters are start point , inital bearing and distance (distance in km)
def find_destination_point(start_point, distance, bearing):
    radius = 6371000 # the radius of earth in m
    distance = distance * 1000 # in meters
    phi_1 = haver.convert_to_radian(start_point[0])
    lam_1 = haver.convert_to_radian(start_point[1])
    bearing_radian = haver.convert_to_radian(bearing)
    sigma = distance/radius
    #print(phi_1)    
    #print(lam_1)


    sin_phi2 = math.sin(phi_1) * math.cos(sigma) + math.cos(phi_1) * math.sin(sigma) * math.cos(bearing_radian)

    phi_2 = math.asin(sin_phi2)


    y = math.sin(bearing_radian) * math.sin(sigma) * math.cos(phi_1)
    x = math.cos(sigma) - math.sin(phi_1)* sin_phi2

    lam_2 = lam_1 + math.atan2(y,x)

    lat2 = haver.radian_to_degree(phi_2)
    lon2 = haver.radian_to_degree(lam_2)
    lon2 = (lon2  + 540)%360-180
    
    destination_result_dd = lat2, lon2 # in dd
    
    
    #print(destination_result)
    #final_bearing_result = haver.final_bearing(start_point,destination_result)
    if lat2 > 0:
        pol = "N"
    else: 
        pol = "S"
        lat2 = -1 * lat2
    if lon2 > 0:
        direction = "E"
    else:
        direction = "W"
        lon2 = -1 * lon2
    lat2_result = haver.dd_to_dms(lat2) # in dms
    lon2_result = haver.dd_to_dms(lon2) # in dms
    lat2_result_with_pol = lat2_result, pol
    lon_2_result_with_direction = lon2_result,direction

    destination_result = lat2_result_with_pol,lon_2_result_with_direction
    #print("desto ",destination_result)
    #print(lat2_result_with_pol)
    #print(lon_2_result_with_direction)
    
    #print("destination point is ",((haver.dd_to_dms(lat2),pol),(haver.dd_to_dms(lon2),direction )))
    #print("final_bearing is ", haver.final_bearing(start_point, destination_result_dd))
    final_bearing_result  = haver.final_bearing(start_point, destination_result_dd)
    
    result_to_displayed = destination_result, final_bearing_result
    #print(result_to_displayed)

    return result_to_displayed





#FOR TAB2
def calculate_destinaion_point(lat1_deg,lat1_min,lat1_sec,lat1_pol,lon1_deg,lon1_min,lon1_sec,lon1_dir,distance,bearing_deg,bearing_min,bearing_sec):
    lat1_dd = lat1_deg + (lat1_min/60) + (lat1_sec/3600)
    lon1_dd = lon1_deg + (lon1_min/60) + (lon1_sec/3600)

    bearing_dd = bearing_deg + (bearing_min/60) + (bearing_sec/3600)


    if lat1_pol == "S" or lat1_pol == "s":
        lat1_dd = -1 * lat1_dd
    if lon1_dir == "W" or lon1_dir == "w":
        lon1_dd = -1* lon1_dd

    startpoint = lat1_dd, lon1_dd 

    result = find_destination_point(startpoint,distance,bearing_dd)

    return result








