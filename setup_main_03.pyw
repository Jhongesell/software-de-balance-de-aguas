import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog
from UI.option03_main import *
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
        self.ui.actionSubWindow_View.triggered.connect(self.SubWindow_View)
        self.ui.actionTabbed_View.triggered.connect(self.Tabbed_View)
        self.ui.actionCascade_View.triggered.connect(self.cascadeArrange)
        self.ui.actionTile_View.triggered.connect(self.tileArrange)

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
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())