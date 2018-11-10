# C:\Users\Гость\AppData\Local\Programs\Python\Python37-32\Scripts\pip.exe"
__author__ = 'TheLost'
import sys
# серверная часть
import webbrowser
from http.server import *

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidgetItem

# импорты форм
import ErrorMsg_mem
import authdialog
import creation
import errormessage
import mainwindow
import passent
# .
# импорт клиентских функций
from my_functions import GetAMainMessages, SendAMainMessage, GetSessionNumb, SendSessionNumberAndToken, AddOnline, \
    GetTabInformation, decoding, connect, connect_by_name, getbyconf
# .
# вк функции
from vkfunction import getfullandsecondname

# .

role = 'Citizen'
flag_serv = 0
certain = 0


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global flag_serv, certain
        self.count = self.path
        if flag_serv == 1:
            return
        flag_serv = 1
        get_url = "https://oauth.vk.com/access_token"
        get_payload = {"client_id": '6717045', 'client_secret': 'vxsLyG7QpfvUHnUeTmMB',
                       'redirect_uri': 'http://localhost:7200', 'code': self.count[7:]}
        get_request = requests.get(
            'https://oauth.vk.com/access_token?client_id=6717045&client_secret=vxsLyG7QpfvUHnUeTmMB&redirect_uri=http://localhost:7200&code=' + self.count[
                                                                                                                                                7:])
        certain = get_request.json()
        raise KeyboardInterrupt


class AThreadForServer(QThread):
    finished = pyqtSignal()

    def run(self):
        while True:
            try:
                self.serv = HTTPServer(('localhost', 7200), MyServer)
                self.serv.serve_forever()
            except KeyboardInterrupt:
                self.serv.server_close()
                self.finished.emit()
                break


class AMainThread(QThread):
    mainmessage = pyqtSignal(str)
    flag = 1
    conf = 0

    def run(self):
        while True:
            if self.flag == 1:
                self.ss = GetAMainMessages(self.conf).replace(';', ' - ')[4:]
                self.mainmessage.emit(self.ss)
            else:
                break
            self.sleep(4)

    def stop(self):
        self.flag = 0


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.dictofthreads = {
            'MainChatThread': AMainThread(),
        }
        self.flag_connection = 0
        self.count = 0
        self.token = ''
        self.sessionnumber = ''
        self.AuthDialog()
        self.InitUi()

        self.transltoTable()
        self.reboot.clicked.connect(self.transltoTable)
        self.flagrun = 0

    def AuthDialog(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = authdialog.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.pushButton.clicked.connect(self.AuthByVK)
        self.dialog.exec_()

    def creation_buffer(self):
        name = self.dialog.ui.lineEdit.text()
        maxmember = self.dialog.ui.lineEdit_2.text()
        password = self.dialog.ui.lineEdit_3.text()
        admin = self.id
        try:
            assert 6 <= int(maxmember) < 13
        except:
            self.dialog_err = QtWidgets.QDialog()
            self.dialog_err.ui = ErrorMsg_mem.Ui_Dialog()
            self.dialog_err.ui.setupUi(self.dialog_err)
            self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
            self.dialog_err.exec_()
            self.dialog.ui.lineEdit.clear()
            self.dialog.ui.lineEdit_2.clear()
            self.dialog.ui.lineEdit_3.clear()
            return

        l = GetTabInformation(self.dialog.ui.lineEdit.text(), self.dialog.ui.lineEdit_3.text(),
                              self.dialog.ui.lineEdit_2.text(), admin, self.sessionnumber)
        if l['invalidname'] == '1':
            self.dialog_err = QtWidgets.QDialog()
            self.dialog_err.ui = ErrorMsg_mem.Ui_Dialog()
            self.dialog_err.ui.setupUi(self.dialog_err)
            self.dialog_err.ui.textBrowser.setText('Комната с таким именем уже существует!')
            self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
            self.dialog_err.exec_()
            self.dialog.ui.lineEdit.clear()
            self.dialog.ui.lineEdit_2.clear()
            self.dialog.ui.lineEdit_3.clear()
            return
        self.conf = self.dialog.ui.lineEdit.text()
        self.flag_connection = 1
        self.flagrun = 1
        connect_by_name(self.conf, self.sessionnumber, self.id, self.dialog.ui.lineEdit_3.text())
        self.conf = getbyconf(self.conf)
        self.dictofthreads['MainChatThread'].conf = self.conf
        self.dialog.close()
        self.transltoTable()
        self.creationButthon.clicked.connect(self.passer)

    def creation(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = creation.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.pushButton.clicked.connect(self.creation_buffer)
        self.dialog.exec_()

    def passer(self):
        pass

    def InitUi(self):
        self.setupUi(self)
        self.tabWidget.currentChanged.connect(self.onch)
        self.creationButthon.clicked.connect(self.creation)

    def enter_helper(self):
        result = connect(self.row, self.sessionnumber, self.dialog.ui.lineEdit.text())
        if decoding(result['errors']) == 'No':
            self.dialog.close()

    def doubleclick(self, i, j):
        if not self.flag_connection:
            temp = self.tableofrooms.currentItem()
            self.row = temp.row()
            self.col = temp.column()
            if self.tableofrooms.item(self.row, self.col) == 'Yes':
                self.dialog = QtWidgets.QDialog()
                self.dialog.ui = passent.Ui_Dialog()
                self.dialog.ui.setupUi(self.dialog)
                self.dialog.ui.enter.clicked.connect(self.enter_helper)
                self.dialog.exec_()
            else:
                connect(self.row, self.sessionnumber)
            self.conf = self.row
            self.flag_connection = 1
            self.flagrun = 1
            self.dictofthreads['MainChatThread'].conf = self.conf

    def transltoTable(self):
        rowPosition = self.tableofrooms.rowCount()
        self.stack = GetTabInformation()
        self.names = decoding(self.stack['name']).split('$')
        self.members = decoding(self.stack['members']).split('$')
        self.passwords = decoding(self.stack['passwords']).split('$')
        self.started = decoding(self.stack['started']).split('$')
        self.admin = decoding(self.stack['admin']).split('$')
        for i in range(rowPosition):
            self.tableofrooms.removeRow(i)
        for i in range(len(self.names)):
            self.tableofrooms.insertRow(i)
            self.tableofrooms.setItem(i, 0, QTableWidgetItem(self.names[i]))
            self.tableofrooms.setItem(i, 1, QTableWidgetItem(self.admin[i]))
            self.tableofrooms.setItem(i, 2, QTableWidgetItem(self.members[i]))
            self.tableofrooms.setItem(i, 3, QTableWidgetItem(self.passwords[i]))
            self.tableofrooms.setItem(i, 4, QTableWidgetItem(self.started[i]))
        self.tableofrooms.cellDoubleClicked.connect(self.doubleclick)

    def onch(self, i):
        if i == 0:
            self.killthreads()
            self.transltoTable()
            self.reboot.clicked.connect(self.transltoTable)
        elif i == 1 and self.flagrun:
            self.sendButton_2.clicked.connect(self.send_main_msg)
            self.killthreads('MainChatThread')
            self.dictofthreads['MainChatThread'] = AMainThread()
            self.dictofthreads['MainChatThread'].mainmessage.connect(self.ChatHistory_Main.setText)
            self.dictofthreads['MainChatThread'].start()

    def send_main_msg(self):
        if self.flagrun:
            self.dictofthreads['MainChatThread'].msleep(4)
            self.ChatHistory_Main.append(str(self.id) + ' - ' + self.messageLineEdit_2.text())
            callback = SendAMainMessage(self.conf, self.id, self.sessionnumber, self.messageLineEdit_2.text())
            if callback == 'ConRE':
                self.dialog_err = QtWidgets.QDialog()
                self.dialog_err.ui = errormessage.Ui_Dialog()
                self.dialog_err.ui.setupUi(self.dialog_err)
                self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
                self.dialog_err.exec_()
                sys.exit()

    def send_role_msg(self):
        # callback = SendAMainMessage(self.id, self.messageLineEdit.text())
        # if callback == 'ConRE':
        self.dialog_err = QtWidgets.QDialog()
        self.dialog_err.ui = errormessage.Ui_Dialog()
        self.dialog_err.ui.setupUi(self.dialog_err)
        self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
        self.dialog_err.exec_()
        sys.exit()

    def quitsearching(self):
        self.flagrun = 0
        self.namechanger()
        self.killthreads()

    def StartSearching(self):
        self.flagrun = 1
        self.killthreads()
        self.namechanger(1)
        # -----

    def killthreads(self, name=''):
        if name == '':
            for i in self.dictofthreads:
                self.dictofthreads[i].stop()
        else:
            for i in self.dictofthreads:
                if i != name:
                    self.dictofthreads[i].stop()

    def AuthByVK(self):
        try:
            file = open('saves.txt')
            n = file.read()
            self.sessionnumber = n.strip().split(';')[1]
            self.id = n.strip().split(';')[0]
            self.dialog.close()
            callback = AddOnline(self.sessionnumber, self.id)
            if callback == 'ConRE':
                self.dialog_err = QtWidgets.QDialog()
                self.dialog_err.ui = errormessage.Ui_Dialog()
                self.dialog_err.ui.setupUi(self.dialog_err)
                self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
                self.dialog_err.exec_()
                sys.exit()
            file.close()
        except IOError:
            self.sessionnumber = GetSessionNumb()
            if self.sessionnumber == 'ConRE':
                self.dialog_err = QtWidgets.QDialog()
                self.dialog_err.ui = errormessage.Ui_Dialog()
                self.dialog_err.ui.setupUi(self.dialog_err)
                self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
                self.dialog_err.exec_()
                sys.exit()
            webbrowser.open(
                'https://oauth.vk.com/authorize?client_id=6717045&display=popup&redirect_uri=http://localhost:7200&scope=photos&response_type=code&v=5.85')
            self.simpleth = AThreadForServer()
            self.simpleth.finished.connect(self.send)
            self.simpleth.start()

    def send(self):
        global certain
        callback = SendSessionNumberAndToken(self.sessionnumber, certain['access_token'])
        if callback == 'ConRE':
            self.dialog_err = QtWidgets.QDialog()
            self.dialog_err.ui = errormessage.Ui_Dialog()
            self.dialog_err.ui.setupUi(self.dialog_err)
            self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
            self.dialog_err.exec_()
            sys.exit()
        self.id = getfullandsecondname(certain['access_token'])
        self.dialog.close()
        with open('saves.txt', mode='w') as file:
            file.write(self.id + ';' + self.sessionnumber)
        callback = AddOnline(self.sessionnumber, self.id)
        if callback == 'ConRE':
            self.dialog_err = QtWidgets.QDialog()
            self.dialog_err.ui = errormessage.Ui_Dialog()
            self.dialog_err.ui.setupUi(self.dialog_err)
            self.dialog_err.setAttribute(Qt.WA_DeleteOnClose)
            self.dialog_err.exec_()
            sys.exit()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
