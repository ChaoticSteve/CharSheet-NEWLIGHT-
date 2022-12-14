from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
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

    def roll_d100(self):
        return randint(1, 100)

    def roll_d20(self):
        return randint(1, 20)

    def connects(self):
        self.strength_p.textChanged.connect(self.get_strength)
        self.strength_b.textChanged.connect(self.get_strength)
        self.agility_p.textChanged.connect(self.get_agility)
        self.agility_b.textChanged.connect(self.get_agility)
        self.dogfight_history.textChanged.connect(self.get_dogfight)
        self.dogfight_bonus.textChanged.connect(self.get_dogfight)
        self.dogfight_skill.textChanged.connect(self.get_dogfight)
        self.dagger_history.textChanged.connect(self.get_dagger)
        self.dagger_bonus.textChanged.connect(self.get_dagger)
        self.dagger_skill.textChanged.connect(self.get_dagger)
        self.sword_history.textChanged.connect(self.get_sword)
        self.sword_bonus.textChanged.connect(self.get_sword)
        self.sword_skill.textChanged.connect(self.get_sword)

    def events(self):
        self.dogfight_btn.mousePressEvent = self.check_dogfight
        self.dogfight_btn.mouseReleaseEvent = self.draw_dogfight
        self.dagger_btn.mousePressEvent = self.check_dagger
        self.dagger_btn.mouseReleaseEvent = self.draw_dagger
        self.sword_btn.mousePressEvent = self.check_sword
        self.sword_btn.mouseReleaseEvent = self.draw_sword

    def check_dogfight(self, ev):
        dice = self.roll_d100()
        if 1 <= dice <= 5:
            self.result.setText(f'Крит успех! Результат броска {str(dice)}')
        elif dice <= float(self.dogfight.text()):
            self.result.setText(f'Успех! Результат броска {str(dice)}')
        elif 95 <= dice <= 100:
            self.result.setText(f'Крит провал! Результат броска {str(dice)}')
        else:
            self.result.setText(f'Провал! Результат броска {str(dice)}')
        self.dogfight_btn.setStyleSheet("color : white;"
                                        "background-color : blue;")

    def draw_dogfight(self, ev):
        self.dogfight_btn.setStyleSheet("background-color : none")

    def check_dagger(self, ev):
        dice = self.roll_d100()
        if 1 <= dice <= 5:
            self.result.setText(f'Крит успех! Результат броска {str(dice)}')
        elif dice <= float(self.dagger.text()):
            self.result.setText(f'Успех! Результат броска {str(dice)}')
        elif 95 <= dice <= 100:
            self.result.setText(f'Крит провал! Результат броска {str(dice)}')
        else:
            self.result.setText(f'Провал! Результат броска {str(dice)}')
        self.dagger_btn.setStyleSheet("color : white;"
                                      "background-color : blue;")

    def draw_dagger(self, ev):
        self.dagger_btn.setStyleSheet("background-color : none")
    def check_sword(self, ev):
        dice = self.roll_d100()
        if 1 <= dice <= 5:
            self.result.setText(f'Крит успех! Результат броска {str(dice)}')
        elif dice <= float(self.sword.text()):
            self.result.setText(f'Успех! Результат броска {str(dice)}')
        elif 95 <= dice <= 100:
            self.result.setText(f'Крит провал! Результат броска {str(dice)}')
        else:
            self.result.setText(f'Провал! Результат броска {str(dice)}')
        self.sword_btn.setStyleSheet("color : white;"
                                      "background-color : blue;")

    def draw_sword(self, ev):
        self.sword_btn.setStyleSheet("background-color : none")

    def get_strength(self):
        if self.strength_p.text().isdigit() and self.strength_b.text().isdigit():
            self.strength.setText(str(int(self.strength_p.text()) + int(self.strength_b.text())))
        elif self.strength_p.text() == '' and self.strength_b.text() == '':
            self.strength.setText('0')
        self.get_dogfight()
        self.get_sword()

    def get_agility(self):
        if self.agility_p.text().isdigit() and self.agility_b.text().isdigit():
            self.agility.setText(str(int(self.agility_p.text()) + int(self.agility_b.text())))
        elif self.agility_p.text() == '' and self.agility_b.text() == '':
            self.agility.setText('0')
        self.get_dogfight()
        self.get_dagger()
        self.get_sword()

    def get_dogfight(self):
        if self.dogfight_history.text().isdigit() and self.dogfight_skill.text().isdigit() \
                and self.dogfight_bonus.text().isdigit():
            self.dogfight.setText(str(10 + int(self.strength.text()) * 1.5 + int(self.agility.text()) / 2 +
                                      int(self.dogfight_history.text()) + int(self.dogfight_bonus.text()) +
                                      int(self.dogfight_skill.text())))

    def get_dagger(self):
        if self.dagger_history.text().isdigit() and self.dagger_skill.text().isdigit() \
                and self.dagger_bonus.text().isdigit():
            self.dagger.setText(str(int(self.agility.text()) * 2 + int(self.dagger_history.text()) +
                                    int(self.dagger_bonus.text()) + int(self.dagger_skill.text())))

    def get_sword(self):
        if self.sword_history.text().isdigit() and self.sword_skill.text().isdigit() \
                and self.sword_bonus.text().isdigit():
            self.sword.setText(str(int(self.strength.text()) + int(self.agility.text()) + int(self.sword_history.text()) +
                                int(self.sword_skill.text()) + int(self.sword_bonus.text())))

app = QApplication([])
# window = Window()
form = Logic()
# form.setupUi(window)

# window.show()
app.exec()
