import sys
from PySide2 import QtWidgets,QtGui
from ui import Ui_MainWindow
import math

class ModiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ModiWindow,self).__init__()
        self.setupUi(self)

        self.lat1.setValidator( QtGui.QIntValidator(0,90,self) )
        self.lon1.setValidator( QtGui.QIntValidator(0,180,self) )
        self.lat1.setValidator( QtGui.QIntValidator(0,90,self) )
        self.lat1.setValidator( QtGui.QIntValidator(0,180,self) )


        self.calculate_button.clicked.connect(self.display)
        

    def display(self):
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
        



app = QtWidgets.QApplication(sys.argv)
window = ModiWindow()
window.show()
app.exec_()