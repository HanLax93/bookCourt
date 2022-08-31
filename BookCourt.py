import sys

import yaml
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from ui.mainui import Ui_MainWindow

from application.app import getConfig, App
from application.modules import Features


class RunThread1(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self, config):
        super(RunThread1, self).__init__()
        self.config = config

    def run(self):
        a = App(self.config)
        t1, t2 = a.main()
        ret = [t1, t2]
        self.signal.emit(ret)


class RunThread2(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self, config):
        super(RunThread2, self).__init__()
        self.config = config

    def run(self):
        a = App(self.config)
        t1, t2 = a.main()
        ret = [t1, t2]
        self.signal.emit(ret)


class MainWindow(QMainWindow):
    def __init__(self, mem):
        super(MainWindow, self).__init__()
        self.thread = None
        self.ui = Ui_MainWindow(mem)
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.whatBtnDo)

        self.nickname = "login"
        self.config = getConfig()
        option1 = list(self.config['stadiumIdList'].keys())
        option2 = list(self.config['periodIdList'].keys())
        # 下拉框
        # 添加options
        # 两个下拉框分别是option1, option2
        for i in option1:
            self.ui.option1.addItem(i)
        for i in option2:
            self.ui.option2.addItem(i)

        self.ui.option1.setCurrentText(mem['topCourt'])
        self.ui.option2.setCurrentText(mem['topCourtTime'])
        self.ui.label2.setText(self.nickname)

    # 点击按钮触发的函数
    def whatBtnDo(self):
        # TODO: write code here
        t_hour = self.ui.input2.text()
        t_min = self.ui.input3.text()
        t_sec = self.ui.input4.text()
        delayms = self.ui.input5.text()
        timing = [t_hour, t_min, t_sec, delayms]
        token = self.ui.input.text()
        court = self.ui.option1.currentText()
        courtTime = self.ui.option2.currentText()
        self.config.update({'topToken': token, 'topCourt': court, 'topCourtTime': courtTime, 'timing': timing})
        timing = self.config['timing']
        t = [int(timing[0]), int(timing[1]), int(timing[2]), 1-int(timing[3])/1000]
        self.config.update({'time': t})
        # t1, t2 = self.operation()

        fname = './config/memo.yaml'
        mem = open(fname, 'r')
        mem_data = yaml.load(mem, Loader=yaml.FullLoader)
        mem_data.update({'topToken': token, 'topCourt': court, 'topCourtTime': courtTime, 'timing': timing})
        with open(fname, 'w') as f:
            f.write(yaml.dump(mem_data, default_flow_style=False))
            f.close()

        _, _, self.nickname = Features(token, self.config).getPriLogs()
        self.ui.label2.setText(self.nickname)
        self.resize(540, 240)
        self.ui.label1.setText("loading...")

        self.thread = RunThread1(self.config)
        self.thread.signal.connect(self.callbacklog)
        self.thread.start()

    def callbacklog(self, msg):
        if msg[1] == "False":
            self.ui.label1.setText(msg[0])
        elif not msg[1]:
            self.ui.label1.setText('Invalid token.')
        else:
            self.resize(540, 335)
            self.ui.label1.setText(msg[0] + '\n' + msg[1])


if __name__ == "__main__":
    gapp = QApplication(sys.argv)

    memo = open('./config/memo.yaml', 'r')
    memo_data = yaml.load(memo, Loader=yaml.FullLoader)
    memo.close()

    window = MainWindow(memo_data)
    window.setWindowTitle("预约小工具")
    window.setWindowIcon(QtGui.QIcon("src/icon.png"))
    window.show()

    sys.exit(gapp.exec())
