import socket
import threading
import re
import json
import signal

from dataBaseAccsessor import dataBaseAccessor

BUFSIZE = 4096

class HttpServer():
   
    def __init__(self, port:int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind(("", port))
        self.lock = threading.Lock()
        self.tmpDataStock = []
    
    def serviceStart(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.sock.listen()
        
        while True:
            client, addr = self.sock.accept()
            th = threading.Thread(target=httpHandle, args=(client,self.tmpDataStock, self.lock,))
            th.start()
        
        


def httpHandle(client:socket.socket, dataStock, lock:threading.Lock):
    data = client.recv(BUFSIZE)

    data = data.decode('UTF-8')

    dataline = data.split("\r\n")
    
    # GET / HTTP/1.1
    # Method request Protocol
    header = dataline[0]
    method = header.split(" ")[0]
    request = header.split(" ")[1]

    reqFile = "webserver/html"
    if method == "GET":
        if request == "/":
            reqFile += "/index.html"
        elif request == "/sensorMonitor.html":
            reqFile += request
        elif re.match("/javascript/.*\.js$", request):
            reqFile = "webserver" + request
        elif re.match("css/.*\.css", request):
            reqFile = "webserver" + request
        else:
            reqFile += "/index.html"
        f = open(reqFile, "rt")
        resBody = f.read()
        f.close()

        resHeader = "HTTP/1.0 200 OK\r\n"
        resHeader += "Server: ServerTest\r\n"
        resHeader += "Date: 2020-10-10\r\n"
        resHeader += "Connection: close\r\n"
        resHeader += "\r\n"

    elif method == "POST":
        if request == "/getSensorData":
            body = dataBaseAccessor.getAnalysisModelAllData()
            resBody = json.dumps(body, ensure_ascii=False, indent=2)
        elif request == '/getSensorDataAuto':
            lock.acquire()
            print(dataStock)
            lock.release()

        

        resHeader = "HTTP/1.0 200 OK\r\n"
        resHeader += "Server: ServerTest\r\n"
        resHeader += "Date: 2020-10-10\r\n"
        resHeader += "Content-Type: application/json\r\n"
        resHeader += "Connection: close\r\n"
        resHeader += "\r\n"

    resHeader += resBody
    resHeader += "\r\n\r\n"
    
    client.sendall(resHeader.encode('UTF-8'))

    client.close()

    
