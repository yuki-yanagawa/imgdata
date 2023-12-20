from dataBaseAccsessor import dataBaseManager
import sqlite3

def registerAnalysisModel(value, xPoint, yPoint):

    # conn = dataBaseManager.DataBaseConnecor.getConnection()

    conn = sqlite3.connect('test_sqlite.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO AnalysisDataModel(value, xPoint, yPoint) values({},{},{})'.format(value, xPoint, yPoint)
    )
    conn.commit()
    cursor.close()
    conn.close()



