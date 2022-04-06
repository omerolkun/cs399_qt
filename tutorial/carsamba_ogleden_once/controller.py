#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from curses import A_ALTCHARSET
import sys
from tokenize import Double
from PySide2 import QtWidgets,QtGui
from ui import Ui_MainWindow
import math
import random
from haver import calculate_midpoint, convert_to_radian, find_bearing, radian_to_degree, dd_to_dms, calculate_distance,final_bearing, calculate_distance_tab2,calculate_azamith_tab2,calculate_final_bearing_tab2,calculate_mid_point_tab2,find_intersection_point,dms_to_dd
from dest_and_final_bearing import calculate_destinaion_point, find_destination_point
from PyQt5.QtWidgets import QMessageBox


class ModiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ModiWindow,self).__init__()
        self.setupUi(self)
        self.invalid = False


        
        #set values for comboboxes

        #for tab1
        self.lat1_pole_tab1.addItems(["N","S"])
        self.lon1_direction_tab1.addItems(["E","W"])
        self.lat2_pole_tab1.addItems(["N","S"])
        self.lon2_direction_tab1.addItems(["E","W"])

        self.point1_lat_pole.addItems(["N","S"])
        self.point1_lon_dir.addItems(["E","W"])
        self.point2_lat_pole.addItems(["N","S"])
        self.point2_lon_dir.addItems(["E","W"])
        self.start_point_lat_combo.addItems(["N","S"])
        self.start_point_lon_combo.addItems(["E","W"])
        
        self.point1_pole_tab3.addItems(["N","S"])
        self.point1_direction_tab3.addItems(["E","W"])
        self.point2_pole_tab3.addItems(["N","S"])
        self.point2_direction_tab3.addItems(["E","W"])

        #validator for lat and lon for tab1's inputs 
        lat_validator = QtGui.QDoubleValidator(0,90,4)
        lat_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        lon_validator = QtGui.QDoubleValidator(0,180,8)
        lon_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        

        
        #set validators for lineedit inputs 
        self.lat1.setValidator( lat_validator)
        self.lon1.setValidator( lon_validator )
        self.lat2.setValidator( lat_validator )
        self.lon2.setValidator( lon_validator )
        self.start_lat_lineedit.setValidator (lat_validator)
        self.start_longitude_lineedit.setValidator(lon_validator)
        self.bearing_lineEdit.setValidator(lon_validator)

        
        #validator for tab2 is lineedits - first part
        lat_deg_validator = QtGui.QIntValidator(0,90,self)
        #lat_deg_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        lon_deg_validator = QtGui.QIntValidator(0,180,self)
        #lon_deg_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        min_validator = QtGui.QIntValidator(0,60,self)
        #min_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        sec_validator = QtGui.QDoubleValidator(0,60,0)
        sec_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        
        #set validators for lineedit inputs - first part
        self.lat1_deg_lineedit.setValidator( lat_deg_validator)
        self.lat1_min_lineedit.setValidator( min_validator )
        self.lat1_sec_lineedit.setValidator( sec_validator )
        self.lon1_deg_lineedit.setValidator( lon_deg_validator)
        self.lon1_min_lineedit.setValidator( min_validator )
        self.lon1_sec_lineedit.setValidator( sec_validator )
        self.lat2_deg_lineedit.setValidator( lat_deg_validator )
        self.lat2_min_lineedit.setValidator( min_validator )
        self.lat2_sec_lineedit.setValidator( sec_validator )
        self.lon2_deg_lineedit.setValidator( lon_deg_validator )
        self.lon2_min_lineedit.setValidator( min_validator )
        self.lon2_sec_lineedit.setValidator( sec_validator )

        #set validators for lineedit inputs - second part 
        self.startpoint_lat_deg_lineedit_tab2.setValidator(lat_deg_validator)
        self.startpoint_lat_min_lineedit_tab2.setValidator(min_validator)
        self.startpoint_lat_min_lineedit_tab2.setValidator(sec_validator)
        self.startpoint_lon_deg_lineedit_tab2.setValidator(lon_deg_validator)
        self.startpoint_lon_min_lineedit_tab2.setValidator(min_validator)
        self.startpoint_lon_sec_lineedit_tab2.setValidator(sec_validator)


        #set validators for lineedit inputs - tab3 - intersection point
        #dd variables
        self.lat1_dd_tab3.setValidator(lat_validator)
        self.lat2_dd_tab3.setValidator(lat_validator)
        self.lon1_dd_tab3.setValidator(lon_validator)
        self.lon2_dd_tab3.setValidator(lon_validator)
        self.bearing1_dd_tab3.setValidator(lon_validator)
        self.bearing2_dd_tab3.setValidator(lon_validator)
        #dms variables
        self.lat1_deg_dms_tab3.setValidator(lat_deg_validator)
        self.lat1_min_dms_tab3.setValidator(min_validator)
        self.lat1_sec_dms_tab3.setValidator(sec_validator)
        self.lon1_deg_dms_tab3.setValidator(lon_deg_validator)
        self.lon1_min_dms_tab3.setValidator(min_validator)
        self.lon1_sec_dms_tab3.setValidator(sec_validator)
        self.lat2_deg_dms_tab3.setValidator(lat_deg_validator)
        self.lat2_min_dms_tab3.setValidator(min_validator)
        self.lat2_sec_dms_tab3.setValidator(sec_validator)
        self.lon2_deg_dms_tab3.setValidator(lon_deg_validator)
        self.lon2_min_dms_tab3.setValidator(min_validator)
        self.lon2_sec_dms_tab3.setValidator(sec_validator)
        self.bearing1_deg_dms_tab3.setValidator(lon_deg_validator)
        self.bearing1_min_dms_tab3.setValidator(min_validator)
        self.bearing1_sec_dms_tab3.setValidator(sec_validator)
        self.bearing2_deg_dms_tab3.setValidator(lon_deg_validator)
        self.bearing2_min_dms_tab3.setValidator(min_validator)
        self.bearing2_sec_dms_tab3.setValidator(sec_validator)




        #default values for tab1 
        self.lat1.setText(str(round(random.uniform(0,90),3)))
        self.lon1.setText(str(round(random.uniform(0,180),3)))
        self.lat2.setText(str(round(random.uniform(0,90),3)))
        self.lon2.setText(str(round(random.uniform(0,180),3)))
        self.start_lat_lineedit.setText(str(round(random.uniform(0,90),3)))
        self.start_longitude_lineedit.setText(str(round(random.uniform(0,180),3)))
        self.bearing_lineEdit.setText(str(round(random.uniform(0,180),3)))
        self.distance_lineEdit.setText(str(round(random.uniform(0,3400),3)))

        #default values for tab2 
        self.lat1_deg_lineedit.setText(str(round(random.uniform(0,90))))
        self.lat1_min_lineedit.setText(str(round(random.uniform(0,59))))
        self.lat1_sec_lineedit.setText(str(round(random.uniform(0,59),0)))
        self.lon1_deg_lineedit.setText(str(round(random.uniform(0,180))))
        self.lon1_min_lineedit.setText(str(round(random.uniform(0,59))))
        self.lon1_sec_lineedit.setText(str(round(random.uniform(0,59),0)))
        self.lat2_deg_lineedit.setText(str(round(random.uniform(0,90))))
        self.lat2_min_lineedit.setText(str(round(random.uniform(0,59))))
        self.lat2_sec_lineedit.setText(str(round(random.uniform(0,59),0)))
        self.lon2_deg_lineedit.setText(str(round(random.uniform(0,180))))
        self.lon2_min_lineedit.setText(str(round(random.uniform(0,59))))
        self.lon2_sec_lineedit.setText(str(round(random.uniform(0,59),0)))

        self.startpoint_lat_deg_lineedit_tab2.setText(str(round(random.uniform(0,90))))
        self.startpoint_lat_min_lineedit_tab2.setText(str(round(random.uniform(0,59))))
        self.startpoint_lat_sec_lineedit_tab2.setText(str(round(random.uniform(0,59),0)))
        self.startpoint_lon_deg_lineedit_tab2.setText(str(round(random.uniform(0,180))))
        self.startpoint_lon_min_lineedit_tab2.setText(str(round(random.uniform(0,59))))
        self.startpoint_lon_sec_lineedit_tab2.setText(str(round(random.uniform(0,59),0)))

        self.bearing_deg_lineedit_tab2.setText(str(round(random.uniform(0,90))))
        self.bearing_min_lineedit_tab2.setText(str(round(random.uniform(0,59))))
        self.bearing_sec_lineedit_tab2.setText(str(round(random.uniform(0,59),0)))
        
        self.distance_lineedit_tab2.setText(str(round(random.uniform(0,3500),0)))

        #default values for tab3
        #dd variables
        self.lat1_dd_tab3.setText(str(round(random.uniform(-90,90))))
        self.lat2_dd_tab3.setText(str(round(random.uniform(-90,90))))
        self.lon1_dd_tab3.setText(str(round(random.uniform(-180,180))))
        self.lon2_dd_tab3.setText(str(round(random.uniform(-180,180))))
        self.bearing1_dd_tab3.setText(str(round(random.uniform(-180,180))))
        self.bearing2_dd_tab3.setText(str(round(random.uniform(-180,180))))
        #dms variables
        self.lat1_deg_dms_tab3.setText(str(round(random.uniform(0,90))))
        self.lat1_min_dms_tab3.setText(str(round(random.uniform(0,59))))
        self.lat1_sec_dms_tab3.setText(str(round(random.uniform(0,59),0)))
        self.lon1_deg_dms_tab3.setText(str(round(random.uniform(0,180))))
        self.lon1_min_dms_tab3.setText(str(round(random.uniform(0,59))))
        self.lon1_sec_dms_tab3.setText(str(round(random.uniform(0,59),0)))
        
        self.lat2_deg_dms_tab3.setText(str(round(random.uniform(0,90))))
        self.lat2_min_dms_tab3.setText(str(round(random.uniform(0,59))))
        self.lat2_sec_dms_tab3.setText(str(round(random.uniform(0,59),0)))
        self.lon2_deg_dms_tab3.setText(str(round(random.uniform(0,180))))
        self.lon2_min_dms_tab3.setText(str(round(random.uniform(0,59))))
        self.lon2_sec_dms_tab3.setText(str(round(random.uniform(0,59),0)))
        
        self.bearing1_deg_dms_tab3.setText(str(round(random.uniform(0,180))))
        self.bearing1_min_dms_tab3.setText(str(round(random.uniform(0,59))))
        self.bearing1_sec_dms_tab3.setText(str(round(random.uniform(0,59),0)))
        self.bearing2_deg_dms_tab3.setText(str(round(random.uniform(0,180))))
        self.bearing2_min_dms_tab3.setText(str(round(random.uniform(0,59))))
        self.bearing2_sec_dms_tab3.setText(str(round(random.uniform(0,59),0)))
        #buttons for tab1
        self.calculate_button.clicked.connect(self.find_distance)
        self.calculate_button.clicked.connect(self.find_azamith)
        self.calculate_button.clicked.connect(self.find_final_bearing)
        self.calculate_button.clicked.connect(self.find_midpoint)
        self.calculate_dest_bearing_button.clicked.connect(self.calculate_destination_point)
        
        #buttons for tab2
        self.calculate_button_tab2.clicked.connect(self.display_distance_tab2)
        self.calculate_button_tab2.clicked.connect(self.display_azamith_tab2)
        self.calculate_button_tab2.clicked.connect(self.display_final_bearing_tab2)
        self.calculate_button_tab2.clicked.connect(self.display_midpoint_tab2)
        self.calculate_button_destination_point_tab2.clicked.connect(self.display_endpoint_and_bearing_tab2)
        
        #buttons for tab3
        self.calculate_inter_point_button.clicked.connect(self.display_intersection_point_dd)
        self.calculate_intersection_dms_button.clicked.connect(self.display_intersection_point_dms)
#for tab1
    def wrap90(self):
        if self.lat1.text() == "":
            self.lat1.setText("0")
        if self.lat2.text() == "":
            self.lat2.setText("0")
        if self.start_lat_lineedit.text() == "":
            self.start_lat_lineedit.setText("0")
        lat1 = wrap90_helper(float(self.lat1.text()))
        lat2 = wrap90_helper(float(self.lat2.text()))
        start_lat = wrap90_helper(float(self.start_lat_lineedit.text()))
        return lat1,lat2,start_lat

#for tab1
    def wrap180(self):
        if self.lon1.text() == "":
            self.lon1.setText("0")
        if self.lon2.text() == "":
            self.lon2.setText("0")
        if self.start_longitude_lineedit.text() == "":
            self.start_longitude_lineedit.setText("0")
        if self.bearing_lineEdit.text() == "":
            self.bearing_lineEdit.setText("0")

        lon1 = wrap180_helper(float(self.lon1.text()))
        lon2 = wrap180_helper(float(self.lon2.text()))
        start_lon = wrap180_helper(float(self.start_longitude_lineedit.text()))
        azamith = wrap180_helper(float(self.bearing_lineEdit.text()))
        return lon1,lon2,start_lon,azamith
    
#for tab2
    def wrap90_tab2_part1(self):
        degree = float(self.lat1_deg_lineedit.text())
        degree2 = float(self.lat2_deg_lineedit.text())
        print("wrap_90_part1_tab2 is called ")
        
        result = wrap90_helper(degree)
        result2 = wrap90_helper(degree2)
        print("result = ", result)
        return result, result2


    def wrap180_tab2_par1(self):
        degree = float(self.lon1_deg_lineedit.text())
        degree2 = float(self.lon2_deg_lineedit.text())
        result = wrap180_helper(degree)
        result2 = wrap180_helper(degree2)
        return result, result2


    def wrap90_tab2_part2(self):
        degree = float(self.startpoint_lat_deg_lineedit_tab2.text())
        return wrap90_helper(degree)
    
    def wrap180_tab2_part2(self):
        degree = float(self.startpoint_lon_deg_lineedit_tab2.text())
        return wrap180_helper(degree)

    def wrap180_tab2_bearing(self):
        degree = float(self.bearing_deg_lineedit_tab2)
        return wrap180_helper(degree)


#functions for tab1
    def find_distance(self):
       

        lat1 = float(self.lat1.text())
        lat2 = float(self.lat2.text())
        lon1 = float(self.lon1.text())
        lon2 = float(self.lon2.text())
        point1 = lat1, lon1
        point2 = lat2, lon2

        flip = 0 
        warning_list = []
        print("lat1 = ",lat1)
        print("lat2 = ",lat2)
        if lat1 > 90 or lat1 < 0 or lat2 > 90 or lat2 < 0:
            flip = flip + 1

            warning_list.append("Latitudes must be in the range from 0 to 90")
        if lon1 > 180 or lon1 < 0 or lon2 > 180 or lon2 < 0:
            flip = flip + 1 
            warning_list.append("Longitudes must be in the range from 0 to 180")
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setIcon(QMessageBox.Critical)

            msg.setText(errorko)
            msg.exec_()
            return
        self.invalid == False
        result = calculate_distance(point1,point2) # comes from haver.py
        #set the label
        self.label_2.setText(str(result))
        

    
    def find_azamith(self):  # azamith means initial bearing
        degree_sign = u"\N{DEGREE SIGN}"    
        lat1 = float(self.lat1.text())
        lat2 = float(self.lat2.text())
        lon1 = float(self.lon1.text())
        lon2 = float(self.lon2.text())


        point1 = lat1, lon1
        point2 = lat2, lon2
        flip = 0 
        warning_list = []
        if lat1 > 90 or lat1 < 0 or lat2 > 90 or lat2 < -0:
            flip = flip + 1
        if lon1 > 180 or lon1 < 0 or lon2 > 180 or lon2 < 0:
            flip = flip + 1 
        if flip > 0:
            return    
        
        result = find_bearing(point1,point2)
        #degree min sec
        result = str(result[0]) + degree_sign + " " + str(result[1]) + "\' " + str(result[2]) + "\'\'" 

        #set the label

        self.label_value_azamith.setText(result)

        
    
    def find_final_bearing(self): 
        degree_sign = u"\N{DEGREE SIGN}"
        lat1 = float(self.lat1.text())
        lon1 = float(self.lon1.text())
        lat2 = float(self.lat2.text())
        lon2 = float(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2

        flip = 0 
        warning_list = []
        if lat1 > 90 or lat1 < 0 or lat2 > 90 or lat2 < 0:
            flip = flip + 1
        if lon1 > 180 or lon1 < 0 or lon2 > 180 or lon2 < 0:
            flip = flip + 1 
        if flip > 0:
            return

        result = final_bearing(point1,point2)
        
        #degree min sec
        result = str(result[0]) + degree_sign + " " + str(result[1]) + "\' " + str(result[2]) + "\'\'" 
        #set label
        self.final_bearing_label.setText(result)


    def find_midpoint(self):
        degree_sign = u"\N{DEGREE SIGN}"          
        lat1 = float(self.lat1.text())
        lon1 = float(self.lon1.text())
        lat2 = float(self.lat2.text())
        lon2 = float(self.lon2.text())
        point1 = lat1, lon1
        point2 = lat2, lon2

        flip = 0 
        warning_list = []
        if lat1 > 90 or lat1 < 0 or lat2 > 90 or lat2 < 0:
            flip = flip + 1
            
        if lon1 > 180 or lon1 < 0 or lon2 > 180 or lon2 < 0:
            flip = flip + 1 
            
        if flip > 0:
            return

        result = calculate_midpoint(point1,point2)

        mid_lat = result[0]
        mid_lon = result[1]
        
        result = str(mid_lat[0][0]) +degree_sign + " "+ str(mid_lat[0][1]) + "\'" + str(mid_lat[0][2]) + "\'\' , " + str(mid_lat[1]) + "  " + str(mid_lon[0][0]) +degree_sign + " "+ str(mid_lon[0][1]) + "\'" + str(mid_lon[0][2]) + "\'\' " + str(mid_lon[1])
        self.midpoint_value_label.setText(result)
        
    ### tab1 second part ###
    def calculate_destination_point(self):
      
        degree_sign = u"\N{DEGREE SIGN}"
        start_lat = float(self.start_lat_lineedit.text())
        start_lon = float(self.start_longitude_lineedit.text())
        distance = float(self.distance_lineEdit.text()) # in km
        azamith  = float(self.bearing_lineEdit.text()) # in dd

        start_point = start_lat , start_lon
        
        flip = 0 
        warning_list = []
        if start_lat > 90 or start_lat < -90 :
            flip = flip + 1
            warning_list.append("Latitude must be in the range from -90 to 90")
        if start_lon > 180 or start_lon < -180:
            flip = flip + 1 
            warning_list.append("Longitude must be in the range from -180 to 180")
        if azamith < -180 or azamith > 180:
            flip = flip + 1
            warning_list.append("Azamith must be in the range from -180 to 180")
        if distance > 6371 or distance < 0:
            flip = flip + 1
            warning_list.append("Distance must be in the range from 0 to 6371 km")
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setIcon(QMessageBox.Critical)

            msg.setText(errorko)
            msg.exec_()
            return


        x = find_destination_point(start_point, distance, azamith)
        

        destination_point_tuple = x[0]
        destination_lat_tuple = x[0][0]
        destination_lat_dms = x[0][0][0]
        destination_lat_pole = x[0][0][1]
        destination_lon_tuple = x[0][1]
        destination_lon_dms = x[0][1][0]
        destination_lon_direction = x[0][1][1]

        final_bearing_part = x[1]
        fbearing_deg = x[1][0]
        fbearing_min = x[1][1]
        fbearing_sec = x[1][2]

        result_destination_point = str(destination_lat_dms[0]) + degree_sign + " " + str(destination_lat_dms[1]) + "\'" + str(destination_lat_dms[2]) + "\'\' " + destination_lat_pole +  ",  " + str(destination_lon_dms[0]) + degree_sign+ " "+str(destination_lon_dms[1]) + "\'" + str(destination_lon_dms[2]) + "\'\' " + destination_lon_direction
        result_fbearing = str(fbearing_deg) + degree_sign + " " + str(fbearing_min) + "\'" + str(fbearing_sec) + "\'\'"
        self.destination_point_value_label.setText(result_destination_point)
        self.final_bearing_value_label.setText(result_fbearing)

    #functions for tab2

    def display_distance_tab2(self):
        self.invalid = False
        lat1_deg = float(self.lat1_deg_lineedit.text())
        lat1_min = float(self.lat1_min_lineedit.text())
        lat1_sec = float(self.lat1_sec_lineedit.text())
        lon1_deg = float(self.lon1_deg_lineedit.text())
        lon1_min = float(self.lon1_min_lineedit.text())
        lon1_sec = float(self.lon1_sec_lineedit.text())
        lat2_deg = float(self.lat2_deg_lineedit.text())
        lat2_min = float(self.lat2_min_lineedit.text())
        lat2_sec = float(self.lat2_sec_lineedit.text())
        lon2_deg = float(self.lon2_deg_lineedit.text())
        lon2_min = float(self.lon2_min_lineedit.text())
        lon2_sec = float(self.lon2_sec_lineedit.text())
        
        lat1_pole = self.point1_lat_pole.currentText()
        lon1_dir = self.point1_lon_dir.currentText()
        lat2_pole = self.point2_lat_pole.currentText()
        lon2_dir = self.point2_lon_dir.currentText()

        flip = 0 # if it is 0 , all inputs are valid
        warning_list = []
        if lat1_deg < 0 or lat1_deg > 90 or lat2_deg < 0 or lat2_deg > 90:
            flip = flip + 1
            warning_list.append("Latitudes degrees must be in the range from 0 to 90")
        if lon1_deg < 0 or lon1_deg > 180 or lon2_deg < 0 or lon2_deg > 180:
            flip = flip + 1
            warning_list.append("Longitudes must be in the range from 0 to 180")
        if lat1_min > 59 or lon1_min > 59 or lat2_min >59 or lon2_min > 59:
            flip = flip + 1
            warning_list.append("Minutes must be in 0-59")
            
        if lat1_sec > 59 or lon1_sec > 59 or lat2_sec > 59 or lon2_sec > 59:
            flip = flip + 1
            warning_list.append("Seconds must be in 0-59")
        
        if flip > 0:
            errorko = ""
            for item in warning_list:
                errorko = errorko + item + "\n"
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setIcon(QMessageBox.Critical)

            msg.setText(errorko)
            msg.exec_()
            return

 
        distance = calculate_distance_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min,lon1_sec,lat2_deg,lat2_min,lat2_sec,lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir)

        self.distance_value_label.setText(str(distance))


    def display_azamith_tab2(self):
        degree_sign = u"\N{DEGREE SIGN}"

        lat1_deg = float(self.lat1_deg_lineedit.text())
        lat1_min = float(self.lat1_min_lineedit.text())
        lat1_sec = float(self.lat1_sec_lineedit.text())
        lon1_deg = float(self.lon1_deg_lineedit.text())
        lon1_min = float(self.lon1_min_lineedit.text())
        lon1_sec = float(self.lon1_sec_lineedit.text())
        lat2_deg = float(self.lat2_deg_lineedit.text())
        lat2_min = float(self.lat2_min_lineedit.text())
        lat2_sec = float(self.lat2_sec_lineedit.text())
        lon2_deg = float(self.lon2_deg_lineedit.text())
        lon2_min = float(self.lon2_min_lineedit.text())
        lon2_sec = float(self.lon2_sec_lineedit.text())

        lat1_pole = self.point1_lat_pole.currentText()
        lon1_dir = self.point1_lon_dir.currentText()
        lat2_pole = self.point2_lat_pole.currentText()
        lon2_dir = self.point2_lon_dir.currentText()

        flip = 0 
        warning_list = []
        if lat1_deg > 90 or lat1_deg < 0 or lat2_deg > 90 or lat2_deg < 0:
            flip = flip + 1
            warning_list.append("Latitudes must be in the range from 0 to 90")
        if lon1_deg > 180 or lon1_deg < 0 or lon2_deg > 180 or lon2_deg < 0:
            flip = flip + 1 
            warning_list.append("Longitudes must be in the range from 0 to 180")
        if lat1_min > 59 or lat1_min < 0 or lat2_min > 59 or lat2_min < 0:
            flip = flip + 1 
            warning_list.append("Minuasdastes must be in the range from 0 to 59")
        if lat1_sec > 59 or lat1_sec < 0 or lat2_sec > 59 or lat2_sec < 0:
            flip = flip + 1
            warning_list.append("Seconds must be in the range from 0 to 59")
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            #msg = QMessageBox()
            #msg.setWindowTitle("Invalid Input")
            #msg.setIcon(QMessageBox.Critical)

            #msg.setText(errorko)
            #msg.exec_()
            return

        azamith = calculate_azamith_tab2(lat1_deg, lat1_min,lat1_sec,lon1_deg,lon1_min,lon1_sec,lat2_deg,lat2_min,lat2_sec,lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir)
        deg = str(azamith[0])
        minu = str(azamith[1])
        seco = str(azamith[2])
        toLabel = deg + " " + degree_sign  + " " + minu + "\' " + seco + " \'\'" 
        self.bearing_value_label.setText(toLabel)



    def display_final_bearing_tab2(self):
        degree_sign = u"\N{DEGREE SIGN}"

        lat1_deg = float(self.lat1_deg_lineedit.text())
        lat1_min = float(self.lat1_min_lineedit.text())
        lat1_sec = float(self.lat1_sec_lineedit.text())
        lon1_deg = float(self.lon1_deg_lineedit.text())
        lon1_min = float(self.lon1_min_lineedit.text())
        lon1_sec = float(self.lon1_sec_lineedit.text())
        lat2_deg = float(self.lat2_deg_lineedit.text())
        lat2_min = float(self.lat2_min_lineedit.text())
        lat2_sec = float(self.lat2_sec_lineedit.text())
        lon2_deg = float(self.lon2_deg_lineedit.text())
        lon2_min = float(self.lon2_min_lineedit.text())
        lon2_sec = float(self.lon2_sec_lineedit.text())
        lat1_pole = self.point1_lat_pole.currentText()
        lon1_dir = self.point1_lon_dir.currentText()
        lat2_pole = self.point2_lat_pole.currentText()
        lon2_dir = self.point2_lon_dir.currentText()
        flip = 0 
        warning_list = []
        if lat1_deg > 90 or lat1_deg < 0 or lat2_deg > 90 or lat2_deg < 0:
            flip = flip + 1
            warning_list.append("Latitudes must be in the range from 0 to 90")
        if lon1_deg > 180 or lon1_deg < 0 or lon2_deg > 180 or lon2_deg < 0:
            flip = flip + 1 
            warning_list.append("Longitudes must be in the range from 0 to 180")
        if lat1_min > 59 or lat1_min < 0 or lat2_min > 59 or lat2_min < 0:
            flip = flip + 1 
            warning_list.append("Minutes must be in the range from 0 to 59")
        if lat1_sec > 59 or lat1_sec < 0 or lat2_sec > 59 or lat2_sec < 0:
            flip = flip + 1
            warning_list.append("Seconds must be in the range from 0 to 59")
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            #msg = QMessageBox()
            #msg.setWindowTitle("Invalid Input")
            #msg.setIcon(QMessageBox.Critical)

            #msg.setText(errorko)
            #msg.exec_()
            return        
        result = calculate_final_bearing_tab2(lat1_deg, lat1_min,lat1_sec,lon1_deg,lon1_min,lon1_sec,lat2_deg,lat2_min,lat2_sec,lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir)
        degree = str(result[0])
        minute = str(result[1])
        sec = str(result[2])
        print(type(degree))
        toLabel = degree + " " + degree_sign + " " + minute + "\' "+sec + " \'\'"
        self.final_bearing_value_tab2_label.setText(toLabel)

    def display_midpoint_tab2(self):
        degree_sign = u"\N{DEGREE SIGN}"
        lat1_deg = float(self.lat1_deg_lineedit.text())
        lat1_min = float(self.lat1_min_lineedit.text())
        lat1_sec = float(self.lat1_sec_lineedit.text())
        lon1_deg = float(self.lon1_deg_lineedit.text())
        lon1_min = float(self.lon1_min_lineedit.text())
        lon1_sec = float(self.lon1_sec_lineedit.text())
        lat2_deg = float(self.lat2_deg_lineedit.text())
        lat2_min = float(self.lat2_min_lineedit.text())
        lat2_sec = float(self.lat2_sec_lineedit.text())
        lon2_deg = float(self.lon2_deg_lineedit.text())
        lon2_min = float(self.lon2_min_lineedit.text())
        lon2_sec = float(self.lon2_sec_lineedit.text())
        lat1_pole = self.point1_lat_pole.currentText()
        lon1_dir = self.point1_lon_dir.currentText()
        lat2_pole = self.point2_lat_pole.currentText()
        lon2_dir = self.point2_lon_dir.currentText()
        flip = 0 
        warning_list = []
        if lat1_deg > 90 or lat1_deg < 0 or lat2_deg > 90 or lat2_deg < 0:
            flip = flip + 1
            warning_list.append("Latitudes must be in the range from 0 to 90")
        if lon1_deg > 180 or lon1_deg < 0 or lon2_deg > 180 or lon2_deg < 0:
            flip = flip + 1 
            warning_list.append("Longitudes must be in the range from 0 to 180")
        if lat1_min > 59 or lat1_min < 0 or lat2_min > 59 or lat2_min < 0:
            flip = flip + 1 
            warning_list.append("Minutes must be in the range from 0 to 59")
        if lat1_sec > 59 or lat1_sec < 0 or lat2_sec > 59 or lat2_sec < 0:
            flip = flip + 1
            warning_list.append("Seconds must be in the range from 0 to 59")
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
           # msg = QMessageBox()
            #msg.setWindowTitle("Invalid Input")
            #msg.setIcon(QMessageBox.Critical)

            #msg.setText(errorko)
            #msg.exec_()
            return
        result = calculate_mid_point_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min,lon1_sec,lat2_deg,lat2_min,lat2_sec,lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir)
        lat_res = result[0]
        lat_res_deg  = lat_res[0][0]
        lat_res_min = lat_res[0][1]
        lat_res_sec = lat_res[0][2]
        lat_res_pol = lat_res[1]

        lon_res = result[1]
        lon_res_deg= lon_res[0][0]
        lon_res_min = lon_res[0][1]
        lon_res_sec = lon_res[0][1]
        lon_res_dir = lon_res[1]


        result = str(lat_res_deg) + degree_sign + " "+str(lat_res_min)+"\' "+ str(lat_res_sec)+"\'\' " + lat_res_pol+",  " + str(lon_res_deg)+degree_sign+" " + str(lon_res_min)+"\' " + str(lon_res_sec)+"\'\' " + lon_res_dir

        
    
        self.midpoint_value_label_tab2.setText(str(result))

    

    def display_endpoint_and_bearing_tab2(self):
        print("dispaly endpoint end bearin tab")
        degree_sign = u"\N{DEGREE SIGN}"
        lat_deg = float(self.startpoint_lat_deg_lineedit_tab2.text())
        lat_min = float(self.startpoint_lat_min_lineedit_tab2.text())
        lat_sec = float(self.startpoint_lat_sec_lineedit_tab2.text())
        lat_pole = str(self.start_point_lat_combo.currentText())
        lon_deg = float(self.startpoint_lon_deg_lineedit_tab2.text())
        lon_min = float(self.startpoint_lon_min_lineedit_tab2.text())
        lon_sec = float(self.startpoint_lon_sec_lineedit_tab2.text())
        lon_dir = str(self.start_point_lon_combo.currentText())

        distance = float(self.distance_lineedit_tab2.text())
        
        b_deg = float(self.bearing_deg_lineedit_tab2.text())
        b_min = float(self.bearing_min_lineedit_tab2.text())
        b_sec = float(self.bearing_sec_lineedit_tab2.text())
        result = calculate_destinaion_point(lat_deg, lat_min,lat_sec, lat_pole,lon_deg,lon_min,lon_sec,lon_dir,distance,b_deg,b_min,b_sec)
        print("lat deg is ", lat_deg)
        flip = 0
        warning_list = []
        if lat_deg > 90 or lat_deg < 0:
            flip = flip + 1
            warning_list.append("Latitudes must be in 0-90")
        if lon_deg > 180 or lon_deg < 0:
            flip = flip + 1
            warning_list.append("Longitudes must be in 0-180")
        if b_deg > 180 or b_deg < 0:
            flip = flip + 1
            warning_list.append("Bearing degree must be in 0-180")
        #check minutes and seconds
        if lat_min > 59 or lon_min >59 or b_min > 59:
            flip = flip + 1
            warning_list.append("Minutes must be in 0-59")
        
        if lat_sec > 59 or lon_sec > 59 :
            flip = flip + 1
            warning_list.append("Seconds must be in 0-59")
        
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setIcon(QMessageBox.Critical)

            msg.setText(errorko)
            msg.exec_()
            return
        
        dest_lag_deg = result[0][0][0][0]
        dest_lag_min = result[0][0][0][1]
        dest_lag_sec = result[0][0][0][2]
        dest_pole = result[0][0][1]
        dest_lon_deg = result[0][1][0][0]
        dest_lon_min = result[0][1][0][1]
        dest_lon_sec = result [0][1][0][2]
        dest_dir = result[0][1][1]
        fbearing_deg = result[1][0]
        fbearing_min = result[1][1]
        fbearing_sec = result[1][2]



        destination_point = str(dest_lag_deg)+degree_sign+" "+str(dest_lag_min)+"\' " + str(dest_lag_sec)+" \'\' " + dest_pole + ", "+str(dest_lon_deg)+degree_sign+" "+str(dest_lon_min)+"\' "+str(dest_lon_sec)+"\'\' " + dest_dir
        fbearing = str(fbearing_deg)+degree_sign + " "+ str(fbearing_min)+"\' "+str(fbearing_sec)+"\'\'"

        self.destination_label_value_tab2.setText(destination_point)
        self.final_bearing_value_label_lab2.setText(fbearing)


    

# function of tab3 - finding intersection point when parameters are in dd format
    def display_intersection_point_dd(self):
        degree_sign = u"\N{DEGREE SIGN}"
        lat1 = float(self.lat1_dd_tab3.text())
        lat2 = float(self.lat2_dd_tab3.text())
        lon1 = float(self.lon1_dd_tab3.text())
        lon2 = float(self.lon2_dd_tab3.text())
        b1 = float (self.bearing1_dd_tab3.text())
        b2 = float(self.bearing2_dd_tab3.text())


        flip = 0 
        warning_list = []
        if lat1 > 90 or lat2 > 90 or lat1 < -90 or lat2 < -90:
            flip = flip + 1
            warning_list.append("Latitudes must be in the range from  -90  to 90")
        if lon1 > 180 or lon2 > 180 or lon1 < -180 or lon1 < -180:
            flip = flip + 1 
            warning_list.append("Longitudes must be in the range from -180 to 180")
        if b1 > 180 or b1 <-180 or b2 > 180 or b2 < -180:
            flip = flip  + 1 
            warning_list.append("Bearing must be in the range of -180 to 180")
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setIcon(QMessageBox.Critical)

            msg.setText(errorko)
            msg.exec_()
            return



        result = find_intersection_point(lat1,lon1,lat2,lon2,b1,b2)
        print(len(result))
        if len(result) == 2:
            print("lkejsf")
            intersection_lat_deg = str(result[0][0][0])
            intersection_lat_min = str(result[0][0][1])
            intersection_lat_sec = str(result[0][0][2])
            intersection_lon_deg = str(result[1][0][0])
            intersection_lon_min = str(result[1][0][1])
            intersection_lon_sec = str(result[1][0][2])
            pole = str(result[0][1])
            direction = str(result[1][1])
            self.intersection_point_value_label.setText(intersection_lat_deg + degree_sign +" " + intersection_lat_min + "\'"+" "+ intersection_lat_sec + "\'\' "+" "+pole+"  ,  " + intersection_lon_deg + degree_sign+" "+ intersection_lon_min + "\'"+" "+ intersection_lon_sec + " \'\' " + direction)
        else:
            print(len(result))
            value = str(result[0])
            print(value)
            self.intersection_point_value_label.setText(value)
    #find intersection point when the paramaters are in dms format
    def display_intersection_point_dms(self):
        degree_sign = u"\N{DEGREE SIGN}"

        lat1_deg = float(self.lat1_deg_dms_tab3.text())
        lat1_min = float(self.lat1_min_dms_tab3.text())
        lat1_sec = float(self.lat1_sec_dms_tab3.text())
        point1_pole = str(self.point1_pole_tab3.currentText())
        lon1_deg = float(self.lon1_deg_dms_tab3.text())
        lon1_min = float(self.lon1_min_dms_tab3.text())
        lon1_sec = float(self.lon1_sec_dms_tab3.text())
        point1_direction = str(self.point1_direction_tab3.currentText())
        lat2_deg = float(self.lat2_deg_dms_tab3.text())
        lat2_min = float(self.lat2_min_dms_tab3.text())
        lat2_sec = float(self.lat2_sec_dms_tab3.text())
        point2_pole = str(self.point2_pole_tab3.currentText())
        lon2_deg = float(self.lon2_deg_dms_tab3.text())
        lon2_min = float(self.lon2_min_dms_tab3.text())
        lon2_sec = float(self.lon2_sec_dms_tab3.text())
        point2_direction = str(self.point2_direction_tab3.currentText())
        b1_deg = float(self.bearing1_deg_dms_tab3.text())
        b1_min = float(self.bearing1_min_dms_tab3.text())
        b1_sec = float(self.bearing1_sec_dms_tab3.text())
        b2_deg = float(self.bearing2_deg_dms_tab3.text())
        b2_min = float(self.bearing2_min_dms_tab3.text())
        b2_sec = float(self.bearing2_sec_dms_tab3.text())

        flip = 0 # if it is 0 , all inputs are valid
        warning_list = []
        if lat1_deg > 90 or lat2_deg > 90:
            flip = flip + 1
            warning_list.append("Latitude degrees must be in 0-90")
        if lon1_deg > 180 or lon2_deg > 180:
            flip = flip + 1
            warning_list.append("Longitude degrees must be in 0-180")
        if b1_deg > 180 or b2_deg > 180:
            flip = flip + 1
            warning_list.append("Bearing degrees must be in 0-180")
        if lat1_min > 59 or lon1_min > 59 or lat2_min >59 or lon2_min > 59:
            flip = flip + 1
            warning_list.append("Minutes must be in 0-59")
        if lat1_sec > 59 or lon1_sec > 59 or lat2_sec > 59 or lon2_sec > 59:
            flip = flip + 1
            warning_list.append("Seconds must be in 0-59")
        
        if flip > 0:
            errorko = ""
            self.invalid = True
            for item in warning_list:
                errorko = errorko + item + "\n"
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setIcon(QMessageBox.Critical)

            msg.setText(errorko)
            msg.exec_()
            return


        lat1_dd = dms_to_dd(lat1_deg, lat1_min,lat1_sec)
        if point1_pole == "S":
            lat1_dd = -1 * lat1_dd
        lon1_dd = dms_to_dd(lon1_deg, lon1_min, lon1_sec)
        if point1_direction == "W":
            lon1_dd = -1 * lon1_dd
        lat2_dd = dms_to_dd(lat2_deg, lat2_min, lat2_sec)
        if point2_pole == "S":
            lat2_dd = -1 * lat2_dd
        lon2_dd = dms_to_dd(lon2_deg, lon2_min, lon2_sec)
        if point2_direction == "W":
            lon2_dd = -1 * lon2_dd
        
        bearing1_dd = dms_to_dd(b1_deg, b1_min, b1_sec)
        bearing2_dd = dms_to_dd(b2_deg, b2_min, b2_sec)

        intersection_point = find_intersection_point(lat1_dd, lon1_dd, lat2_dd, lon2_dd, bearing1_dd, bearing2_dd)


        if len(intersection_point) == 2:
            intersection_lat_deg = str(intersection_point[0][0][0])
            intersection_lat_min = str(intersection_point[0][0][1])
            intersection_lat_sec = str(intersection_point[0][0][2])
            intersection_lon_deg = str(intersection_point[1][0][0])
            intersection_lon_min = str(intersection_point[1][0][1])
            intersection_lon_sec = str(intersection_point[1][0][2])
            pole = str(intersection_point[0][1])
            direction = str(intersection_point[1][1])
            self.intersection_value_dms_label.setText(intersection_lat_deg + degree_sign+" " + intersection_lat_min + " \' "+ intersection_lat_sec + " \'\' "+pole+"  ,  " + intersection_lon_deg + degree_sign+" "+ intersection_lon_min + " \' "+ intersection_lon_sec + " '\'\' " + direction)
        else:
            print(len(intersection_point))
            value = str(intersection_point[0])
            print(value)
            self.intersection_value_dms_label.setText(value)




app = QtWidgets.QApplication(sys.argv)
window = ModiWindow()
window.show()
app.exec_()