import sys
import matplotlib as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from UI.option05_main import *

#from UI.mode_widget_logo import Ui_Form
#from UI.logo import *

class MyForm(QMainWindow):

    # Invocando el mensaje de 'about'
    #def openAboutWindow(self):
     #   self.window = QtWidgets.QMainWindow()
      #  self.ui = Ui_Form()
       # self.ui.setupUi(self.window)
        #self.window.show()

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

        # Pestaña 'about'
        #self.actionAbout_software.clicked.connect(self.openAboutWindow)

        # 01.04. Operacion para filas 3 y 4 (Min y Max precipitación)
        self.ui.pushButton_01.clicked.connect(self.tabla01_precipitacion)

        # 01.05. Operación 'Tabla 03'
        self.ui.pushButton_Input_Tabla03.clicked.connect(self.tabla03_calc)

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

    # 06. Tabla 03 - Calculo de las funciones y gráficas
    
    # Lectura de datos
    def tabla03_calc(self):
        # File A01
        if len(self.ui.lineEdit_Tabla03_A01.text()) != 0:
            t03_a01 = float(self.ui.lineEdit_Tabla03_A01.text())
        else:
            t03_a01 = 0

        # File A02
        if len(self.ui.lineEdit_Tabla03_A02.text()) != 0:
            t03_a02 = float(self.ui.lineEdit_Tabla03_A02.text())
        else:
            t03_a02 = 0

        # File A03
        if len(self.ui.lineEdit_Tabla03_A03.text()) != 0:
            t03_a03 = float(self.ui.lineEdit_Tabla03_A03.text())
        else:
            t03_a03 = 0

        # File A04
        if len(self.ui.lineEdit_Tabla03_A04.text()) != 0:
            t03_a04 = float(self.ui.lineEdit_Tabla03_A04.text())
        else:
            t03_a04 = 0

        # File A05
        if len(self.ui.lineEdit_Tabla03_A05.text()) != 0:
            t03_a05 = float(self.ui.lineEdit_Tabla03_A05.text())
        else:
            t03_a05 = 0

        # File A06
        if len(self.ui.lineEdit_Tabla03_A06.text()) != 0:
            t03_a06 = float(self.ui.lineEdit_Tabla03_A06.text())
        else:
            t03_a06 = 0

        # File A07
        if len(self.ui.lineEdit_Tabla03_A07.text()) != 0:
            t03_a07 = float(self.ui.lineEdit_Tabla03_A07.text())
        else:
            t03_a07 = 0

        # File A08
        if len(self.ui.lineEdit_Tabla03_A08.text()) != 0:
            t03_a08 = float(self.ui.lineEdit_Tabla03_A08.text())
        else:
            t03_a08 = 0

        # File A09
        if len(self.ui.lineEdit_Tabla03_A09.text()) != 0:
            t03_a09 = float(self.ui.lineEdit_Tabla03_A09.text())
        else:
            t03_a09 = 0

        # File A10
        if len(self.ui.lineEdit_Tabla03_A10.text()) != 0:
            t03_a10 = float(self.ui.lineEdit_Tabla03_A10.text())
        else:
            t03_a10 = 0

        # File A11
        if len(self.ui.lineEdit_Tabla03_A11.text()) != 0:
            t03_a11 = float(self.ui.lineEdit_Tabla03_A11.text())
        else:
            t03_a11 = 0

        # File A12
        if len(self.ui.lineEdit_Tabla03_A12.text()) != 0:
            t03_a12 = float(self.ui.lineEdit_Tabla03_A12.text())
        else:
            t03_a12 = 0

        # File A13
        if len(self.ui.lineEdit_Tabla03_A13.text()) != 0:
            t03_a13 = float(self.ui.lineEdit_Tabla03_A13.text())
        else:
            t03_a13 = 0

        # File A14
        if len(self.ui.lineEdit_Tabla03_A14.text()) != 0:
            t03_a14 = float(self.ui.lineEdit_Tabla03_A14.text())
        else:
            t03_a14 = 0

        # File A15
        if len(self.ui.lineEdit_Tabla03_A15.text()) != 0:
            t03_a15 = float(self.ui.lineEdit_Tabla03_A15.text())
        else:
            t03_a15 = 0

        # File A16
        if len(self.ui.lineEdit_Tabla03_A16.text()) != 0:
            t03_a16 = float(self.ui.lineEdit_Tabla03_A16.text())
        else:
            t03_a16 = 0

        # File A17
        if len(self.ui.lineEdit_Tabla03_A17.text()) != 0:
            t03_a17 = float(self.ui.lineEdit_Tabla03_A17.text())
        else:
            t03_a17 = 0

        # File A18
        if len(self.ui.lineEdit_Tabla03_A18.text()) != 0:
            t03_a18 = float(self.ui.lineEdit_Tabla03_A18.text())
        else:
            t03_a18 = 0

        # File A19
        if len(self.ui.lineEdit_Tabla03_A19.text()) != 0:
            t03_a19 = float(self.ui.lineEdit_Tabla03_A19.text())
        else:
            t03_a19 = 0

        # File A20
        if len(self.ui.lineEdit_Tabla03_A20.text()) != 0:
            t03_a20 = float(self.ui.lineEdit_Tabla03_A20.text())
        else:
            t03_a20 = 0

        # File A21
        if len(self.ui.lineEdit_Tabla03_A21.text()) != 0:
            t03_a21 = float(self.ui.lineEdit_Tabla03_A21.text())
        else:
            t03_a21 = 0

        # File A22
        if len(self.ui.lineEdit_Tabla03_A22.text()) != 0:
            t03_a22 = float(self.ui.lineEdit_Tabla03_A22.text())
        else:
            t03_a22 = 0

        t03_d02 = t03_a02 - t03_a01 # Fila 02
        t03_d03 = t03_a03 - t03_a01 # Fila 03
        t03_d04 = t03_a04 - t03_a01 # Fila 04
        t03_d05 = t03_a05 - t03_a01 # Fila 05
        t03_d06 = t03_a06 - t03_a01 # Fila 06
        t03_d07 = t03_a07 - t03_a01 # Fila 07
        t03_d08 = t03_a08 - t03_a01 # Fila 08
        t03_d09 = t03_a09 - t03_a01 # Fila 09
        t03_d10 = t03_a10 - t03_a01 # Fila 10
        t03_d11 = t03_a11 - t03_a01 # Fila 11
        t03_d12 = t03_a12 - t03_a01 # Fila 12
        t03_d13 = t03_a13 - t03_a01 # Fila 13
        t03_d14 = t03_a14 - t03_a01 # Fila 14
        t03_d15 = t03_a15 - t03_a01 # Fila 15
        t03_d16 = t03_a16 - t03_a01 # Fila 16
        t03_d17 = t03_a17 - t03_a01 # Fila 17
        t03_d18 = t03_a18 - t03_a01 # Fila 18
        t03_d19 = t03_a19 - t03_a01 # Fila 19
        t03_d20 = t03_a20 - t03_a01 # Fila 20
        t03_d21 = t03_a21 - t03_a01 # Fila 21
        t03_d22 = t03_a22 - t03_a01 # Fila 22
        

        self.ui.lineEdit_Tabla03_D02.setText(str(t03_d02)) # Fila 02
        self.ui.lineEdit_Tabla03_D03.setText(str(t03_d03)) # Fila 03
        self.ui.lineEdit_Tabla03_D04.setText(str(t03_d04)) # Fila 04
        self.ui.lineEdit_Tabla03_D05.setText(str(t03_d05)) # Fila 05
        self.ui.lineEdit_Tabla03_D06.setText(str(t03_d06)) # Fila 06
        self.ui.lineEdit_Tabla03_D07.setText(str(t03_d07)) # Fila 07
        self.ui.lineEdit_Tabla03_D08.setText(str(t03_d08)) # Fila 08
        self.ui.lineEdit_Tabla03_D09.setText(str(t03_d09)) # Fila 09
        self.ui.lineEdit_Tabla03_D10.setText(str(t03_d10)) # Fila 10
        self.ui.lineEdit_Tabla03_D11.setText(str(t03_d11)) # Fila 11
        self.ui.lineEdit_Tabla03_D12.setText(str(t03_d12)) # Fila 12
        self.ui.lineEdit_Tabla03_D13.setText(str(t03_d13)) # Fila 13
        self.ui.lineEdit_Tabla03_D14.setText(str(t03_d14)) # Fila 14
        self.ui.lineEdit_Tabla03_D15.setText(str(t03_d15)) # Fila 15
        self.ui.lineEdit_Tabla03_D16.setText(str(t03_d16)) # Fila 16
        self.ui.lineEdit_Tabla03_D17.setText(str(t03_d17)) # Fila 17
        self.ui.lineEdit_Tabla03_D18.setText(str(t03_d18)) # Fila 18
        self.ui.lineEdit_Tabla03_D19.setText(str(t03_d19)) # Fila 19
        self.ui.lineEdit_Tabla03_D20.setText(str(t03_d20)) # Fila 20
        self.ui.lineEdit_Tabla03_D21.setText(str(t03_d21)) # Fila 21
        self.ui.lineEdit_Tabla03_D22.setText(str(t03_d22)) # Fila 22

        # (0.088*D33^2-0.086*D33+0.017)*1000000
        t03_c02 = (0.088*t03_d02**2-0.086*t03_d02+0.017)*1000000 # Fila 02
        t03_c03 = (0.088*t03_d03**2-0.086*t03_d03+0.017)*1000000 # Fila 03
        t03_c04 = (0.088*t03_d04**2-0.086*t03_d04+0.017)*1000000 # Fila 04
        t03_c05 = (0.088*t03_d05**2-0.086*t03_d05+0.017)*1000000 # Fila 05
        t03_c06 = (0.088*t03_d06**2-0.086*t03_d06+0.017)*1000000 # Fila 06
        t03_c07 = (0.088*t03_d07**2-0.086*t03_d07+0.017)*1000000 # Fila 07
        t03_c08 = (0.088*t03_d08**2-0.086*t03_d08+0.017)*1000000 # Fila 08
        t03_c09 = (0.088*t03_d09**2-0.086*t03_d09+0.017)*1000000 # Fila 09
        t03_c10 = (0.088*t03_d10**2-0.086*t03_d10+0.017)*1000000 # Fila 10
        t03_c11 = (0.088*t03_d11**2-0.086*t03_d11+0.017)*1000000 # Fila 11
        t03_c12 = (0.088*t03_d12**2-0.086*t03_d12+0.017)*1000000 # Fila 12
        t03_c13 = (0.088*t03_d13**2-0.086*t03_d13+0.017)*1000000 # Fila 13
        t03_c14 = (0.088*t03_d14**2-0.086*t03_d14+0.017)*1000000 # Fila 14
        t03_c15 = (0.088*t03_d15**2-0.086*t03_d15+0.017)*1000000 # Fila 15
        t03_c16 = (0.088*t03_d16**2-0.086*t03_d16+0.017)*1000000 # Fila 16
        t03_c17 = (0.088*t03_d17**2-0.086*t03_d17+0.017)*1000000 # Fila 17
        t03_c18 = (0.088*t03_d18**2-0.086*t03_d18+0.017)*1000000 # Fila 18
        t03_c19 = (0.088*t03_d19**2-0.086*t03_d19+0.017)*1000000 # Fila 19
        t03_c20 = (0.088*t03_d20**2-0.086*t03_d20+0.017)*1000000 # Fila 20
        t03_c21 = (0.088*t03_d21**2-0.086*t03_d21+0.017)*1000000 # Fila 21
        t03_c22 = (0.088*t03_d22**2-0.086*t03_d22+0.017)*1000000 # Fila 22

        self.ui.lineEdit_Tabla03_C02.setText(str(t03_c02)) # Fila 02
        self.ui.lineEdit_Tabla03_C03.setText(str(t03_c03)) # Fila 03
        self.ui.lineEdit_Tabla03_C04.setText(str(t03_c04)) # Fila 04
        self.ui.lineEdit_Tabla03_C05.setText(str(t03_c05)) # Fila 05
        self.ui.lineEdit_Tabla03_C06.setText(str(t03_c06)) # Fila 06
        self.ui.lineEdit_Tabla03_C07.setText(str(t03_c07)) # Fila 07
        self.ui.lineEdit_Tabla03_C08.setText(str(t03_c08)) # Fila 08
        self.ui.lineEdit_Tabla03_C09.setText(str(t03_c09)) # Fila 09
        self.ui.lineEdit_Tabla03_C10.setText(str(t03_c10)) # Fila 10
        self.ui.lineEdit_Tabla03_C11.setText(str(t03_c11)) # Fila 11
        self.ui.lineEdit_Tabla03_C12.setText(str(t03_c12)) # Fila 12
        self.ui.lineEdit_Tabla03_C13.setText(str(t03_c13)) # Fila 13
        self.ui.lineEdit_Tabla03_C14.setText(str(t03_c14)) # Fila 14
        self.ui.lineEdit_Tabla03_C15.setText(str(t03_c15)) # Fila 15
        self.ui.lineEdit_Tabla03_C16.setText(str(t03_c16)) # Fila 16
        self.ui.lineEdit_Tabla03_C17.setText(str(t03_c17)) # Fila 17
        self.ui.lineEdit_Tabla03_C18.setText(str(t03_c18)) # Fila 18
        self.ui.lineEdit_Tabla03_C19.setText(str(t03_c19)) # Fila 19
        self.ui.lineEdit_Tabla03_C20.setText(str(t03_c20)) # Fila 20
        self.ui.lineEdit_Tabla03_C21.setText(str(t03_c21)) # Fila 21
        self.ui.lineEdit_Tabla03_C22.setText(str(t03_c22)) # Fila 22

        # =(2.35*D33^2+8.5*D33-2)*10000
        t03_b02 = (2.35*t03_d02**2+8.5*t03_d02-2)*10000 # Fila 02
        t03_b03 = (2.35*t03_d03**2+8.5*t03_d03-2)*10000 # Fila 03
        t03_b04 = (2.35*t03_d04**2+8.5*t03_d04-2)*10000 # Fila 04
        t03_b05 = (2.35*t03_d05**2+8.5*t03_d05-2)*10000 # Fila 05
        t03_b06 = (2.35*t03_d06**2+8.5*t03_d06-2)*10000 # Fila 06
        t03_b07 = (2.35*t03_d07**2+8.5*t03_d07-2)*10000 # Fila 07
        t03_b08 = (2.35*t03_d08**2+8.5*t03_d08-2)*10000 # Fila 08
        t03_b09 = (2.35*t03_d09**2+8.5*t03_d09-2)*10000 # Fila 09
        t03_b10 = (2.35*t03_d10**2+8.5*t03_d10-2)*10000 # Fila 10
        t03_b11 = (2.35*t03_d11**2+8.5*t03_d11-2)*10000 # Fila 11
        t03_b12 = (2.35*t03_d12**2+8.5*t03_d12-2)*10000 # Fila 12
        t03_b13 = (2.35*t03_d13**2+8.5*t03_d13-2)*10000 # Fila 13
        t03_b14 = (2.35*t03_d14**2+8.5*t03_d14-2)*10000 # Fila 14
        t03_b15 = (2.35*t03_d15**2+8.5*t03_d15-2)*10000 # Fila 15
        t03_b16 = (2.35*t03_d16**2+8.5*t03_d16-2)*10000 # Fila 16
        t03_b17 = (2.35*t03_d17**2+8.5*t03_d17-2)*10000 # Fila 17
        t03_b18 = (2.35*t03_d18**2+8.5*t03_d18-2)*10000 # Fila 18
        t03_b19 = (2.35*t03_d19**2+8.5*t03_d19-2)*10000 # Fila 19
        t03_b20 = (2.35*t03_d20**2+8.5*t03_d20-2)*10000 # Fila 20
        t03_b21 = (2.35*t03_d21**2+8.5*t03_d21-2)*10000 # Fila 21
        t03_b22 = (2.35*t03_d22**2+8.5*t03_d22-2)*10000 # Fila 22

        self.ui.lineEdit_Tabla03_B02.setText(str(t03_b02)) # Fila 02
        self.ui.lineEdit_Tabla03_B03.setText(str(t03_b03)) # Fila 03
        self.ui.lineEdit_Tabla03_B04.setText(str(t03_b04)) # Fila 04
        self.ui.lineEdit_Tabla03_B05.setText(str(t03_b05)) # Fila 05
        self.ui.lineEdit_Tabla03_B06.setText(str(t03_b06)) # Fila 06
        self.ui.lineEdit_Tabla03_B07.setText(str(t03_b07)) # Fila 07
        self.ui.lineEdit_Tabla03_B08.setText(str(t03_b08)) # Fila 08
        self.ui.lineEdit_Tabla03_B09.setText(str(t03_b09)) # Fila 09
        self.ui.lineEdit_Tabla03_B10.setText(str(t03_b10)) # Fila 10
        self.ui.lineEdit_Tabla03_B11.setText(str(t03_b11)) # Fila 11
        self.ui.lineEdit_Tabla03_B12.setText(str(t03_b12)) # Fila 12
        self.ui.lineEdit_Tabla03_B13.setText(str(t03_b13)) # Fila 13
        self.ui.lineEdit_Tabla03_B14.setText(str(t03_b14)) # Fila 14
        self.ui.lineEdit_Tabla03_B15.setText(str(t03_b15)) # Fila 15
        self.ui.lineEdit_Tabla03_B16.setText(str(t03_b16)) # Fila 16
        self.ui.lineEdit_Tabla03_B17.setText(str(t03_b17)) # Fila 17
        self.ui.lineEdit_Tabla03_B18.setText(str(t03_b18)) # Fila 18
        self.ui.lineEdit_Tabla03_B19.setText(str(t03_b19)) # Fila 19
        self.ui.lineEdit_Tabla03_B20.setText(str(t03_b20)) # Fila 20
        self.ui.lineEdit_Tabla03_B21.setText(str(t03_b21)) # Fila 21
        self.ui.lineEdit_Tabla03_B22.setText(str(t03_b22)) # Fila 22
        


    
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())