import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.mainui import Ui_MainWindow
from ui.popui import Ui_PopWindow

from application.app import getConfig, app
from application.progress import long_operation


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
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
        t1, t2 = self.operation()
        # 弹出第二个窗口
        self.popWin.show()

        self.popWin.ui.text1.setText(t1)
        self.popWin.ui.text2.setText(t2)

    @long_operation("Counting down")
    def operation(self):
        a = app(self.config)
        return a.main()


class PopWindow(QMainWindow):
    def __init__(self):
        super(PopWindow, self).__init__()
        self.ui = Ui_PopWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    gapp = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(gapp.exec())
