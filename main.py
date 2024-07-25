import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from menu import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(("Icon_calc.ico")))
        self.stroka = ""
        self.flagBracket = 0
        self.ui.pushButton_0.clicked.connect(self.click_0)
        self.ui.pushButton_1.clicked.connect(self.click_1)
        self.ui.pushButton_2.clicked.connect(self.click_2)
        self.ui.pushButton_3.clicked.connect(self.click_3)
        self.ui.pushButton_4.clicked.connect(self.click_4)
        self.ui.pushButton_5.clicked.connect(self.click_5)
        self.ui.pushButton_6.clicked.connect(self.click_6)
        self.ui.pushButton_7.clicked.connect(self.click_7)
        self.ui.pushButton_8.clicked.connect(self.click_8)
        self.ui.pushButton_9.clicked.connect(self.click_9)
        self.ui.pushButton_add.clicked.connect(self.click_add)
        self.ui.pushButton_qual_to.clicked.connect(self.click_qual_to)
        self.ui.pushButton_delete_symvol.clicked.connect(
            self.click_delete_symvol)
        self.ui.pushButton_bracket.clicked.connect(self.click_bracket)
        self.ui.pushButton_delete_str.clicked.connect(self.clicl_delete_str)
        self.ui.pushButton_minus.clicked.connect(self.click_minus)
        self.ui.pushButton_multiplication.clicked.connect(
            self.click_multiplication)
        self.ui.pushButton_division.clicked.connect(self.click_division)
        self.ui.pushButton_comma.clicked.connect(self.click_comma)
        self.ui.pushButton_procent.clicked.connect(self.click_procent)
        self.ui.lineEdit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        if (self.ui.lineEdit.hasFocus()):
            self.stroka += self.ui.lineEdit.text()[-1]
            print(self.stroka)

    def click_procent(self):
        self.ui.label.setText("% Дорабатывается")

    def click_comma(self):
        self.stroka += "."
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_division(self):
        self.stroka += "/"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_multiplication(self):
        self.stroka += "*"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_minus(self):
        self.stroka += "-"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def clicl_delete_str(self):
        self.stroka = ""
        self.ui.label.clear()
        self.ui.lineEdit.clear()

    def click_bracket(self):
        if (self.flagBracket == 0):
            self.stroka += "("
            self.flagBracket = 1
            self.ui.lineEdit.setText(self.stroka)
        else:
            self.stroka += ")"
            self.flagBracket = 0
            self.ui.lineEdit.setText(self.stroka)

    def click_0(self):
        self.stroka += "0"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_1(self):
        self.stroka += "1"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_2(self):
        self.stroka += "2"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_3(self):
        self.stroka += "3"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_4(self):
        self.stroka += "4"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_5(self):
        self.stroka += "5"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_6(self):
        self.stroka += "6"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_7(self):
        self.stroka += "7"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_8(self):
        self.stroka += "8"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_9(self):
        self.stroka += "9"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_add(self):
        self.stroka += "+"
        print(self.stroka)
        self.ui.lineEdit.setText(self.stroka)

    def click_qual_to(self):
        self.ui.label.setText("")
        try:
            for i in range(len(self.stroka)):
                if (not (self.stroka[i].isdecimal()) and self.stroka[i] == self.stroka[i+1]):
                    raise TypeError("Error!")
            str1 = eval(self.stroka)
            print(str1)
            self.ui.label.setText(str(str1))
            str1 = ""
        except ZeroDivisionError:
            self.ui.label.setText("division by zero")
        except TypeError:
            self.ui.label.setText("Error!")
        except:
            self.ui.label.setText("Error!")

    def click_delete_symvol(self):
        self.stroka = self.stroka[:-1]
        self.ui.lineEdit.setText(self.stroka)
        self.ui.label.clear()
        print(self.stroka)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setFixedSize(360,466)
    window.show()
    sys.exit(app.exec())
