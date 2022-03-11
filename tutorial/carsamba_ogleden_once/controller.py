import sys
from tokenize import Double
from PySide2 import QtWidgets,QtGui
from ui import Ui_MainWindow
import math
from haver import calculate_midpoint, convert_to_radian, find_bearing, radian_to_degree, dd_to_dms, calculate_distance,final_bearing, calculate_distance_tab2,calculate_azamith_tab2
from dest_and_final_bearing import find_destination_point
class ModiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ModiWindow,self).__init__()
        self.setupUi(self)


        #validator for lat and lon for tab1's inputs 
        lat_validator = QtGui.QDoubleValidator(-90,90,4)
        lat_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        lon_validator = QtGui.QDoubleValidator(-180,180,8)
        lon_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        
        #set validators for lineedit inputs 
        self.lat1.setValidator( lat_validator)
        self.lon1.setValidator( lon_validator )
        self.lat2.setValidator( lat_validator )
        self.lon2.setValidator( lon_validator )

        #validator for tab2 is lineedits
        lat_deg_validator = QtGui.QDoubleValidator(0,90,4)
        lat_deg_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        min_validator = QtGui.QDoubleValidator(0,60,4)
        min_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        sec_validator = QtGui.QDoubleValidator(0,60,4)
        sec_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        lon_deg_validator = QtGui.QDoubleValidator(0,180,4)
        lon_deg_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        
        #set validators for lineedit inputs
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

        
        

                
        #buttons for tab1
        self.calculate_button.clicked.connect(self.find_distance)
        self.calculate_button.clicked.connect(self.find_azamith)
        self.calculate_button.clicked.connect(self.find_final_bearing)
        self.calculate_button.clicked.connect(self.find_midpoint)
        self.calculate_dest_bearing_button.clicked.connect(self.calculate_destination_point)
        
        #buttons for tab2
        self.calculate_button_tab2.clicked.connect(self.display_distance_tab2)
        self.calculate_button_tab2.clicked.connect(self.display_azamith_tab2)
        
        

    #functions for tab1
    def find_distance(self):
        lat1 = (float((self.lat1.text())))
        lon1= float(self.lon1.text())
        lat2 = float(self.lat2.text())
        lon2 = float(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2

        result = calculate_distance(point1,point2) # comes from haver.py
        #set the label
        self.label_2.setText(str(result))
        

    
    def find_azamith(self):  # azamith means initial bearing
        degree_sign = u"\N{DEGREE SIGN}"

        
        lat1 = (float((self.lat1.text())))
        lon1= float(self.lon1.text())
        lat2 = float(self.lat2.text())
        lon2 = float(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2
        result = find_bearing(point1,point2)
        

        #degree min sec
        result = str(result[0]) + degree_sign + " " + str(result[1]) + "\' " + str(result[2]) + "\'\'" 

        #set the label

        self.label_value_azamith.setText(result)

        
    
    def find_final_bearing(self):
        degree_sign = u"\N{DEGREE SIGN}"
        lat1 = (float((self.lat1.text())))
        lon1= float(self.lon1.text())
        lat2 = float(self.lat2.text())
        lon2 = float(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2

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

        result = calculate_midpoint(point1,point2)

        mid_lat = result[0]
        mid_lon = result[1]
        
        result = str(mid_lat[0][0]) +degree_sign + " "+ str(mid_lat[0][1]) + "\'" + str(mid_lat[0][2]) + "\'\' " + str(mid_lat[1]) + "  " + str(mid_lon[0][0]) +degree_sign + " "+ str(mid_lon[0][1]) + "\'" + str(mid_lon[0][2]) + "\'\' " + str(mid_lon[1])
        self.midpoint_value_label.setText(result)
        

    def calculate_destination_point(self):
        degree_sign = u"\N{DEGREE SIGN}"
        start_lat = float(self.start_lat_lineedit.text()) # in dd
        start_lon = float(self.start_longitude_lineedit.text()) # in dd
        distance = float(self.distance_lineEdit.text()) # in km
        azamith  = float(self.bearing_lineEdit.text()) # in dd

        start_point = start_lat , start_lon
        
        x = find_destination_point(start_point, distance, azamith)
        
        #print(x)

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
        print(final_bearing_part)

        result_destination_point = str(destination_lat_dms[0]) + degree_sign + " " + str(destination_lat_dms[1]) + "\'" + str(destination_lat_dms[2]) + "\'\' " + destination_lat_pole +  ",  " + str(destination_lon_dms[0]) + degree_sign+ " "+str(destination_lon_dms[1]) + "\'" + str(destination_lon_dms[2]) + "\'\' " + destination_lon_direction
        result_fbearing = str(fbearing_deg) + degree_sign + " " + str(fbearing_min) + "\'" + str(fbearing_sec) + "\'\'"
        self.destination_point_value_label.setText(result_destination_point)
        self.final_bearing_value_label.setText(result_fbearing)

    #functions for tab2
    def foo(self):
        self.distance_value_label.setText("omer")


    def display_distance_tab2(self):
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

        lat1_pole = str(self.lat1_pole_lineedit.text())
        lon1_dir = str(self.lon1_direction_lineedit.text())
        lat2_pole = str(self.lat2_pole_lineedit.text())
        lon2_dir = str(self.lon2_direction_lineedit.text())

        distance = calculate_distance_tab2(lat1_deg,lat1_min,lat1_sec,lon1_deg,lon1_min,lon1_sec,lat2_deg,lat2_min,lat2_sec,lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir)
        print(distance)

        self.distance_value_label.setText(str(distance))


    def display_azamith_tab2(self):
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

        lat1_pole = str(self.lat1_pole_lineedit.text())
        lon1_dir = str(self.lon1_direction_lineedit.text())
        lat2_pole = str(self.lat2_pole_lineedit.text())
        lon2_dir = str(self.lon2_direction_lineedit.text())

        azamith = calculate_azamith_tab2(lat1_deg, lat1_min,lat1_sec,lon1_deg,lon1_min,lon1_sec,lat2_deg,lat2_min,lat2_sec,lon2_deg,lon2_min,lon2_sec,lat1_pole,lon1_dir,lat2_pole,lon2_dir)
        print("azamith is ",azamith)
        self.bearing_value_label.setText(str(azamith))

app = QtWidgets.QApplication(sys.argv)
window = ModiWindow()
window.show()
app.exec_()