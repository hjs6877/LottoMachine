import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("../../ui/hello.ui", self)
        self.ui.show()


    @pyqtSlot()
    def test_slot1(self):
        self.ui.label1.setText("Good Morning")

    @pyqtSlot()
    def test_slot2(self):
        self.ui.label2.setText("Good Afternoon")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())