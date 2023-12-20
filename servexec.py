from webserver import httpServer

import subprocess
import signal

if __name__ == "__main__":
    serv = httpServer.HttpServer(8080)
    serv.serviceStart()

