# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatMainWindow(object):
    def setupUi(self, ChatMainWindow):
        ChatMainWindow.setObjectName("ChatMainWindow")
        ChatMainWindow.resize(610, 479)
        self.centralwidget = QtWidgets.QWidget(ChatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.chatHistory = QtWidgets.QTextBrowser(self.centralwidget)
        self.chatHistory.setAcceptDrops(False)
        self.chatHistory.setAcceptRichText(True)
        self.chatHistory.setObjectName("chatHistory")
        self.vboxlayout.addWidget(self.chatHistory)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(5)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.hboxlayout1.addWidget(self.label)
        self.messageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.messageLineEdit.setObjectName("messageLineEdit")
        self.hboxlayout1.addWidget(self.messageLineEdit)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setWhatsThis("")
        self.sendButton.setObjectName("sendButton")
        self.hboxlayout1.addWidget(self.sendButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)
        ChatMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChatMainWindow)
        self.statusbar.setObjectName("statusbar")
        ChatMainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(ChatMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAboutQt = QtWidgets.QAction(ChatMainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionChangeNickname = QtWidgets.QAction(ChatMainWindow)
        self.actionChangeNickname.setObjectName("actionChangeNickname")
        self.label.setBuddy(self.messageLineEdit)

        self.retranslateUi(ChatMainWindow)
        self.messageLineEdit.returnPressed.connect(self.sendButton.animateClick)
        self.actionQuit.triggered['bool'].connect(ChatMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ChatMainWindow)
        ChatMainWindow.setTabOrder(self.chatHistory, self.messageLineEdit)
        ChatMainWindow.setTabOrder(self.messageLineEdit, self.sendButton)

    def retranslateUi(self, ChatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatMainWindow.setWindowTitle(_translate("ChatMainWindow", "YourClassChat"))
        self.chatHistory.setToolTip(_translate("ChatMainWindow", "Messages sent and received from other users"))
        self.label.setText(_translate("ChatMainWindow", "Message:"))
        self.sendButton.setToolTip(_translate("ChatMainWindow", "Sends a message to other people"))
        self.sendButton.setText(_translate("ChatMainWindow", "Send"))
        self.actionQuit.setText(_translate("ChatMainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("ChatMainWindow", "Ctrl+Q"))
        self.actionAboutQt.setText(_translate("ChatMainWindow", "About Qt..."))
        self.actionChangeNickname.setText(_translate("ChatMainWindow", "Change nickname..."))
        self.actionChangeNickname.setShortcut(_translate("ChatMainWindow", "Ctrl+N"))

