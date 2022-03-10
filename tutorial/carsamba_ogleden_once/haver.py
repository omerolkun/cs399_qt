import random
import math
import sys
point1 = 0,0
point2 = 0,0

R = 6371000 # in meters



# check the representation of the point. if the point is deg min sec ,the function return true
def check_degminsec(point):
    
    if point[0].__contains__('N') == True or point[0].__contains__('S') == True:
        return True
    else:
        return False


#if the point's representation is deg ming sec, the function converts it to decimal representation
#if the point is decimal, no action
def make_decimal(point):

    if check_degminsec(point) == False:
        point = float(point[0]), float(point[1])
        return point
    else:
        point_lat_lst = point[0].split(" ")
        point_long_lst = point[1].split(" ")

        point_lat_deg = int(point_lat_lst[0])
        point_lat_min = int(point_lat_lst[1])
        point_lat_sec = int(point_lat_lst[2][0:-1])
        point_lat_direction = point_lat_lst[2][-1]


        point_long_deg = int(point_long_lst[0])
        point_long_min = int(point_long_lst[1])
        point_long_sec = int(point_long_lst[2][0:-1])
        point_long_direction = point_long_lst[2][-1]

        result_lat  = point_lat_deg + (point_lat_min/60) + (point_lat_sec/3600)
        result_long = point_long_deg + (point_long_min/60) + (point_long_sec/3600)

        if point_lat_direction == "S":
            result_lat = -1 * result_lat
        
        if point_long_direction == "W":
            result_long = -1 * result_long

        result = (result_lat,result_long)

        return result

# it is using in bearings method 
def convert_to_radian(degree):
    return degree * (math.pi/180)

def calculate_distance(point1, point2):
    '''p1 = make_decimal(point1)
    p2 = make_decimal(point2)'''
    
    lat1 = point1[0]
    lat2 = point2[0]
    long1 = point1[1]
    long2 = point2[1]



    phase1 = lat1 * math.pi / 180 # radian value of latitude of point1
    phase2 = lat2 * math.pi / 180 # radian value of latitude of point2

    delta_lambda = (long2 - long1) * math.pi / 180 # difference of the longitudes of the points in radian
    delta_phase = (lat2 - lat1) * math.pi/180 #######

    #haversine formula
    #a = math.pow( math.sin(delta_phase/2),2) + math.cos(phase1) * math.cos(phase2) * math.pow( math.sin(delta_lambda/2),2)
    a = math.sin(delta_phase/2) * math.sin(delta_phase/2) + math.cos(phase1) * math.cos(phase2) * math.sin(delta_lambda/2) *math.sin(delta_lambda/2) 
    #sqrt_of_a = math.sqrt(a)
    # c = 2 * atan2(square root of a, square root of 1-a )

    #c = 2 * math.atan2(sqrt_of_a, math.sqrt(1-a))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))


    #distance formula is d = Radius of Earth * c 

    result = R * c
    
    #return result
    return (round(result/1000,0))



def dd_to_dms(value):
    degree = int(value)
    (minute_temp )= (value - (degree)) * 60
    minute = int(minute_temp)
    (seconds) = int((minute_temp-minute) * 60)
    
    return  (degree,minute,seconds)


def find_bearing(point1, point2): #parameters elements are in dd format
    lat1 = convert_to_radian(point1[0])
    lon1 = convert_to_radian(point1[1])
    lat2 = convert_to_radian(point2[0])
    lon2 = convert_to_radian(point2[1])

    diff_of_longs = (lon2 - lon1)

    x = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(diff_of_longs)) 
    y = math.sin(diff_of_longs) * math.cos(lat2)
    
    #formula
    teta = math.atan2(y,x)

    result = (teta * 180 / math.pi + 360 ) % 360 # converting to degree in this final step
    fbear = (teta*180/math.pi + 180)%360
    #print("the bearing is ",result)
    dms_version_bearing = dd_to_dms(result)
    #print(dms_version_bearing)
    return dd_to_dms(result) 


def final_bearing(point1,point2):
    result = find_bearing(point2,point1)
    result_temp  = list(result)
    result_temp[0] = (result_temp[0] + 180) % 360
    result = tuple(result_temp)
    return result
    
def calculate_midpoint(point1, point2):
    phi_1 = convert_to_radian( point1[0])
    lam_1 = convert_to_radian(point1[1])
    phi_2 = convert_to_radian(point2[0])
    lam_2 = convert_to_radian(point2[1])

    bx = math.cos(phi_2) * math.cos(lam_2- lam_1)
    by = math.cos(phi_2) * math.sin(lam_2-lam_1)
    

    phi_3 = math.atan2 ( math.sin(phi_1) + math.sin(phi_2) , math.sqrt ( (math.cos(phi_1) + bx) * (math.cos(phi_1) + bx ) + by * by))
    lam_3 = lam_1 + math.atan2(by , math.cos(phi_1) + bx)


    deg_lat =round( radian_to_degree(phi_3),3)
    deg_lon = round(radian_to_degree(lam_3),3)
    deg_lon = (deg_lon+540)%360-180
    


    if deg_lat < 0:
        pole = "S"
        dms_lat = dd_to_dms(-deg_lat)
    else:
        pole = "N"
        dms_lat = dd_to_dms(deg_lat)

    if deg_lon < 0:
        direction = "W"
        dms_lon = dd_to_dms(-deg_lon)
    else:
        direction = "E"
        dms_lon = dd_to_dms(deg_lon)
    
    result_lat = dms_lat,pole
    result_lon = dms_lon,direction
    return result_lat, result_lon

def radian_to_degree(value): # parameter is radian
    return value * 180 / math.pi


if __name__ == "__main__":

    '''
    #ask users to select representation type of the points
    option = input("DMS (0) / DD (1)   ")
    if option == "1":
        #taking the inputs
        lat1= input("Enter the latidute for point 1: ")
        lon1 = input("Enter the longitude for point 1: ")
        point1 = float(lat1), float(lon1)
        
        lat2= input("Enter the latitude for point 2: ")
        lon2 = input("Entert the longitude for point 2: ")
        point2 = float(lat2), float(lon2)
        
        print("---\nDistance" ,calculate_distance(point1,point2))
        print("Bearing :", find_bearing(point1,point2))
        print("Final bearing: ",final_bearing(point1,point2) ,"\n---" )

    elif option == "0":
        print("Enter the values for latitude of first point")
        degree_lat1, minute_lat1, seconds_lat1, pole_lat1 = input().split()

        print("Enter the values for longitude of first point")
        degree_lon1, minute_lon1, seconds_lon1, direction_lon1 = input().split()


        print("Enter the values for latitude of second point")
        degree_lat2, minute_lat2, seconds_lat2, pole_lat2 = input().split()

        print("Enter the values for longitude of second point")
        degree_lon2, minute_lon2, seconds_lon2, direction_lon2 = input().split()

        degree_lat1 = float(degree_lat1)
        minute_lat1 = float(minute_lat1)
        seconds_lat1 = float(seconds_lat1)

        
        degree_lat2 = float(degree_lat2)
        minute_lat2 = float(minute_lat2)
        seconds_lat2 = float(seconds_lat2)

        degree_lon1 = float(degree_lon1)
        minute_lon1 = float(minute_lon1)
        seconds_lon1 = float(seconds_lon1)


        degree_lon2 = float(degree_lon2)
        minute_lon2 = float(minute_lon2)
        seconds_lon2 = float(seconds_lon2)

        #dms to dd
        result_lat_point1 = round(degree_lat1 + (minute_lat1/60) + (seconds_lat1/3600) , 6)
        if pole_lat1 == "S" or pole_lat1 == "s":
            result_lat_point1 = -1 * result_lat_point1
        
        result_lon_point1 = round(degree_lon1 + (minute_lon1/60) + (seconds_lon1/3600),6)
        if direction_lon1 == "W" or direction_lon1 == "w":
            result_lon_point1 = -1 * result_lon_point1
        
        result_lat_point2 = round(degree_lat2 + (minute_lat2/60) + (seconds_lat2/3600) , 6)
        if pole_lat2 == "S" or pole_lat2 == "s":
            result_lat_point2 = -1 * result_lat_point2
        
        result_lon_point2 = round(degree_lon2 + (minute_lon2/60) + (seconds_lon2/3600),6)
        if direction_lon2 == "W" or direction_lon2 == "w":
            result_lon_point2 = -1 * result_lon_point2

        point1 = result_lat_point1,result_lon_point1 #dd version of point1
        point2 = result_lat_point2,result_lon_point2 #dd version of point2
        
        #print("point1 in degrees: ",point1)
        #print("point2 in degrees: ",point2)
        
        print("---\nDistance" ,calculate_distance(point1,point2))
        print("Bearing :", find_bearing(point1,point2))
        print("Final bearing: ",final_bearing(point1,point2) ,"\n---" )
    else:
        print("Invalid input")
        sys.exit("Program is terminated...")




    '''


    lat1 = round(random.uniform(-90,90),3)
    lon1 = round(random.uniform(-180,180),3)

    lat2 = round(random.uniform(-90,90),3)
    lon2 = round(random.uniform(-180,180),3)

    point1 = lat1, lon1
    point2 = lat2, lon2

    print("point1 :" , point1)
    print("point2 : ", point2)

    print( "---------\nDISTANCE: ", calculate_distance(point1,point2))
    print("Inital bearing: ",find_bearing(point1,point2))
    print("Final bearing : ", final_bearing(point1,point2))





    print("Mid point is ", calculate_midpoint(point1,point2))
