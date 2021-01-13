from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

######################################## connected pages : [1]Login  [2]SignUp  [3]dahab and hurghada hotel #########################
from tharwatlogin import *
from tharwatsignup import *
from project import MainDahab
from tharwathotel import App_WindowHurghada
######################################################################################################################################

from PyQt5.uic import loadUiType
import sys
from os import path

from PyQt5.uic.properties import QtWidgets

MainUI,_ = loadUiType('intro2.ui')

class Intro_Main(QMainWindow, MainUI):
    def __init__(self, USERSTATUS ,parent=None):
        super(Intro_Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pure life hotels")
        ## to connect with database ##
        self.INTRO_connect_DB()
        self.UStatus=USERSTATUS
        ## to go to another page ##
        self.Transation()
        ## User account Button should be hidden by default ##
        self.SignBtn.setVisible(False)
        self.Flag=0
        #print(self.UStatus)


    

    def INTRO_connect_DB(self):
        self.conn=sqlite3.connect('projectDB.db')
        self.c=self.conn.cursor()

    def Transation(self):
        self.pushButton_2.clicked.connect(self.open_Login)
        self.pushButton.clicked.connect(self.open_Signup)
        self.pushButton_3.clicked.connect(self.open_DahabHotel)
        self.pushButton_4.clicked.connect(self.open_HurghadaHotel)
        

    def open_Login(self):
        self.LoginObj=App_Window()
        self.LoginObj.show()
        self.close()        

    def open_Signup(self):
        self.signupObj=App_WindowSU()
        self.signupObj.show()
        self.close()    


    def open_DahabHotel(self):
        self.DahabObj=MainDahab(self.UStatus,"Pure Life Dahab")
        self.DahabObj.show()
        self.close()

    def open_HurghadaHotel(self):
        self.HurghadaObj=App_WindowHurghada(self.UStatus,"Pure Life Hurghada")
        self.HurghadaObj.show()
        self.close()
            

def main():
    app = QApplication(sys.argv)
    window = Intro_Main(0)
    window.show()
    app.exec_()


if __name__ == '__main__' :
    main()