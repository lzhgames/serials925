# -*- coding: utf-8 -*-
# __author__ = 'Lu'
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ =="__main__":
    app=QApplication(sys.argv)
    mywindow=QWidget()
    mywindow.setWindowTitle('My Window!')
    mywindow.setGeometry(300,300,380,380)
    mywindow.show()
    sys.exit(app.exec_())