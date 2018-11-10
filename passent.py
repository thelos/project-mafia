# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passenter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 170)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bandit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-image: url(ae.jpg) ;\n"
"color: rgb(202, 0, 0);")
        self.enter = QtWidgets.QPushButton(Dialog)
        self.enter.setGeometry(QtCore.QRect(80, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 281, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enter.setText(_translate("Dialog", "Enter"))

