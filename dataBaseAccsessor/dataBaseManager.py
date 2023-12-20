import sqlite3

class DataBaseConnecor():
    _connection = sqlite3.connect('test_sqlite.db')
    
    @classmethod
    def getConnection(cls) -> sqlite3.Connection:
        if cls._connection is None:
            cls._connection = sqlite3.connect('test_sqlite.db')
        return cls._connection