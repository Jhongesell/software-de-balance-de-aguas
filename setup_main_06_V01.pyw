import sys
import matplotlib as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QDialog
#from UI.option05_main import *
from UI.option06_mainV02 import Ui_VentanaPrincipalSBW
#from UI.dialog_aboutproject_01 import Ui_Dialog_aboutproject_01

#from UI.mode_widget_logo import Ui_Form
#from UI.logo import *

class MyForm(QMainWindow):


    # 01. Método inicial
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipalSBW()
        self.ui.setupUi(self)
 
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())