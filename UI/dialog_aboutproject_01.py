# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_aboutproject_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_aboutproject_01(object):
    def setupUi(self, Dialog_aboutproject_01):
        Dialog_aboutproject_01.setObjectName("Dialog_aboutproject_01")
        Dialog_aboutproject_01.resize(309, 331)
        Dialog_aboutproject_01.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog_aboutproject_01)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog_aboutproject_01)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(Dialog_aboutproject_01)
        QtCore.QMetaObject.connectSlotsByName(Dialog_aboutproject_01)

    def retranslateUi(self, Dialog_aboutproject_01):
        _translate = QtCore.QCoreApplication.translate
        Dialog_aboutproject_01.setWindowTitle(_translate("Dialog_aboutproject_01", "About project"))
        self.textBrowser.setHtml(_translate("Dialog_aboutproject_01", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">El software es desarrollado gracias a Water, Waste &amp; Land (WWL).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Se ejecuta la iteracción para un trazo de 10mil años logrando predecir el comportamiento de las precipitacinoes.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Para suscribirse a las noticias del proyecto puede ingresar a <span style=\" color:#0000ff;\">https://wwlengineering.com/es</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_aboutproject_01 = QtWidgets.QDialog()
    ui = Ui_Dialog_aboutproject_01()
    ui.setupUi(Dialog_aboutproject_01)
    Dialog_aboutproject_01.show()
    sys.exit(app.exec_())