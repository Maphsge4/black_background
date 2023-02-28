"""
我大概知道了，不能用sleep，而是得用Qt自带的计时器。因为python的sleep相当于程序暂停，你运行的窗口也是个程序，所以sleep的是胡窗口也就白屏了
"""

import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer

# from start import Ui_MainWindow as GUI1
from untitled import Ui_MainWindow as GUI1


class MyGUI1(QtWidgets.QMainWindow, GUI1):
    #       初始化窗口
    def __init__(self):
        super().__init__()
        self.sec = None
        self.setupUi(self)
        self.timer = QTimer()  # 创建定时器
        self.run()

        self.trueButton.hide()
        self.FalseButton.hide()

    # 更新计数器的数字
    def setText(self):
        self.sec += 1
        _translate = QtCore.QCoreApplication.translate
        if self.sec == 1:
            self.label.setText(_translate("MainWindow", "[  ]"))
            self.timer.stop()
            self.timer.start(200)
        elif self.sec == 2:
            self.label.setText(_translate("MainWindow", "(^_^)"))
            self.timer.stop()
            self.timer.start(200)
        elif self.sec == 3:
            self.label.setText(_translate("MainWindow", "楼阁"))
            self.timer.stop()
            self.timer.start(1000)
        elif self.sec == 4:
            self.label.setText(_translate("MainWindow", "(^_^)"))
            self.timer.stop()
            self.timer.start(200)
        else:
            self.label.setText(_translate("MainWindow", "楼闾"))
            self.timer.stop()
            self.start_confirm_button.hide()
            self.trueButton.show()
            self.FalseButton.show()

    # 开始计数
    def startCount(self):
        self.sec = 0
        # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        self.timer.start(1000)
        # 当单击按钮开始计时后，按钮文字修改为停止计时，并且绑定的槽函数发生改变
        # self.pushButton.setText("停止计时")
        # self.pushButton.clicked.connect(self.stopTime)

    # # 停止计时，计时置为0
    # def stopTime(self):
    #     global sec
    #     sec = 0
    #     self.timer.stop()
    #     self.lcdNumber.display(sec)
    #     # 当单击按钮停止计时时，按钮文字修改为开始计时，按钮绑定槽函数改变
    #     self.pushButton.setText("开始计时")
    #     self.pushButton.clicked.connect(self.startCount)

    # 绑定信号与槽
    def run(self):
        # 每秒计数器计数结束后更新计数板数字
        self.timer.timeout.connect(self.setText)
        # 单击按钮计数开始
        self.start_confirm_button.clicked.connect(self.startCount)

        self.trueButton.clicked.connect(self.clickT)
        self.FalseButton.clicked.connect(self.clickF)

    def clickT(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "回答错误"))

    def clickF(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "回答正确"))


# class MyGUI2(QtWidgets.QMainWindow, GUI2):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.timer = QTimer()  # 创建定时器
#         self.timer.stop()  # 停止
#         self.timer.setInterval(200)  # 定时周期200ms
#         self.timer.timeout.connect(self.do_timer_timeout)
#
#     def do_timer_timeout(self):
#         self.cnt += 1
#         _translate = QtCore.QCoreApplication.translate
#         if self.cnt == 1:
#             self.label.setText(_translate("Form", "haha"))
#         elif self.cnt == 2:
#             self.label.setText(_translate("Form", "（＾ｖ＾）"))
#         elif self.cnt == 3:
#             self.label.setText(_translate("Form", "楼阁"))


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)

    MyGUI1show = MyGUI1()
    MyGUI1show.show()

    sys.exit(app.exec_())
