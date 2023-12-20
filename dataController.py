import dataUtilClass
from dataBaseAccsessor import dataBaseRegister

def registerSensorData(dataQeueManager : dataUtilClass.DataQeueManager):
    while True:
        datalist = dataQeueManager.getDataList(True)
        for data in datalist:
            model:dataUtilClass.DataAnalysisModel = data
            xPoint = model.getX()
            yPoint = model.getY()
            value = model.getValue()

            dataBaseRegister.registerAnalysisModel(value, xPoint, yPoint)
    