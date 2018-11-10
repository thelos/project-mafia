import base64
import http.client


def decoding_serv(obj):
    return base64.b64decode(obj).decode('utf-8')


def decoding(obj):
    return base64.b64decode(obj[2:-1]).decode('utf-8')


def encoding(obj):
    return base64.b64encode(bytes(obj, encoding='utf-8'))


def GetTabInformation(name='', password='', maxusers='12', admin='', sessionnumber='', started=False):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('GetTabInformation', 'GetTabInformation')
        if name == '':
            h3.putheader('general', 1)
            h3.putheader('took', 0)
        else:
            h3.putheader('took', 1)
            h3.putheader('general', 0)
            h3.putheader('name', encoding(name))
            h3.putheader('password', encoding(password))
            h3.putheader('admin', encoding(admin + ';' + sessionnumber))
            h3.putheader('maxusers', encoding(maxusers))
            h3.putheader('sessions', encoding(sessionnumber))
        h3.endheaders()
        result = h3.getresponse()
        dist = result.headers
        return dist

    except ConnectionRefusedError:
        return 'ConRE'


def GetAMainMessages(conf):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('ReturnMainMessages', 'ReturnMessages')
        h3.putheader('conf', encoding(str(conf)))
        h3.endheaders()
        result = h3.getresponse()
        return result.read().decode('utf-8')
    except ConnectionRefusedError:
        return 'ConRE'


def SendAMainMessage(conf, ide, session, text):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('WriteMainMessage', 'sda')
        h3.putheader('conf', encoding(str(conf)))
        h3.putheader('text', encoding(ide + ' - ' + text))
        h3.putheader('session', encoding(session))
        h3.endheaders()
        h3.close()
    except ConnectionRefusedError:
        return 'ConRE'


def AddOnline(session, name):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('AddOnline', 'sda')
        h3.putheader('session_number', encoding(session))
        h3.putheader('name', encoding(name))
        h3.endheaders()
        h3.close()
    except ConnectionRefusedError:
        return 'ConRE'


def SendSessionNumberAndToken(sessionnumb, token):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('SendSAndToken', str(sessionnumb) + ';' + token)
        h3.putheader(token, '2')
        h3.endheaders()
        h3.close()
    except ConnectionRefusedError:
        return 'ConRE'


def GetASysMessages():
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('ReturnSysMessages', 'ReturnMessages')
        h3.putheader('s', '2')
        h3.endheaders()
        result = h3.getresponse()
        return result.read().decode('utf-8')
    except ConnectionRefusedError:
        return 'ConRE'


def GetSessionNumb():
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('GetSessionNumb', 'ReturnMessages')
        h3.putheader('s', '2')
        h3.endheaders()
        result = h3.getresponse()
        return result.read().decode('utf-8')
    except ConnectionRefusedError:
        return 'ConRE'


def connect(number, sessionnumber, password=''):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('Connect', 'Connect')
        h3.putheader('number', encoding(str(number)))
        h3.putheader('session', encoding(sessionnumber))
        h3.putheader('password', encoding(password))
        h3.endheaders()
        return h3.getresponse().headers
    except ConnectionRefusedError:
        return 'ConRE'


def connect_by_name(conf, sessionnumber, ide, password):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('ConnectByName', 'Connect')
        h3.putheader('name', encoding(conf))
        h3.putheader('session', encoding(sessionnumber))
        h3.putheader('ide', encoding(ide))
        h3.putheader('password', encoding(password))
        h3.endheaders()
    except ConnectionRefusedError:
        return 'ConRE'


def getbyconf(conf):
    try:
        h3 = http.client.HTTPConnection('localhost', 8000)
        h3.putrequest('GetByName', 'Connect')
        h3.putheader('name', encoding(conf))
        h3.endheaders()
        return int(decoding(h3.getresponse().headers['number']))
    except ConnectionRefusedError:
        return 'ConRE'
