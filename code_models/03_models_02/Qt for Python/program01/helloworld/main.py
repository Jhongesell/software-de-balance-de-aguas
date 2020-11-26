# This Python file uses the following encoding: utf-8
import sys
# from PySide2.QtWidgets import QApplication
from PySide2 import QtCore, QtWidgets


if __name__ == "__main__":
    #app = QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    message = "hello world\nPySide2 using Qt {}".format(QtCore.qVersion())
    label = QtWidgets.QLabel(message)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.resize(400, 300)
    label.show()
    # ...
    sys.exit(app.exec_())
