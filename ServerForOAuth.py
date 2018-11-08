from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import requests
import json
flag = 0

class ServerFinish(Exception):
    pass


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global flag
        self.count = self.path
        if flag == 1:
            return
        flag = 1
        get_url = "https://oauth.vk.com/access_token"
        get_payload = {"client_id": '6717045', 'client_secret': 'vxsLyG7QpfvUHnUeTmMB', 'redirect_uri': 'http://localhost:7200', 'code': self.count[7:]}
        get_request = requests.get('https://oauth.vk.com/access_token?client_id=6717045&client_secret=vxsLyG7QpfvUHnUeTmMB&redirect_uri=http://localhost:7200&code=' + self.count[7:])
        response = get_request.json()
        #webbrowser.open('https://oauth.vk.com/access_token?client_id=6717045&client_secret=vxsLyG7QpfvUHnUeTmMB&redirect_uri=http://localhost:7200&code=' + self.count[7:])
        raise ServerFinish

