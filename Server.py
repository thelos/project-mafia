# -*- coding: utf-8 -*-
import base64
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from my_functions import decoding_serv, encoding
from randomshuffled import generate


class MyThread(Thread):
    def run(self):
        while True:
            temp = input()
            try:
                print(allmatchinghere[temp])
            except:
                continue


listofSessions = dict()
mainmessages = []
sysmessages = []
messages_role = []
tab_information = {
}

data_temp = {
    'name': [],
    'members': [],
    'passwords': [],
    'started': [],
    'admin': [],
}

users_online = dict()
lay = dict()
lay_of_tokens = dict()

allmatchinghere = {
    'listofSessions': listofSessions,
    'mainmessages': mainmessages,
    'messages_role': messages_role,
    'tab_info': tab_information,
    'users_online': users_online,
    'data': data_temp,

}

thread = MyThread()
thread.start()

for line in open('UserId_Key.txt', 'r'):
    line_t = line.strip()
    s = line_t.split(' - ')
    lay[s[0]] = s[1]

for line in open('BaseOfVk.txt', 'r'):
    line_t = line.strip()
    s = line_t.split(';')
    listofSessions[s[0]] = s[1]


class MyServer(BaseHTTPRequestHandler):
    def do_WriteMainMessage(self):
        temp = data_temp['name'][int(decoding_serv(self.headers['conf']))]
        tab_information[temp]['mainmessages'].append(decoding_serv(self.headers['text']))

    def do_GetTabInformation(self):
        head = self.headers
        if head['general'] == '1':
            self.send_response(200)
            self.send_header('noerrors', 1)
            global data_temp
            self.send_header('name', encoding('$'.join(data_temp['name'])))
            self.send_header('members', encoding('$'.join(data_temp['members'])))
            res = []
            for i in data_temp['passwords']:
                if i != '':
                    res.append('Yes')
                else:
                    res.append('No')
            self.send_header('passwords', encoding('$'.join(res)))
            self.send_header('started', encoding('$'.join(data_temp['started'])))
            self.send_header('admin', encoding('$'.join(data_temp['admin'])))
            self.end_headers()
        else:
            if decoding_serv(head['name']) in data_temp['name']:
                self.send_response(200)
                self.send_header('noerrors', 0)
                self.send_header('invalidname', 1)
                self.end_headers()
            else:
                name = decoding_serv(self.headers['name'])
                tab_information[name] = {}
                tab_information[name]['members'] = '1/' + decoding_serv(self.headers['maxusers'])
                if 'sessions' in tab_information[name]:
                    tab_information[name]['sessions'].append(decoding_serv(self.headers['sessions']))
                else:
                    tab_information[name]['sessions'] = [decoding_serv(self.headers['sessions'])]
                tab_information[name]['passwords'] = decoding_serv(self.headers['password'])
                tab_information[name]['started'] = '0'
                tab_information[name]['admin'] = decoding_serv(self.headers['admin'])
                data_temp['name'].append(name)
                data_temp['members'].append(tab_information[name]['members'])
                data_temp['passwords'].append(tab_information[name]['passwords'])
                data_temp['started'].append('0')
                data_temp['admin'].append(tab_information[name]['admin'])
                tab_information[name]['mainmessages'] = [
                    'Привет! Вы зашли в комнату, для начала игры вы должны иметь в комнате как минимум 6 человек',
                    'После получения этого кол-ва админ должен прописать !start для начала игры! Удачи:)']
                self.send_response(200)
                self.send_header('noerrors', 1)
                self.send_header('invalidname', 0)
                self.end_headers()

    def do_ReturnMainMessages(self):
        s = self.headers
        self.send_response(200)
        self.send_header('sd', s)
        self.end_headers()
        self.wfile.write(
            bytes('\n'.join(tab_information[data_temp['name'][int(decoding_serv(s['conf']))]]['mainmessages']),
                  encoding='utf-8'))

    def do_GetSessionNumb(self):
        s = 0
        while True:
            s = generate()
            if s not in listofSessions:
                listofSessions[s] = 0
                break
        self.send_response(200)
        self.send_header('sd', s)
        self.end_headers()
        self.wfile.write(bytes(s, encoding='utf-8'))

    def do_SendSAndToken(self):
        v = self.path.split(';')
        listofSessions[v[0]] = v[1]
        with open('BaseOfVk.txt', 'a') as file:
            file.write(v[0] + ';' + v[1])

    def do_ReturnTokenHaven(self):
        for line in open('BaseOfTokens.txt', 'r'):
            line_t = line.strip()
            s = line_t.split(' - ')
            if s[0] not in lay:
                lay[s[0]] = s[1]
        v = self.path.split(';')

    # Все хорошо
    def do_AddOnline(self):
        sessionnumber = (base64.b64decode(self.headers['session_number'])).decode('utf-8')
        name = (base64.b64decode(self.headers['name'])).decode('utf-8')
        users_online[sessionnumber] = name

    # доработай
    def do_Connect(self):
        head = self.headers
        room = tab_information[data_temp['name'][int(decoding_serv(head['number']))]]
        if int(room['members'].split('/')[0]) < int(room['members'].split('/')[1]) and room['started'] != '1':
            room['sessions'].append(decoding_serv(head['session']))

    def do_ConnectByName(self):
        head = self.headers
        room = tab_information[decoding_serv(head['name'])]
        if int(room['members'].split('/')[0]) < int(room['members'].split('/')[1]) and room['started'] != '1':
            room['sessions'].append(decoding_serv(head['session']))
        room['mainmessages'].append(decoding_serv(head['ide']) + ' Succesfully Connected!')

    def do_GetByName(self):
        head = self.headers
        self.send_response(200)
        for i in range(len(data_temp['name'])):
            if data_temp['name'][i] == decoding_serv(head['name']):
                self.send_header('number', encoding(str(i)))
        self.end_headers()


myServer = HTTPServer(("localhost", 8000), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % ("localhost", 8000))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % ("localhost", 8000))
