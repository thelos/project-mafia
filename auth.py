# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 620)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../PycharmProjects/Project_S/venv/bandit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AuthVkButton = QtWidgets.QPushButton(self.centralwidget)
        self.AuthVkButton.setGeometry(QtCore.QRect(270, 210, 311, 51))
        self.AuthVkButton.setObjectName("AuthVkButton")
        self.AuthTokenButton = QtWidgets.QPushButton(self.centralwidget)
        self.AuthTokenButton.setGeometry(QtCore.QRect(270, 270, 311, 51))
        self.AuthTokenButton.setObjectName("AuthTokenButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Authorization"))
        self.AuthVkButton.setText(_translate("MainWindow", "Авторизация через Вк"))
        self.AuthTokenButton.setText(_translate("MainWindow", "Авторизация через Токен"))
