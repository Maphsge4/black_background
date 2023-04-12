"""
我大概知道了，不能用sleep，而是得用Qt自带的计时器。因为python的sleep相当于程序暂停，你运行的窗口也是个程序，所以sleep的是胡窗口也就白屏了
打包exe: pyinstaller -F -w main.py
"""

import random
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer

from GUI_Main import Ui_MainWindow as GUI2
# from start import Ui_MainWindow as GUI1
from GUI_Practice import Ui_MainWindow as GUI1

true_lines = list()
false_lines = list()


class MyGUI1(QtWidgets.QMainWindow, GUI1):
    switch_window = QtCore.pyqtSignal()

    #       初始化窗口
    def __init__(self):
        super().__init__()
        self.sec = None
        self.setupUi(self)
        self.timer = QTimer()  # 创建定时器
        self.ans_timer = QTimer()
        self.run()
        self.cur_time = 1000

        self.trueButton.hide()
        self.FalseButton.hide()

        self.mutex = 0

        self.it = -1

        self.true_count = 0
        self.tot_count = 0

        self.a = True

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Y and self.mutex == 1:
            print("Y pressed")
            self.clickT()
        elif event.key() == Qt.Key_N and self.mutex == 1:
            print("N pressed")
            self.clickF()

    # 更新计数器的数字
    def setText(self):
        self.sec += 1
        _translate = QtCore.QCoreApplication.translate
        # if self.sec == 1:
        #     self.label.setText(_translate("MainWindow", "[  ]"))
        #     self.timer.stop()
        #     self.timer.start(200)
        # elif self.sec == 2:
        #     self.label.setText(_translate("MainWindow", "☒☒☒"))
        #     self.timer.stop()
        #     self.timer.start(200)
        if self.sec == 1:
            # self.label.setText(_translate("MainWindow", "楼阁"))
            self.label.setText(_translate("MainWindow", true_lines[self.it]))
            self.timer.stop()
            self.timer.start(self.cur_time)
        elif self.sec == 2:
            self.label.setText(_translate("MainWindow", "☒☒☒"))
            self.timer.stop()
            self.timer.start(200)
        elif self.sec == 3:
            # global a
            self.a = random.choice([True, False])
            if self.a:
                self.label.setText(_translate("MainWindow", true_lines[self.it]))
            else:
                self.label.setText(_translate("MainWindow", false_lines[self.it]))
            self.timer.stop()
            self.timer.start(self.cur_time)
        else:
            self.label.setText(_translate("MainWindow", " "))
            self.timer.stop()
            self.start_confirm_button.hide()
            self.trueButton.show()
            self.FalseButton.show()
            self.mutex = 1
            self.ans_timer.start(1000)

    # 开始计数
    def startCount(self):
        self.it = -1

        self.true_count = 0
        self.tot_count = 0

        self.a = True
        self.sec = 0
        # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        self.timer.start(1000)
        # 当单击按钮开始计时后，按钮文字修改为停止计时，并且绑定的槽函数发生改变
        # self.pushButton.setText("停止计时")
        # self.pushButton.clicked.connect(self.stopTime)
        self.it += 1

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
        self.ans_timer.timeout.connect(self.timeOut)
        # 单击按钮计数开始
        self.start_confirm_button.clicked.connect(self.startCount)
        self.exitButton.clicked.connect(self.exit)

        self.trueButton.clicked.connect(self.clickT)
        self.FalseButton.clicked.connect(self.clickF)

    def clickT(self):
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        # self.label.setText(_translate("MainWindow", "回答错误"))
        if self.a:
            self.label.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
        else:
            self.label.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0
        self.tot_count += 1

        if self.true_count == 5:
            self.exit()
        elif self.tot_count >= 10:
            self.label.setText(_translate("MainWindow", "结束"))
            self.trueButton.hide()
            self.FalseButton.hide()
            self.start_confirm_button.show()
        else:
            self.sec = 0
            # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
            self.timer.start(self.cur_time)
            self.it += 1
            self.trueButton.hide()
            self.FalseButton.hide()

    def clickF(self):
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        # self.label.setText(_translate("MainWindow", "回答正确"))
        if not self.a:
            self.label.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
        else:
            self.label.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0
        self.tot_count += 1

        if self.true_count == 5:
            self.exit()
        elif self.tot_count >= 10:
            self.label.setText(_translate("MainWindow", "结束"))
            self.trueButton.hide()
            self.FalseButton.hide()
            self.start_confirm_button.show()
        else:
            self.sec = 0
            # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
            self.timer.start(self.cur_time)
            self.it += 1
            self.trueButton.hide()
            self.FalseButton.hide()

    def timeOut(self):
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "作答超时"))
        self.true_count = 0
        self.tot_count += 1

        if self.true_count == 5:
            self.exit()
        elif self.tot_count >= 10:
            self.label.setText(_translate("MainWindow", "结束"))
            self.trueButton.hide()
            self.FalseButton.hide()
            self.start_confirm_button.show()
        else:
            self.sec = 0
            # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
            self.timer.start(self.cur_time)
            # global it
            self.it += 1
            self.trueButton.hide()
            self.FalseButton.hide()

    def exit(self):
        self.switch_window.emit()


class MyGUI2(QtWidgets.QMainWindow, GUI2):
    switch_window = QtCore.pyqtSignal()

    #       初始化窗口
    def __init__(self):
        super().__init__()
        self.sec = None
        self.setupUi(self)
        self.timer = QTimer()  # 创建定时器
        self.ans_timer = QTimer()
        self.run()
        self.cur_time = 1000
        self.cha_time = 200

        self.trueButton.hide()
        self.FalseButton.hide()

        self.mutex = 0

        self.tot_prac = 0
        self.it = -1

        self.true_count = 0
        self.false_count = 0
        self.change = list()

        self.pos_list = list()
        self.neg_list = list()

        self.a = True

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Y and self.mutex == 1:
            print("Y pressed")
            self.clickT()
        elif event.key() == Qt.Key_N and self.mutex == 1:
            print("N pressed")
            self.clickF()

    # 更新计数器的数字
    def setText(self):

        self.sec += 1
        _translate = QtCore.QCoreApplication.translate
        # if self.sec == 1:
        #     self.label.setText(_translate("MainWindow", "[  ]"))
        #     self.timer.stop()
        #     self.timer.start(self.cha_time)
        if self.sec == 1:
            self.label.setText(_translate("MainWindow", "☒☒☒"))
            self.timer.stop()
            self.timer.start(self.cha_time)
        elif self.sec == 2:
            self.label.setText(_translate("MainWindow", true_lines[self.it]))
            self.timer.stop()
            self.timer.start(self.cur_time)
        elif self.sec == 3:
            self.label.setText(_translate("MainWindow", "☒☒☒"))
            self.timer.stop()
            self.timer.start(self.cha_time)
        elif self.sec == 4:
            # global a
            self.a = random.choice([True, False])
            if self.a:
                self.label.setText(_translate("MainWindow", true_lines[self.it]))
            else:
                self.label.setText(_translate("MainWindow", false_lines[self.it]))
            self.timer.stop()
            self.timer.start(self.cur_time)
        else:
            self.label.setText(_translate("MainWindow", "   "))
            self.timer.stop()
            self.start_confirm_button.hide()
            self.trueButton.show()
            self.FalseButton.show()
            self.mutex = 1
            self.ans_timer.start(1000)

    # 开始计数
    def startCount(self):

        self.sec = 0
        self.it += 1
        self.trueButton.hide()
        self.FalseButton.hide()
        self.mutex = 0

        if self.it >= 100:
            self.summary()

        # print("pos_list:", self.pos_list)
        # print("neg_list:", self.neg_list)

        if len(self.pos_list) >= 3 and len(self.neg_list) >= 3:
            # print("pop")
            self.cha_time = int(self.cha_time * 0.8)
            self.pos_list.pop()
            self.neg_list.pop()
            self.pos_list.pop()
            self.neg_list.pop()
            self.pos_list.pop()
            self.neg_list.pop()

        # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        self.timer.start(self.cur_time)

    def summary(self):
        # print(self.change)
        positive = 0
        negative = 0
        for i in range(80, 100):
            if self.change[i] == 1:
                positive += 1
            if self.change[i] == -1:
                negative += 1
        if positive == 0 and negative == 0:
            # print("valid")
            with open("output.txt", "a") as file:
                file.write("valid\n")
        else:
            # print("invalid")
            with open("output.txt", "a") as file:
                file.write("invalid\n")
        self.close()

    # 绑定信号与槽
    def run(self):
        # 每秒计数器计数结束后更新计数板数字
        self.timer.timeout.connect(self.setText)
        self.ans_timer.timeout.connect(self.timeOut)
        # 单击按钮计数开始
        self.start_confirm_button.clicked.connect(self.startCount)

        self.trueButton.clicked.connect(self.clickT)
        self.FalseButton.clicked.connect(self.clickF)

    def clickT(self):
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        if self.a:
            self.label.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
            if self.true_count == 3:
                if self.cur_time == 17:
                    self.change.append(0)
                elif self.cur_time > 17:
                    self.cur_time -= self.cha_time
                    if self.cur_time < 17:
                        self.cur_time = 17
                    self.change.append(-1)
                    self.neg_list.append(-1)
                self.true_count = 0
            else:
                self.change.append(0)
        else:
            self.label.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0

            if self.cur_time == 1200:
                self.change.append(0)
            elif self.cur_time < 1200:
                self.cur_time += self.cha_time
                if self.cur_time > 1200:
                    self.cur_time = 1200
                self.change.append(1)
                self.pos_list.append(1)

        # self.sec = 0
        # # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        # self.timer.start(self.cur_time)
        # # global it
        # self.it += 1
        # self.trueButton.hide()
        # self.FalseButton.hide()
        self.startCount()

    def clickF(self):
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        if not self.a:
            self.label.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
            if self.true_count == 3:
                if self.cur_time == 17:
                    self.change.append(0)
                elif self.cur_time > 17:
                    self.cur_time -= self.cha_time
                    if self.cur_time < 17:
                        self.cur_time = 17
                    self.change.append(-1)
                    self.neg_list.append(-1)
                self.true_count = 0
            else:
                self.change.append(0)
        else:
            self.label.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0

            if self.cur_time == 1200:
                self.change.append(0)
            elif self.cur_time < 1200:
                self.cur_time += self.cha_time
                if self.cur_time > 1200:
                    self.cur_time = 1200
                self.change.append(1)
                self.pos_list.append(1)
        # self.sec = 0
        # # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        # self.timer.start(self.cur_time)
        # # global it
        # self.it += 1
        # self.trueButton.hide()
        # self.FalseButton.hide()
        self.startCount()

    def timeOut(self):
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "作答超时"))
        self.true_count = 0

        if self.cur_time == 1200:
            self.change.append(0)
        elif self.cur_time < 1200:
            self.cur_time += self.cha_time
            if self.cur_time > 1200:
                self.cur_time = 1200
            self.change.append(1)
            self.pos_list.append(1)

        # self.sec = 0
        # # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        # self.timer.start(self.cur_time)
        # # global it
        # self.it += 1
        # self.trueButton.hide()
        # self.FalseButton.hide()
        self.startCount()


class Controller:
    def __init__(self):
        self.window = None
        self.practice = None

    def show_practice(self):
        self.practice = MyGUI1()
        self.practice.switch_window.connect(self.show_main)
        self.practice.showMaximized()

    def show_main(self):
        self.window = MyGUI2()
        # self.window.switch_window.connect(self.show_window_two)
        self.practice.close()
        self.window.showMaximized()


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)

    with open("true.txt", "r", encoding='utf-8') as tf:
        true_lines = tf.read().split(',')
    with open("false.txt", "r", encoding='utf-8') as tf:
        false_lines = tf.read().split(',')

    controller = Controller()
    controller.show_practice()

    sys.exit(app.exec_())
