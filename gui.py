import typing
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QWidget

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("organizerGUI.ui", self)
        self.show()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()


if __name__ == '__main__':
    main()

