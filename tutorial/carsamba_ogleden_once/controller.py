import sys
from tokenize import Double
from PySide2 import QtWidgets,QtGui
from ui import Ui_MainWindow
import math
from haver import calculate_midpoint, convert_to_radian, find_bearing, radian_to_degree, dd_to_dms, calculate_distance,final_bearing

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
        print("--final bearing---")
        
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
        
        result = str(mid_lat[0][0]) +degree_sign + str(mid_lat[0][1]) + "\'" + str(mid_lat[0][2]) + "\'\' " + str(mid_lat[1]) + "  " + str(mid_lon[0][0]) +degree_sign + str(mid_lon[0][1]) + "\'" + str(mid_lon[0][2]) + "\'\' " + str(mid_lon[1])
        self.midpoint_value_label.setText(result)
        


app = QtWidgets.QApplication(sys.argv)
window = ModiWindow()
window.show()
app.exec_()