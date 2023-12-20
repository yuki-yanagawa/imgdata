import sqlite3

conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()

curs.execute(
    'CREATE TABLE AnalysisDataModel(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP, value INTEGER, xPoint INEGER, yPoint INTEGER)'
)
conn.commit()

conn.close()