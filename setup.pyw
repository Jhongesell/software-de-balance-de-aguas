import sys
from PyQt5.QtWidgets import QDialog, QApplication
from UI.option01 import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_01.clicked.connect(self.operacion01)
        self.show()
    def operacion01(self):
        if len(self.ui.lineEdit_Jan_Fila01.text()) != 0:
            A1 = float(self.ui.lineEdit_Jan_Fila01.text())
        else:
            A1 = 0
        if len(self.ui.lineEdit_Jan_Fila02.text()) != 0:
            A2 = float(self.ui.lineEdit_Jan_Fila02.text())
        else:
            A2 = 0
        A3 = A1-2*A2
        A4 = A1+2*A2
        self.ui.lineEdit_Jan_Fila03.setText(str(A3))
        self.ui.lineEdit_Jan_Fila03.setText(str(A4))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())