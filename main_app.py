from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, \
    QMessageBox
from PyQt6 import uic
from time import sleep
from random import randint

Form, Window = uic.loadUiType("gui.ui")


class Logic(Form):
    def __init__(self):
        super().__init__()

        self.window = Window()
        self.setupUi(self.window)
        self.connects()
        self.events()
        self.window.show()

    def connects(self):
        pass

    def events(self):
        self.dogfight_btn.mousePressEvent = self.check
        self.dogfight_btn.mouseReleaseEvent = self.draw

    def check(self, *args):
        self.result.setText('Рукопашный бой')
        self.dogfight_btn.setStyleSheet("color : white;"
                                        "background-color : blue;")


    def draw(self, *args):
        self.dogfight_btn.setStyleSheet("background-color : none")


app = QApplication([])
#window = Window()
form = Logic()
# form.setupUi(window)

#window.show()
app.exec()
