# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow_01 import Ui_OtherWindow_01
from OtherWindow_02 import Ui_OtherWindow_02
from OtherWindow_dialogo_02 import Ui_Dialog_emergente_01

class Ui_MainWindow(object):
    def openWindow_01(self):
        self.window_01 = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow_01()
        self.ui.setupUi(self.window_01)
        self.window_01.show()

    def openWindow_02(self):
        self.window_02 = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow_02()
        self.ui.setupUi(self.window_02)
        self.window_02.show()

    def openWindow_03(self):
        self.window_03 = QtWidgets.QDialog()
        self.ui = Ui_Dialog_emergente_01()
        self.ui.setupUi(self.window_03)
        self.window_03.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 256)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_open_01 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_01.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_open_01.setObjectName("btn_open_01")

        self.btn_open_01.clicked.connect(self.openWindow_01) # Agregado

        self.verticalLayout.addWidget(self.btn_open_01)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_open_02 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_02.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_open_02.setObjectName("btn_open_02")

        self.btn_open_02.clicked.connect(self.openWindow_02) # Agregado

        self.horizontalLayout.addWidget(self.btn_open_02)
        self.btn_open_03 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_03.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_open_03.setObjectName("btn_open_03")

        self.btn_open_03.clicked.connect(self.openWindow_03) # Agregado

        self.horizontalLayout.addWidget(self.btn_open_03)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Programa principal"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Te gusta</span></p><p align=\"center\"><span style=\" font-size:20pt;\">nuestro trabajo</span></p></body></html>"))
        self.btn_open_01.setText(_translate("MainWindow", "Síguenos como"))
        self.btn_open_02.setText(_translate("MainWindow", "Productos"))
        self.btn_open_03.setText(_translate("MainWindow", "Servicios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
