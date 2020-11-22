import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from GUI_01 import *
from class01 import *
# class MyForm(QMainWindow):

class MyForm(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        studentObj = Student(self.ui.lineEditName.text())
        self.ui.labelResponse.setText("Hello "+studentObj.printName())
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())