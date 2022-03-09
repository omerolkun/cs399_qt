import sys
from PySide2 import QtWidgets,QtGui
from ui import Ui_MainWindow
import math
from haver import find_bearing
class ModiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ModiWindow,self).__init__()
        self.setupUi(self)

        self.lat1.setValidator( QtGui.QIntValidator(-90,90,self) )
        self.lon1.setValidator( QtGui.QIntValidator(-180,180,self) )
        self.lat1.setValidator( QtGui.QIntValidator(-90,90,self) )
        self.lat1.setValidator( QtGui.QIntValidator(-180,180,self) )

        #Point variables as tuple
        

        self.calculate_button.clicked.connect(self.display_distance)
        self.calculate_button.clicked.connect(self.find_bearing1)
        self.calculate_button.clicked.connect(self.find_final_bearing)

        print("heyy")
        

    def display_distance(self):
        R = 6371000 # in meters   radius of earth
        lat1 = int(self.lat1.text())
        lon1 = int(self.lon1.text())
        lat2 = int(self.lat2.text())
        lon2 = int(self.lon2.text())


        phase1 = lat1 * math.pi / 180 # radian value of latitude of point1
        phase2 = lat2 * math.pi / 180 # radian value of latitude of point2

        delta_lambda = (lon2 - lon1) * math.pi / 180 # difference of the longitudes of the points in radian
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
        print (round(result/1000,0))
        
        self.label_2.setText(str(round(result/1000,0)))
        
    
    def find_bearing1(self):
        lat1 = int(self.lat1.text()) * math.pi / 180
        lon1 = int(self.lon1.text()) * math.pi / 180
        lat2 = int(self.lat2.text()) * math.pi / 180
        lon2 = int(self.lon2.text()) * math.pi / 180

        dif_of_lons = (lon2 - lon1)
        x = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(dif_of_lons))
        y = math.sin(dif_of_lons) * math.cos(lat2)

        #formula
        teta = math.atan2(y,x)

        result = (teta * 180 / math.pi + 360 ) % 360 # converting to degree in this final step

        degree = int(result)
        (minute_temp )= (result - (degree)) * 60
        minute = int(minute_temp)
        (seconds) = int((minute_temp-minute) * 60)
        
        dms_azamith =   (degree,minute,seconds)
        
        degree_sign = u"\N{DEGREE SIGN}"
        dms_azamith = str(degree ) + degree_sign + " " + str(minute) + "\'" + str(seconds) + "\'\'"

        self.label_value_azamith.setText(str(dms_azamith))

    def find_final_bearing(self):
        pass
        #print(self.point1[0])
        #print("omers")
        point1 = int(self.lat1.text()) , int(self.lon1.text())
        point2 = int(self.lat2.text()) , int(self.lon2.text())
        result = find_bearing(point2, point1)

        result_temp  = list(result)
        result_temp[0] = (result_temp[0] + 180) % 360
        result = tuple(result_temp)
        #return result
        print(result[0])
        print(result[1])
        print(result[2])
        degree_sign = u"\N{DEGREE SIGN}"
        final_bear = str(result[0]) + degree_sign + str(result[1]) + "\'" + str(result[2]) + "\'\'"
        self.final_bearing_label.setText(final_bear)




app = QtWidgets.QApplication(sys.argv)
window = ModiWindow()
window.show()
app.exec_()