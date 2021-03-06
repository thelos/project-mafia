# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 700)
        MainWindow.setMinimumSize(QtCore.QSize(886, 700))
        MainWindow.setMaximumSize(QtCore.QSize(886, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bandit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-image: url(mafia.jpg) ;\n"
"}\n"
"QTabWidget{\n"
"    background-image: url(mafia.jpg) ;\n"
"}\n"
"    font: 8pt \"MV Boli\";")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 150, 592, 420))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(5)
        self._2.setObjectName("_2")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableofrooms = QtWidgets.QTableWidget(self.tab)
        self.tableofrooms.setGeometry(QtCore.QRect(10, 10, 571, 341))
        self.tableofrooms.setStyleSheet("")
        self.tableofrooms.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableofrooms.setObjectName("tableofrooms")
        self.tableofrooms.setColumnCount(5)
        self.tableofrooms.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableofrooms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableofrooms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableofrooms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableofrooms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setItalic(False)
        item.setFont(font)
        self.tableofrooms.setHorizontalHeaderItem(4, item)
        self.creationButthon = QtWidgets.QPushButton(self.tab)
        self.creationButthon.setGeometry(QtCore.QRect(10, 360, 571, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.creationButthon.setFont(font)
        self.creationButthon.setStyleSheet("")
        self.creationButthon.setObjectName("creationButthon")
        self.reboot = QtWidgets.QPushButton(self.tab)
        self.reboot.setGeometry(QtCore.QRect(550, 10, 31, 21))
        self.reboot.setStyleSheet("")
        self.reboot.setObjectName("reboot")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ChatHistory_Main = QtWidgets.QTextBrowser(self.tab_3)
        self.ChatHistory_Main.setGeometry(QtCore.QRect(10, 10, 561, 321))
        self.ChatHistory_Main.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.ChatHistory_Main.setObjectName("ChatHistory_Main")
        self.messageLineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.messageLineEdit_2.setGeometry(QtCore.QRect(70, 340, 411, 20))
        self.messageLineEdit_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.messageLineEdit_2.setObjectName("messageLineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(0, 320, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sendButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.sendButton_2.setGeometry(QtCore.QRect(490, 340, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton_2.sizePolicy().hasHeightForWidth())
        self.sendButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sendButton_2.setFont(font)
        self.sendButton_2.setWhatsThis("")
        self.sendButton_2.setStyleSheet("")
        self.sendButton_2.setObjectName("sendButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ChatHistory_Role = QtWidgets.QTextBrowser(self.tab_2)
        self.ChatHistory_Role.setGeometry(QtCore.QRect(10, 10, 561, 321))
        self.ChatHistory_Role.setObjectName("ChatHistory_Role")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 91, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.messageLineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.messageLineEdit_3.setGeometry(QtCore.QRect(70, 340, 411, 20))
        self.messageLineEdit_3.setObjectName("messageLineEdit_3")
        self.sendButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.sendButton_3.setGeometry(QtCore.QRect(490, 340, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton_3.sizePolicy().hasHeightForWidth())
        self.sendButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sendButton_3.setFont(font)
        self.sendButton_3.setWhatsThis("")
        self.sendButton_3.setStyleSheet("")
        self.sendButton_3.setObjectName("sendButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        self._2.addWidget(self.tabWidget)
        self.vboxlayout.addLayout(self._2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 21))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mafia"))
        item = self.tableofrooms.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableofrooms.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "admin"))
        item = self.tableofrooms.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Member/Max member"))
        item = self.tableofrooms.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "password"))
        item = self.tableofrooms.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "started?"))
        self.creationButthon.setText(_translate("MainWindow", "CreateNewRoom"))
        self.reboot.setText(_translate("MainWindow", "۞"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Rooms"))
        self.ChatHistory_Main.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Message:"))
        self.sendButton_2.setToolTip(_translate("MainWindow", "Sends a message to other people"))
        self.sendButton_2.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "MainChat"))
        self.label_5.setText(_translate("MainWindow", "Message:"))
        self.sendButton_3.setToolTip(_translate("MainWindow", "Sends a message to other people"))
        self.sendButton_3.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "RoleChat"))
        self.menuGame.setTitle(_translate("MainWindow", "Game"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "About Us"))

