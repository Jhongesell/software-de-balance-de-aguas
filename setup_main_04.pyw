import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from UI.option05_main import *
class MyForm(QMainWindow):

    # 01. Método inicial
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 01.01. Pestaña 'File'
        self.ui.actionOpen.triggered.connect(self.openFileDialog)
        self.ui.actionSave.triggered.connect(self.saveFileDialog)

        """# 01.02. Pestaña 'Edition'
        self.ui.actionCut.triggered.connect(self.cutMethod)
        self.ui.actionCopy.triggered.connect(self.copyMethod)
        self.ui.actionPaste.triggered.connect(self.pasteMethod)"""

        # 01.03. Pestaña 'Windows'
        self.ui.mdiArea.addSubWindow(self.ui.subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_2)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_3)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_4)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_5)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_6)
        self.ui.actionSubWindow_View.triggered.connect(self.SubWindow_View)
        self.ui.actionTabbed_View.triggered.connect(self.Tabbed_View)
        self.ui.actionCascade_View.triggered.connect(self.cascadeArrange)
        self.ui.actionTile_View.triggered.connect(self.tileArrange)

        # 01.04. Operacion para filas 3 y 4 (Min y Max precipitación)
        self.ui.pushButton_01.clicked.connect(self.tabla01_precipitacion)

        self.show()

    # 02. Método 'File'
    def openFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file'
        '/home')
        if fname[0]:
            f = open(fname[0], 'r')
        with f:
            data = f.read()
            self.ui.textEdit.setText(data)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,
        "QFileDialog.getSaveFileName()",
        "", "All files (*);; Text Files (*.txt)", options=options)
        f = open(fileName, 'w')
        text = self.ui.textEdit.toPlainText()
        f.write(text)
        f.close()

    """# 03. Método 'Edition'
    def cutMethod(self):
        self.ui.label.setText("Cut menu item is selected")

    def copyMethod(self):
        self.ui.label.setText("Copy menu item is selected")

    def pasteMethod(self):
        self.ui.label.setText("Paste menu item is selected")"""

    # 04. Método 'Window'
    def SubWindow_View(self):
        self.ui.mdiArea.setViewMode(0)
    def Tabbed_View(self):
        self.ui.mdiArea.setViewMode(1)
    def cascadeArrange(self):
        self.ui.mdiArea.cascadeSubWindows()
    def tileArrange(self):
        self.ui.mdiArea.tileSubWindows()

    # 05. Tabla 01 - Calculo de precipitaciones mínimas y máximas

    # Lectura de precipitación y desviación estandar para enero
    def tabla01_precipitacion(self):
        if len(self.ui.lineEdit_Jan_Fila01.text()) != 0:
            a01 = float(self.ui.lineEdit_Jan_Fila01.text())
        else:
            a01 = 0
        if len(self.ui.lineEdit_Jan_Fila02.text()) != 0:
            a02 = float(self.ui.lineEdit_Jan_Fila02.text())
        else:
            a02 = 0

        # Lectura de precipitación y desviación estandar para febrero
        if len(self.ui.lineEdit_Feb_Fila01.text()) != 0:
            b01 = float(self.ui.lineEdit_Feb_Fila01.text())
        else:
            b01 = 0
        if len(self.ui.lineEdit_Feb_Fila02.text()) != 0:
            b02 = float(self.ui.lineEdit_Feb_Fila02.text())
        else:
            b02 = 0

        # Lectura de precipitación y desviación estandar para marzo
        if len(self.ui.lineEdit_Mar_Fila01.text()) != 0:
            c01 = float(self.ui.lineEdit_Mar_Fila01.text())
        else:
            c01 = 0
        if len(self.ui.lineEdit_Mar_Fila02.text()) != 0:
            c02 = float(self.ui.lineEdit_Mar_Fila02.text())
        else:
            c02 = 0

        # Lectura de precipitación y desviación estandar para abril
        if len(self.ui.lineEdit_Abr_Fila01.text()) != 0:
            d01 = float(self.ui.lineEdit_Abr_Fila01.text())
        else:
            d01 = 0
        if len(self.ui.lineEdit_Abr_Fila02.text()) != 0:
            d02 = float(self.ui.lineEdit_Abr_Fila02.text())
        else:
            d02 = 0

        # Lectura de precipitación y desviación estandar para mayo
        if len(self.ui.lineEdit_May_Fila01.text()) != 0:
            e01 = float(self.ui.lineEdit_May_Fila01.text())
        else:
            e01 = 0
        if len(self.ui.lineEdit_May_Fila02.text()) != 0:
            e02 = float(self.ui.lineEdit_May_Fila02.text())
        else:
            e02 = 0

        # Lectura de precipitación y desviación estandar para junio
        if len(self.ui.lineEdit_Jun_Fila01.text()) != 0:
            f01 = float(self.ui.lineEdit_Jun_Fila01.text())
        else:
            f01 = 0
        if len(self.ui.lineEdit_Jun_Fila02.text()) != 0:
            f02 = float(self.ui.lineEdit_Jun_Fila02.text())
        else:
            f02 = 0

        # Lectura de precipitación y desviación estandar para julio
        if len(self.ui.lineEdit_Jul_Fila01.text()) != 0:
            g01 = float(self.ui.lineEdit_Jul_Fila01.text())
        else:
            g01 = 0
        if len(self.ui.lineEdit_Jun_Fila02.text()) != 0:
            g02 = float(self.ui.lineEdit_Jul_Fila02.text())
        else:
            g02 = 0

        # Lectura de precipitación y desviación estandar para agosto
        if len(self.ui.lineEdit_Aug_Fila01.text()) != 0:
            h01 = float(self.ui.lineEdit_Aug_Fila01.text())
        else:
            h01 = 0
        if len(self.ui.lineEdit_Aug_Fila02.text()) != 0:
            h02 = float(self.ui.lineEdit_Aug_Fila02.text())
        else:
            h02 = 0

        # Lectura de precipitación y desviación estandar para setiembre
        if len(self.ui.lineEdit_Set_Fila01.text()) != 0:
            i01 = float(self.ui.lineEdit_Set_Fila01.text())
        else:
            i01 = 0
        if len(self.ui.lineEdit_Set_Fila02.text()) != 0:
            i02 = float(self.ui.lineEdit_Set_Fila02.text())
        else:
            i02 = 0

        # Lectura de precipitación y desviación estandar para octubre
        if len(self.ui.lineEdit_Oct_Fila01.text()) != 0:
            j01 = float(self.ui.lineEdit_Oct_Fila01.text())
        else:
            j01 = 0
        if len(self.ui.lineEdit_Oct_Fila02.text()) != 0:
            j02 = float(self.ui.lineEdit_Oct_Fila02.text())
        else:
            j02 = 0

        # Lectura de precipitación y desviación estandar para noviembre
        if len(self.ui.lineEdit_Nov_Fila01.text()) != 0:
            k01 = float(self.ui.lineEdit_Nov_Fila01.text())
        else:
            k01 = 0
        if len(self.ui.lineEdit_Nov_Fila02.text()) != 0:
            k02 = float(self.ui.lineEdit_Nov_Fila02.text())
        else:
            k02 = 0

        # Lectura de precipitación y desviación estandar para diciembre
        if len(self.ui.lineEdit_Dic_Fila01.text()) != 0:
            l01 = float(self.ui.lineEdit_Dic_Fila01.text())
        else:
            l01 = 0
        if len(self.ui.lineEdit_Dic_Fila02.text()) != 0:
            l02 = float(self.ui.lineEdit_Dic_Fila02.text())
        else:
            l02 = 0

        # Calculo de filas 3 y 4
        a03 = a01-2*a02 # Enero
        a04 = a01+2*a02

        b03 = b01-2*b02 # Febrero
        b04 = b01+2*b02

        c03 = c01-2*c02 # Marzo
        c04 = c01+2*c02

        d03 = d01-2*d02 # Abril
        d04 = d01+2*d02

        e03 = e01-2*e02 # Mayo
        e04 = e01+2*e02

        f03 = f01-2*f02 # Junio
        f04 = f01+2*f02

        g03 = g01-2*g02 # Julio
        g04 = g01+2*g02

        h03 = h01-2*h02 # Agosto
        h04 = h01+2*h02

        i03 = i01-2*i02 # Setiembre
        i04 = i01+2*i02

        j03 = j01-2*j02 # Octubre
        j04 = j01+2*j02

        k03 = k01-2*k02 # Noviembre
        k04 = k01+2*k02

        l03 = l01-2*l02 # Diciembre
        l04 = l01+2*l02

        # Presentación en fila 3 y 4
        self.ui.lineEdit_Jan_Fila03.setText(str(a03))
        self.ui.lineEdit_Jan_Fila04.setText(str(a04))

        self.ui.lineEdit_Feb_Fila03.setText(str(b03))
        self.ui.lineEdit_Feb_Fila04.setText(str(b04))

        self.ui.lineEdit_Mar_Fila03.setText(str(c03))
        self.ui.lineEdit_Mar_Fila04.setText(str(c04))

        self.ui.lineEdit_Abr_Fila03.setText(str(d03))
        self.ui.lineEdit_Abr_Fila04.setText(str(d04))

        self.ui.lineEdit_May_Fila03.setText(str(e03))
        self.ui.lineEdit_May_Fila04.setText(str(e04))

        self.ui.lineEdit_Jun_Fila03.setText(str(f03))
        self.ui.lineEdit_Jun_Fila04.setText(str(f04))

        self.ui.lineEdit_Jul_Fila03.setText(str(g03))
        self.ui.lineEdit_Jul_Fila04.setText(str(g04))

        self.ui.lineEdit_Aug_Fila03.setText(str(h03))
        self.ui.lineEdit_Aug_Fila04.setText(str(h04))

        self.ui.lineEdit_Set_Fila03.setText(str(i03))
        self.ui.lineEdit_Set_Fila04.setText(str(i04))

        self.ui.lineEdit_Oct_Fila03.setText(str(j03))
        self.ui.lineEdit_Oct_Fila04.setText(str(j04))

        self.ui.lineEdit_Nov_Fila03.setText(str(k03))
        self.ui.lineEdit_Nov_Fila04.setText(str(k04))

        self.ui.lineEdit_Dic_Fila03.setText(str(l03))
        self.ui.lineEdit_Dic_Fila04.setText(str(l04))
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())