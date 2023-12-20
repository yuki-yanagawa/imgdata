from dataBaseAccsessor import dataBaseManager
import dataUtilClass

import sqlite3

def getAnalysisModelAllData():

    # conn = dataBaseManager.DataBaseConnecor.getConnection()

    conn = sqlite3.connect('test_sqlite.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM AnalysisDataModel'
    )

    retData = []
    dataList = cursor.fetchall()

    for data in dataList:
        dic = {}
        dic['val'] = data[2]
        dic['x'] = data[3]
        dic['y'] = data[4]
        retData.append(dic)


    conn.commit()



    cursor.close()
    conn.close()

    return retData