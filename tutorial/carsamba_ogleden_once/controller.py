import sys
from tokenize import Double
from PySide2 import QtWidgets,QtGui
from ui import Ui_MainWindow
import math
from haver import calculate_midpoint, convert_to_radian, find_bearing, radian_to_degree, dd_to_dms, calculate_distance,final_bearing
from dest_and_final_bearing import find_destination_point
class ModiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ModiWindow,self).__init__()
        self.setupUi(self)

        self.lat1.setValidator( QtGui.QIntValidator(-90,90,self) )
        self.lon1.setValidator( QtGui.QIntValidator(-180,180,self) )
        self.lat1.setValidator( QtGui.QIntValidator(-90,90,self) )
        self.lat1.setValidator( QtGui.QIntValidator(-180,180,self) )

        #Point variables as tuple
        

        #self.calculate_button.clicked.connect(self.display_distance)
        
        self.calculate_button.clicked.connect(self.find_distance)
        self.calculate_button.clicked.connect(self.find_azamith)
        self.calculate_button.clicked.connect(self.find_final_bearing)
        self.calculate_button.clicked.connect(self.find_midpoint)


        self.calculate_dest_bearing_button.clicked.connect(self.calculate_destination_point)
        
    def find_distance(self):
        lat1 = (int((self.lat1.text())))
        lon1= int(self.lon1.text())
        lat2 = int(self.lat2.text())
        lon2 = int(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2

        result = calculate_distance(point1,point2) # comes from haver.py
        #set the label
        self.label_2.setText(str(result))
        

    
    def find_azamith(self):  # azamith means initial bearing
        degree_sign = u"\N{DEGREE SIGN}"

        
        lat1 = (int((self.lat1.text())))
        lon1= int(self.lon1.text())
        lat2 = int(self.lat2.text())
        lon2 = int(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2
        result = find_bearing(point1,point2)
        

        #degree min sec
        result = str(result[0]) + degree_sign + " " + str(result[1]) + "\' " + str(result[2]) + "\'\'" 

        #set the label

        self.label_value_azamith.setText(result)

        
    
    def find_final_bearing(self):
        degree_sign = u"\N{DEGREE SIGN}"
        lat1 = (int((self.lat1.text())))
        lon1= int(self.lon1.text())
        lat2 = int(self.lat2.text())
        lon2 = int(self.lon2.text())

        point1 = lat1, lon1
        point2 = lat2, lon2

        result = final_bearing(point1,point2)
        
        #degree min sec
        result = str(result[0]) + degree_sign + " " + str(result[1]) + "\' " + str(result[2]) + "\'\'" 
        #set label
        self.final_bearing_label.setText(result)


    def find_midpoint(self):
        degree_sign = u"\N{DEGREE SIGN}"
        
        lat1 = int(self.lat1.text())
        lon1 = int(self.lon1.text())
        lat2 = int(self.lat2.text())
        lon2 = int(self.lon2.text())

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



app = QtWidgets.QApplication(sys.argv)
window = ModiWindow()
window.show()
app.exec_()