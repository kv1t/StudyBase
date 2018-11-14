import sys
import gui
import functions
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class main(QMainWindow, gui.Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_0.clicked.connect(self.buttonClicked)
        self.pushButton_1.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.buttonClicked)
        self.pushButton_3.clicked.connect(self.buttonClicked)
        self.pushButton_4.clicked.connect(self.buttonClicked)
        self.pushButton_5.clicked.connect(self.buttonClicked)
        self.pushButton_6.clicked.connect(self.buttonClicked)
        self.pushButton_7.clicked.connect(self.buttonClicked)
        self.pushButton_8.clicked.connect(self.buttonClicked)
        self.pushButton_9.clicked.connect(self.buttonClicked)
        self.pushButton_dot.clicked.connect(self.buttonClicked)
        self.pushButton_chson.clicked.connect(self.buttonClicked)
        self.pushButton_div.clicked.connect(self.buttonClicked)
        self.pushButton_add.clicked.connect(self.buttonClicked)
        self.pushButton_sub.clicked.connect(self.buttonClicked)
        self.pushButton_mult.clicked.connect(self.buttonClicked)
        self.pushButton_sqr.clicked.connect(self.buttonClicked)
        self.pushButton_oneDiv.clicked.connect(self.buttonClicked)
        self.pushButton_equal.clicked.connect(self.buttonClicked)
        self.pushButton_c.clicked.connect(self.buttonClicked)

    def funcExec(self):
        if self.label.text() == '/':
            try:
                self.lcdNumber_previous.display(functions.div(self.lcdNumber_previous.value(),self.lcdNumber.value()))
                self.lcdNumber.display(0)
                self.line.setEnabled(True)
            except Exception:
                self.lcdNumber_previous.display(0)
                self.lcdNumber.display(0)
                self.label.setText('')
                self.label_error.setText('Error division by zero')
                self.line.setEnabled(True)
        elif self.label.text() == '+':
            self.lcdNumber_previous.display(functions.add(self.lcdNumber_previous.value(),self.lcdNumber.value()))
            self.label.setText('')
            self.lcdNumber.display(0)
            self.line.setEnabled(True)
        elif self.label.text() == '-':
            self.lcdNumber_previous.display(functions.sub(self.lcdNumber_previous.value(),self.lcdNumber.value()))
            self.label.setText('')
            self.lcdNumber.display(0)
            self.line.setEnabled(True)
        elif self.label.text() == '*':
            self.lcdNumber_previous.display(functions.mult(self.lcdNumber_previous.value(),self.lcdNumber.value()))
            self.label.setText('')
            self.lcdNumber.display(0)
            self.line.setEnabled(True)


    def buttonClicked(self):
        sender = self.sender()
        self.label_error.setText('')
        isInput = True

        try:
#            print(sender.text())
            num = int(sender.text())
            if self.line.isEnabled() == True:
#                print(True)
                self.lcdNumber.display(int(str(self.lcdNumber.intValue()) + sender.text()))
            else:
                if self.pushButton_dot.isEnabled() == False:
                    self.lcdNumber.display(float(str(self.lcdNumber.value())[:-1] + sender.text()))
                    self.pushButton_dot.setEnabled(True)
                else:
                    self.lcdNumber.display(float(str(self.lcdNumber.value()) + sender.text()))
        except Exception:
            isInput = False


        if isInput == False:
            if sender.objectName() == 'pushButton_chson':
                if self.line.isEnabled() == True:
                    self.lcdNumber.display(self.lcdNumber.intValue() * -1)
                else:
                    self.lcdNumber.display(self.lcdNumber.value() * -1)
            elif sender.objectName() == 'pushButton_div':
                if self.lcdNumber_previous.value() == 0:
                    self.lcdNumber_previous.display(self.lcdNumber.value())
                    self.label.setText('/')
                    self.lcdNumber.display(0)
                    self.line.setEnabled(True)
                else:
                    self.funcExec()
                    self.label.setText('/')
                    self.lcdNumber.display(0)
            elif sender.objectName() == 'pushButton_add':
                if self.lcdNumber_previous.value() == 0:
                    self.lcdNumber_previous.display(self.lcdNumber.value())
                    self.label.setText('+')
                    self.lcdNumber.display(0)
                    self.line.setEnabled(True)
                else:
                    self.funcExec()
                    self.label.setText('+')
                    self.lcdNumber.display(0)
            elif sender.objectName() == 'pushButton_sub':
                if self.lcdNumber_previous.value() == 0:
                    self.lcdNumber_previous.display(self.lcdNumber.value())
                    self.label.setText('-')
                    self.lcdNumber.display(0)
                    self.line.setEnabled(True)
                else:
                    self.funcExec()
                    self.label.setText('-')
                    self.lcdNumber.display(0)
            elif sender.objectName() == 'pushButton_mult':
                if self.lcdNumber_previous.value() == 0:
                    self.lcdNumber_previous.display(self.lcdNumber.value())
                    self.label.setText('*')
                    self.lcdNumber.display(0)
                    self.line.setEnabled(True)
                else:
                    self.funcExec()
                    self.label.setText('*')
                    self.lcdNumber.display(0)
            elif sender.objectName() == 'pushButton_sqr':
                try:
                    self.line.setEnabled(False)
                    self.lcdNumber.display(functions.sqr(self.lcdNumber.value()))
                except Exception:
                    self.lcdNumber.display(0)
                    self.label_error.setText('No real roots')
            elif sender.objectName() == 'pushButton_oneDiv':
                try:
                    self.line.setEnabled(False)
                    self.lcdNumber.display(functions.oneDiv(self.lcdNumber.value()))
                except ZeroDivisionError:
                    self.lcdNumber.display(0)
                    self.label_error.setText('Error division by zero')
            elif sender.objectName() == 'pushButton_equal':
                if self.lcdNumber_previous.intValue() == 0 and self.lcdNumber_previous.value() == 0:
                    pass
                else:
                    self.funcExec()
                    self.lcdNumber.display(self.lcdNumber_previous.value())
                    self.lcdNumber_previous.display(0)
            elif sender.objectName() == 'pushButton_dot':
                if self.line.isEnabled() == True:
                    self.pushButton_dot.setEnabled(False)
                self.line.setEnabled(False)
            elif sender.objectName() == 'pushButton_c':
                self.lcdNumber.display(0)
                self.lcdNumber_previous.display(0)
                self.label.setText('')
                self.line.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = main()
    form.show()
    app.exec()