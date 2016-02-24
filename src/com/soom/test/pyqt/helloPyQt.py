import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(550, 350)
    w.move(300, 300)
    w.setWindowTitle('Hello World')
    w.setToolTip("Hello PyQt5!!")
    w.show()

    sys.exit(app.exec_())