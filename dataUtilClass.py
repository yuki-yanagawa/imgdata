import threading

class DataQeueManager():
    _instance = None
    _lock = threading.Lock()
    _condition = threading.Condition()
    _datalist = []

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance


    def addDataList(self, data):
        print("ADD DATA")
        self._condition.acquire()
        with self._lock:
            self._datalist.append(data)
            self._condition.notifyAll()
            self._condition.release()
    
    def getDataList(self, removeflg):
        print("GET DATA START")
        self._condition.acquire()
        if len(self._datalist) == 0:
            self._condition.wait()
            self._condition.release()
        print("GET DATA NEXT")
        with self._lock:
            if removeflg:
                tmpData = self._datalist
                self._datalist = []
                return tmpData
            return self._datalist


class DataAnalysisModel():
    def __init__(self, datadict):
        self._value = datadict['value']
        self._x = datadict['x']
        self._y = datadict['y']
    
    def getValue(self):
        return self._value
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
