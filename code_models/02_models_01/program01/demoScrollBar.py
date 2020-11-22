# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSliders.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 503)
        Dialog.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalScrollBarSugarLevel = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBarSugarLevel.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.horizontalScrollBarSugarLevel.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarSugarLevel.setObjectName("horizontalScrollBarSugarLevel")
        self.verticalLayout.addWidget(self.horizontalScrollBarSugarLevel)
        self.horizontalSliderBloodPressure = QtWidgets.QSlider(Dialog)
        self.horizontalSliderBloodPressure.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.horizontalSliderBloodPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBloodPressure.setObjectName("horizontalSliderBloodPressure")
        self.verticalLayout.addWidget(self.horizontalSliderBloodPressure)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalScrollBarPulseRate = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBarPulseRate.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.verticalScrollBarPulseRate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarPulseRate.setObjectName("verticalScrollBarPulseRate")
        self.horizontalLayout.addWidget(self.verticalScrollBarPulseRate)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalSliderCholestrolLevel = QtWidgets.QSlider(Dialog)
        self.verticalSliderCholestrolLevel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.verticalSliderCholestrolLevel.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderCholestrolLevel.setObjectName("verticalSliderCholestrolLevel")
        self.horizontalLayout_3.addWidget(self.verticalSliderCholestrolLevel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.lineEditResult = QtWidgets.QLineEdit(Dialog)
        self.lineEditResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditResult.setObjectName("lineEditResult")
        self.verticalLayout_4.addWidget(self.lineEditResult)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sugar Level"))
        self.label_2.setText(_translate("Dialog", "Blood Pressure"))
        self.label_3.setText(_translate("Dialog", "Pulse rate"))
        self.label_4.setText(_translate("Dialog", "Cholesterol Level"))

