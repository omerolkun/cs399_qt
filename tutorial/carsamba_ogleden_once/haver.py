#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import math
import sys
point1 = 0,0
point2 = 0,0

R = 6371000 # in meters

def wrap90_helper(degree):
    if float(degree) >= -90 and float(degree) <= 90:
       return float(degree)
       
    x  = degree
    a = 90
    p = 360
    result = float ( float(4*a/p) * abs((((x-p/4)%p)+p)%p - p/2) - a )
   
    return result


def wrap180_helper(degree):
    if degree>=-180 and degree <= 180:
        return float(degree)
    x = degree
    a =180
    p=360
    return (((2 * a *x/p - p/2)%p)+p)%p - a

def dms_to_dd(deg,min,sec):
    result = deg + min/60 + sec/3600
    return result
# it is using in bearings method 
def convert_to_radian(degree):
    return degree * (math.pi/180)
def radian_to_degree(value): # parameter is radian
    return value * 180 / math.pi

def dd_to_dms(value):
    degree = int(value)
    (minute_temp )= (value - (degree)) * 60
    minute = int(minute_temp)
    (seconds) = int((minute_temp-minute) * 60)
    
    return  (degree,minute,seconds)


#tab3 functions 
def find_intersection_point(lat1,lon1,lat2,lon2,b1,b2):
    phi_1 = convert_to_radian(lat1)
    phi_2 = convert_to_radian(lat2)
    lambda_1 = convert_to_radian(lon1)
    lambda_2 = convert_to_radian(lon2)

    teta13 = convert_to_radian(b1)
    teta23 = convert_to_radian(b2)

    print("phi1 :",phi_1)
    print("phi2 " ,phi_2)
    print("lambda1 ",lambda_1)
    print("lambda2 ",lambda_2)
    print("teta13 ",teta13)
    print("teta23 ",teta23)

    delta_phi = phi_2 - phi_1
    delta_lambda = lambda_2 - lambda_1

    result_list  = []
    sigma12 = 2 * math.asin(math.sqrt(math.sin(delta_phi/2) * math.sin(delta_phi/2) + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda/2) * math.sin(delta_lambda/2)))
    print(sys.float_info.epsilon)
    if abs(sigma12)  < sys.float_info.epsilon:
        result_list.append("coendiets")
        return result_list
    

    cos_teta_a = (math.sin(phi_2) - math.sin(phi_1) * math.cos(sigma12)) / (math.sin(sigma12) *  math.cos(phi_1))
    cos_teta_b = (math.sin(phi_1) - math.sin(phi_2) * math.cos(sigma12)) / (math.sin(sigma12) * math.cos(phi_2));
     

    teta_a = math.acos( min(max(cos_teta_a, -1),1))
    teta_b = math.acos (min(max(cos_teta_b, -1),1))

    if math.sin(lambda_2 - lambda_1) > 0:
        teta12 = teta_a
    else: 
        teta12 = 2 * math.pi - teta_a

    if math.sin(lambda_2 - lambda_1) > 0:
        teta21 = 2 * math.pi - teta_b
    else:
        teta21 = teta_b
    
    alfa_1 = teta13 - teta12
    alfa_2 = teta21 - teta23
    


    if (math.sin(alfa_1) == 0 and math.sin(alfa_2) == 0):
        result_list.append("B")
        return
    
    if (math.sin(alfa_1) * math.sin(alfa_2) < 0) :
        result_list.append("[ambigious]")
        return result_list


    
    cos_alfa3 = -1 * math.cos(alfa_1) * math.cos(alfa_2) + math.sin(alfa_1) * math.sin(alfa_2) * math.cos(sigma12)
    sigma13  =  math.atan2( math.sin(sigma12) * math.sin(alfa_1)* math.sin(alfa_2), math.cos(alfa_2) + math.cos(alfa_1)*cos_alfa3)

    
    phi_3 = math.asin(min(max(math.sin(phi_1)* math.cos(sigma13) + math.cos(phi_1) * math.sin(sigma13) * math.cos(teta13), -1),1))

    delta_lambda13 = math.atan2(math.sin(teta13) * math.sin(sigma13) * math.cos(phi_1), math.cos(sigma13) - math.sin(phi_1)* math.sin(phi_3))

    lambda_3 = lambda_1 + delta_lambda13

    result_lat = radian_to_degree(phi_3)
    result_lon = radian_to_degree(lambda_3)
    if result_lat < 0:
        result_lat = result_lat * -1
        pole = "S"
    else:
        pole = "N"

    if result_lon < 0:
        result_lon = -1 * result_lon
        direction = "W"
    else:
        direction = "E"
    dms_lat = (dd_to_dms(result_lat) , pole)
    dms_lon = (dd_to_dms(result_lon)) ,direction
    print("result lat = ",dms_lat)
    print("result lon = ",dms_lon)
    point = dms_lat, dms_lon
    result_list.append(dms_lat)
    result_list.append(dms_lon)
    print("result point" , point)
    print("result_list is ",result_list)
    return result_list











# calculate distance in parameters dms , degree
def calculate_distance_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min, lon1_sec,lat2_deg,lat2_min,lat2_sec, lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir):
    lat1_dd = lat1_deg + (lat1_min/60) + (lat1_sec/3600)
    lon1_dd = lon1_deg + (lon1_min/60) + (lon1_sec/3600)
    
    lat2_dd = lat2_deg + (lat2_min/60) + (lat2_sec/3600)
    lon2_dd = lon2_deg + (lon2_min/60) + (lon2_sec/3600)

   
    #it sets the negative possibilies of values for dd format
    if lat1_pole == 'S' or lat1_pole == 's':
        lat1_dd = -1 * lat1_dd
    if lon1_dir == 'W' or lon1_dir == 'w':
        lon1_dd = -1 * lon1_dd
    if lat2_pole == 'S' or lat2_pole == 's':
        lat2_dd = -1 * lat2_dd
    if lon2_dir == 'W' or lon2_dir == 'w':
        lon2_dd = -1 * lon2_dd








    #final results for point1 and point2    
    point1 = lat1_dd, lon1_dd
    point2 = lat2_dd, lon2_dd



    return calculate_distance(point1,point2)
# inputs are in dms format
def calculate_azamith_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min, lon1_sec,lat2_deg,lat2_min,lat2_sec, lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir):
    lat1_dd = lat1_deg + (lat1_min/60) + (lat1_sec/3600)
    lon1_dd = lon1_deg + (lon1_min/60) + (lon1_sec/3600)
    lat2_dd = lat2_deg + (lat2_min/60) + (lat2_sec/3600)
    lon2_dd = lon2_deg + (lon2_min/60) + (lon2_sec/3600)

    #negative or not
    if lat1_pole == 'S' or lat1_pole == 's':
        lat1_dd = -1 * lat1_dd
    if lon1_dir == 'W' or lon1_dir == 'w':
        lon1_dd = -1 * lon1_dd
    if lat2_pole == 'S' or lat2_pole == 's':
        lat2_dd = -1 * lat2_dd
    if lon2_dir == 'W' or lon2_dir == 'w':
        lon2_dd = -1 * lon2_dd

    #final results for point1 and point2    
    point1 = lat1_dd,lon1_dd
    point2 = lat2_dd, lon2_dd



    point1 = lat1_dd,lon1_dd
    point2 = lat2_dd, lon2_dd

    result = find_bearing(point1,point2)    
    return result


def calculate_final_bearing_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min, lon1_sec,lat2_deg,lat2_min,lat2_sec, lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir):
    lat1_dd = lat1_deg + (lat1_min/60) + (lat1_sec/3600)
    lon1_dd = lon1_deg + (lon1_min/60) + (lon1_sec/3600)
    lat2_dd = lat2_deg + (lat2_min/60) + (lat2_sec/3600)
    lon2_dd = lon2_deg + (lon2_min/60) + (lon2_sec/3600)

    #negative or not
    if lat1_pole == 'S' or lat1_pole == 's':
        lat1_dd = -1 * lat1_dd
    if lon1_dir == 'W' or lon1_dir == 'w':
        lon1_dd = -1 * lon1_dd
    if lat2_pole == 'S' or lat2_pole == 's':
        lat2_dd = -1 * lat2_dd
    if lon2_dir == 'W' or lon2_dir == 'w':
        lon2_dd = -1 * lon2_dd

    #final results for point1 and point2    
    point1 = lat1_dd,lon1_dd
    point2 = lat2_dd, lon2_dd

    point1 = lat1_dd,lon1_dd
    point2 = lat2_dd, lon2_dd
    
    result = final_bearing(point1,point2)
    return result

def calculate_mid_point_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min, lon1_sec,lat2_deg,lat2_min,lat2_sec, lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir):
    lat1_dd = lat1_deg + (lat1_min/60) + (lat1_sec/3600)
    lon1_dd = lon1_deg + (lon1_min/60) + (lon1_sec/3600)
    lat2_dd = lat2_deg + (lat2_min/60) + (lat2_sec/3600)
    lon2_dd = lon2_deg + (lon2_min/60) + (lon2_sec/3600)

    #negative or not
    if lat1_pole == 'S' or lat1_pole == 's':
        lat1_dd = -1 * lat1_dd
    if lon1_dir == 'W' or lon1_dir == 'w':
        lon1_dd = -1 * lon1_dd
    if lat2_pole == 'S' or lat2_pole == 's':
        lat2_dd = -1 * lat2_dd
    if lon2_dir == 'W' or lon2_dir == 'w':
        lon2_dd = -1 * lon2_dd

    #final results for point1 and point2    
    point1 = lat1_dd,lon1_dd
    point2 = lat2_dd, lon2_dd

    result = calculate_midpoint(point1,point2)
    return result

#rest functions are not explicitly related to tab2 in qt 
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

'''    print("point1 :" , point1)
    print("point2 : ", point2)

    print( "---------\nDISTANCE: ", calculate_distance(point1,point2))
    print("Inital bearing: ",find_bearing(point1,point2))
    print("Final bearing : ", final_bearing(point1,point2))





    print("Mid point is ", calculate_midpoint(point1,point2))

'''



    #print(calculate_distance_tab2(10,15,23,50,52,30,80,20,33,150,50,1))


