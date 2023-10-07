from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QDial
from PyQt6.QtCore import QRect,Qt
from PyQt6.QtGui import QIcon,QPixmap
from sys import argv,exit
from widgets.miniCalc import CalcWindow


if __name__ == "__main__":
    app = QApplication(argv)
    sg = CalcWindow()
    sg.show()
    exit(app.exec())