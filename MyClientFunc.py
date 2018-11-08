import http.client


def SendATokenToCheck(connection, token):
    h3 = connection
    f = h3.putrequest('SendAndCheck', token)
    h3.putheader(token)
    h3.endheaders()
    result = h3.getresponse()
    return result.read().decode('utf-8')


def SendATokenToSave(connection, id, token):
    h3 = connection
    f = h3.putrequest('SendAndSave', str(id) + ';' + token)
    h3.putheader(token)
    h3.endheaders()

def SendAMessage(connection, id, text):
    h3 = connection
    h3.putrequest('WriteMessage', id + text)
    h3.putheader(text, '2')
    h3.endheaders()

def GetAMessages(connection):
    h3 = connection
    f = h3.putrequest('ReturnMessages', 'ReturnMessages')
    h3.putheader('s', '2')
    h3.endheaders()
    result = h3.getresponse()
    return result.read().decode('utf-8')

if __name__ == '__main__':
    SendAMessage('228')