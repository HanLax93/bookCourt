import sys

import yaml
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from ui.mainui import Ui_MainWindow
from ui.popui import Ui_PopWindow

from application.app import getConfig, app
from application.progress import long_operation


class RunThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self, config):
        super(RunThread, self).__init__()
        self.config = config

    def run(self):
        a = app(self.config)
        t1, t2 = a.main()
        ret = [t1, t2]
        self.signal.emit(ret)


class MainWindow(QMainWindow):
    def __init__(self, mem):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow(mem)
        self.ui.setupUi(self)

        self.popWin = PopWindow()
        self.ui.btn.clicked.connect(self.whatBtnDo)

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
        # t1, t2 = self.operation()
        # 弹出第二个窗口

        fname = './config/memo.yaml'
        mem = open(fname, 'r')
        mem_data = yaml.load(mem, Loader=yaml.FullLoader)
        mem_data.update({'topToken': token, 'topCourt': court, 'topCourtTime': courtTime, 'timing': timing})
        with open(fname, 'w') as f:
            f.write(yaml.dump(mem_data, default_flow_style=False))
            f.close()

        self.ui.label1.setText("loading...")

        self.thread = RunThread(self.config)
        self.thread.signal.connect(self.callbacklog)
        self.thread.start()
        # self.popWin.show()
        # self.popWin.ui.text1.setText(t1)
        # self.popWin.ui.text2.setText(t2)

    def callbacklog(self, msg):
        self.ui.label1.setText(msg[1] + '\n' + msg[0])
    # @long_operation("Counting down")
    # def operation(self):
    #     a = app(self.config)
    #     return a.main()


class PopWindow(QMainWindow):
    def __init__(self):
        super(PopWindow, self).__init__()
        self.ui = Ui_PopWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    gapp = QApplication(sys.argv)

    memo = open('./config/memo.yaml', 'r')
    memo_data = yaml.load(memo, Loader=yaml.FullLoader)
    memo.close()

    window = MainWindow(memo_data)
    window.show()

    sys.exit(gapp.exec())
