# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow_dialogo_02.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_emergente_01(object):
    def setupUi(self, Dialog_emergente_01):
        Dialog_emergente_01.setObjectName("Dialog_emergente_01")
        Dialog_emergente_01.resize(531, 282)
        Dialog_emergente_01.setWindowOpacity(0.8)
        Dialog_emergente_01.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog_emergente_01)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Dialog_emergente_01)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog_emergente_01)
        QtCore.QMetaObject.connectSlotsByName(Dialog_emergente_01)

    def retranslateUi(self, Dialog_emergente_01):
        _translate = QtCore.QCoreApplication.translate
        Dialog_emergente_01.setWindowTitle(_translate("Dialog_emergente_01", "Ventana emergente - Servicios"))
        self.label.setText(_translate("Dialog_emergente_01", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">- Entrenamiento a sus colaboradores.</span></p><p align=\"justify\"><span style=\" font-weight:600;\">- Transferencia tecnológica.</span></p><p align=\"justify\"><span style=\" font-weight:600;\">- Asesoría en innovación.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_emergente_01 = QtWidgets.QDialog()
    ui = Ui_Dialog_emergente_01()
    ui.setupUi(Dialog_emergente_01)
    Dialog_emergente_01.show()
    sys.exit(app.exec_())
