# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setWindowModality(QtCore.Qt.NonModal)
        Calculator.resize(240, 250)
        Calculator.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 100, 31, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 100, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 100, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 130, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 130, 31, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 130, 31, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 160, 31, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 160, 31, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 160, 31, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 190, 71, 23))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(90, 190, 31, 23))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_chson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_chson.setGeometry(QtCore.QRect(50, 70, 31, 23))
        self.pushButton_chson.setObjectName("pushButton_chson")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(140, 190, 31, 23))
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(140, 100, 31, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(140, 130, 31, 23))
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_mult = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mult.setGeometry(QtCore.QRect(140, 160, 31, 23))
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.pushButton_sqr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqr.setGeometry(QtCore.QRect(190, 130, 31, 23))
        self.pushButton_sqr.setObjectName("pushButton_sqr")
        self.pushButton_oneDiv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_oneDiv.setGeometry(QtCore.QRect(190, 100, 31, 23))
        self.pushButton_oneDiv.setObjectName("pushButton_oneDiv")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(190, 160, 31, 51))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 40, 221, 21))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(9)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_previous = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_previous.setGeometry(QtCore.QRect(10, 10, 181, 23))
        self.lcdNumber_previous.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcdNumber_previous.setSmallDecimalPoint(True)
        self.lcdNumber_previous.setDigitCount(9)
        self.lcdNumber_previous.setObjectName("lcdNumber_previous")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(90, 70, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_error.setPalette(palette)
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c.setEnabled(True)
        self.pushButton_c.setGeometry(QtCore.QRect(10, 70, 31, 23))
        self.pushButton_c.setObjectName("pushButton_c")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(20, 220, 201, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        Calculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_dot.setText(_translate("Calculator", "."))
        self.pushButton_chson.setText(_translate("Calculator", "±"))
        self.pushButton_div.setText(_translate("Calculator", "/"))
        self.pushButton_add.setText(_translate("Calculator", "+"))
        self.pushButton_sub.setText(_translate("Calculator", "-"))
        self.pushButton_mult.setText(_translate("Calculator", "*"))
        self.pushButton_sqr.setText(_translate("Calculator", "sqr"))
        self.pushButton_oneDiv.setText(_translate("Calculator", "1/x"))
        self.pushButton_equal.setText(_translate("Calculator", "="))
        self.pushButton_c.setText(_translate("Calculator", "C"))
