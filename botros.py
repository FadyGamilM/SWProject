from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from project2 import *

import sqlite3
import SQLiteDB_Design

import sys
from os import path

Class,_=loadUiType(path.join(path.dirname(__file__),"staff.ui"))

class Botros(QMainWindow,Class):
   def __init__(self,Account,parent=None):
      super(Botros,self).__init__(parent)
      QMainWindow.__init__(self)
      self.setupUi(self)
      self.Transation()
      self.modify_Ui()
      self.Account=Account
      #self.pushButton_13.setVisible(False)
      self.pushButton_13.setText(self.Account)
      self.staff_connect_DB()
    
    

   def staff_connect_DB(self):
        self.conn=sqlite3.connect('projectDB.db')
        self.c=self.conn.cursor()

   def modify_Ui(self):
      self.tabWidget.tabBar().setVisible(True)


   def Transation(self):
      self.pushButton.clicked.connect(self.open_BookingTap)
      self.pushButton_4.clicked.connect(self.LogOut)
      self.pushButton_2.clicked.connect(self.open_TasksPage)
      self.pushButton_12.clicked.connect(self.Show_Tasks)
      self.pushButton_9.clicked.connect(self.open_MarkTasksPage)
      self.pushButton_11.clicked.connect(self.Mark_FinishedTasks)

########################## Log Out ########################################3
   def LogOut(self):
      self.MainPageObject=Intro_Main(0)
      self.MainPageObject.show()
      self.close()
########################## Booking Tap ######################################
   def open_BookingTap(Self):
      Self.tabWidget.setCurrentIndex(0)

########################### Tasks Tap #######################################
   def open_TasksPage(self):
      self.tabWidget.setCurrentIndex(1)

######################### Edit Task Status #######################
   def open_MarkTasksPage(self):
      self.tabWidget.setCurrentIndex(2)

######################### SHOW assigned Tasks ##########################
   def Show_Tasks(self):
      query=("SELECT ID,Date,Task,STatus FROM Tasks WHERE EmployeeName=?")
      self.c.execute(query,(self.Account,))
      self.conn.commit()
      TaskData=self.c.fetchall()
      self.tableWidget_9.clearContents()
      self.tableWidget_9.setRowCount(0)
      self.tableWidget_9.insertRow(0)
      for row,form in enumerate(TaskData):
         for col,item in enumerate(form):
            self.tableWidget_9.setItem(row,col,QTableWidgetItem(str(item)))
            col=col+1
         rowPosition=self.tableWidget_9.rowCount()
         self.tableWidget_9.insertRow(rowPosition)


######################### Mark The Task ################################################
   def Mark_FinishedTasks(Self):
      ID_ofTask=Self.lineEdit_33.text()
      MarkingEntry=(1,ID_ofTask,Self.Account)
      somequery=(""" UPDATE Tasks SET Status =? WHERE ID =? AND EmployeeName=? """)
      Self.c.execute(somequery,MarkingEntry)
      Self.conn.commit()





##################################################################################





def main():
   app=QApplication(sys.argv)
   window=Botros("")
   window.show()
   app.exec_()

if __name__ == '__main__':
     main()