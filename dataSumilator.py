import dataUtilClass
import dataController
import threading
import time
import signal

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    dataQeueManager = dataUtilClass.DataQeueManager()

    dcThread = threading.Thread(target=dataController.registerSensorData, args=(dataQeueManager,))
    dcThread.start()

    counter = 0

    # データ取得をイメージ
    while counter < 500:
        time.sleep(5)
        counter += 1
        data = {}
        data['x'] = 10
        data['y'] = 20
        data['value'] = 50
        model1 = dataUtilClass.DataAnalysisModel(data)
        dataQeueManager.addDataList(model1)

if __name__ == "__main__":
    main()
