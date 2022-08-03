from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,
                             QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()

    def set_apper(self):
        self.setWindowTitle(win_title)
        self.resize(win_w, win_h)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.v_line1 = QVBoxLayout()
        self.v_line1.addWidget(QLabel('Навыки'), alignment=Qt.AlignCenter)
        self.v_line1.addWidget(QLabel('Имя'))
        self.v_line1.addWidget(QLabel('Раса'))
        self.v_line1.addWidget(QLabel('Очки Развития'))
        self.v_line1.addWidget(QLabel('Репутация'))
        self.v_line1.addWidget(QLabel('Деньги'))
        self.v_line1.addWidget(QLabel('Сила'))
        self.v_line1.addWidget(QLabel('Телосложение'))
        self.v_line1.addWidget(QLabel('Ловкость'))
        self.v_line1.addWidget(QLabel('Харизма'))
        self.v_line1.addWidget(QLabel('Интеллект'))
        self.v_line1.addWidget(QLabel('Воля'))
        self.v_line1.addWidget(QLabel('Очки характиристик'))
        self.v_line1.addWidget(QLabel('Очки навыков'))
        self.v_line1.addWidget(QLabel('Здоровье'))
        self.v_line1.addWidget(QLabel('Бодрость'))
        self.v_line1.addWidget(QLabel('Инициатива'))
        self.v_line1.addWidget(QLabel('Скорость'))
        self.v_line1.addWidget(QLabel('Край жизни'))
        self.h_line.addLayout(self.v_line1)
        self.v_line2 = QVBoxLayout()
        self.name = QLineEdit('Имя персонажа')
        self.race = QLineEdit('Раса')
        self.ev_point = QLineEdit('Очки развития')
        self.reputation = QLineEdit('Репутация')
        self.money = QLineEdit('Деньги')
        self.v_line2.addWidget(self.name)
        self.v_line2.addWidget(self.race)
        self.v_line2.addWidget(self.ev_point)
        self.v_line2.addWidget(self.reputation)
        self.v_line2.addWidget(self.money)
        self.h_line.addLayout(self.v_line2)
        self.setLayout(self.h_line)


    def connects(self):
        pass


app = QApplication([])
mw = MainWin()
app.exec_()
