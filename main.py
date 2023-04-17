"""
我大概知道了，不能用sleep，而是得用Qt自带的计时器。因为python的sleep相当于程序暂停，你运行的窗口也是个程序，所以sleep的是胡窗口也就白屏了
打包exe: pyinstaller -F -w main.py
"""
import random
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from GUI_Main_3 import Ui_MainWindow as GUI2
# from start import Ui_MainWindow as GUI1
from GUI_Practice_5 import Ui_MainWindow as GUI1

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
        self.status_timer = QTimer()
        self.run()
        self.cur_time = 1000

        self.trueButton.hide()
        self.FalseButton.hide()
        self.quiz.hide()
        self.commitButton.hide()

        self.mutex = 0

        self.it = -1

        self.true_count = 0
        self.tot_count = 0

        self.a = True
        # self.mode = 0

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
            # self.start_confirm_button.hide()
            self.trueButton.show()
            self.FalseButton.show()
            self.mutex = 1
            self.ans_timer.start(5000)

    # 开始计数
    def startCount(self):
        self.start_confirm_button.hide()
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
        self.status_timer.timeout.connect(self.statusTimeOut)
        # 单击按钮计数开始
        self.start_confirm_button.clicked.connect(self.startCount)
        self.exitButton.clicked.connect(self.exit)

        self.trueButton.clicked.connect(self.clickT)
        self.FalseButton.clicked.connect(self.clickF)
        self.commitButton.clicked.connect(self.surveySummary)

    def clickT(self):
        self.status_timer.start(500)
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        # self.label.setText(_translate("MainWindow", "回答错误"))
        if self.a:

            self.statusLabel.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
        else:
            self.statusLabel.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0
        self.tot_count += 1

        if self.true_count == 5:
            # self.exit()
            self.survey()
        elif self.tot_count >= 10:
            self.statusLabel.setText(_translate("MainWindow", "请重新开始"))
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
        self.status_timer.start(500)
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        # self.label.setText(_translate("MainWindow", "回答正确"))
        if not self.a:
            self.statusLabel.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
        else:
            self.statusLabel.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0
        self.tot_count += 1

        if self.true_count == 5:
            self.survey()
        elif self.tot_count >= 10:
            self.statusLabel.setText(_translate("MainWindow", "请重新开始"))
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

    def statusTimeOut(self):
        _translate = QtCore.QCoreApplication.translate
        self.status_timer.stop()
        self.statusLabel.setText(_translate("MainWindow", "   "))

    def timeOut(self):
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        self.status_timer.start(500)
        self.statusLabel.setText(_translate("MainWindow", "作答超时"))
        self.true_count = 0
        self.tot_count += 1

        if self.true_count == 5:
            self.survey()
        elif self.tot_count >= 10:
            self.statusLabel.setText(_translate("MainWindow", "请重新开始"))
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

    def surveySummary(self):
        quiz1 = int(self.comboBox.currentText())
        quiz2 = int(self.comboBox_2.currentText())
        quiz3 = int(self.comboBox_3.currentText())
        quiz4 = int(self.comboBox_4.currentText())
        print(quiz1, quiz2, quiz3, quiz4)
        # pass
        self.exit()

    def exit(self):
        self.switch_window.emit()

    def survey(self):
        print("进入survey")  # debug
        self.quiz.show()
        self.commitButton.show()


class MyGUI2(QtWidgets.QMainWindow, GUI2):
    switch_window = QtCore.pyqtSignal()

    #       初始化窗口
    def __init__(self):
        super().__init__()
        self.sec = None
        self.setupUi(self)
        # self.setStyleSheet("background-color:rgb(26,26,26)")
        # self.label.setStyleSheet("color:rgb(140,140,140);\n"
        #                          "border:2px solid rgb(255,255,255);")
        # font = QtGui.QFont()
        # font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
        # font.setPointSize(14)
        # self.label.setFont(font)

        self.timer = QTimer()  # 创建定时器
        self.ans_timer = QTimer()
        self.status_timer = QTimer()

        self.cur_time = 1000
        self.cha_time = 200

        self.trueButton.hide()
        self.FalseButton.hide()
        self.quiz.hide()
        self.commitButton.hide()
        # self.start_confirm_button.hide()

        self.mutex = 0

        self.tot_prac = 0
        self.it = -1
        self.idx = None

        self.true_count = 0
        self.false_count = 0
        self.change = list()

        self.pos_list = list()
        self.neg_list = list()
        self.cur_time_list = list()

        self.a = True
        self.iteration = 1
        self.mode = 0
        self.mode_list = [x for x in range(1, 25)]

        self.init_run()

        with open("output.csv", "w+") as file:
            file.write("average_time,correct_rate,mode,q1,q2,q3,q4\n")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Y and self.mutex == 1:
            print("Y pressed")
            self.clickT()
        elif event.key() == Qt.Key_N and self.mutex == 1:
            print("N pressed")
            self.clickF()

    # 更新计数器的数字
    def setText(self):
        # print("进入setText")  # debug
        self.sec += 1
        _translate = QtCore.QCoreApplication.translate
        # if self.sec == 1:
        #     self.label.setText(_translate("MainWindow", "[  ]"))
        #     self.timer.stop()
        #     self.timer.start(self.cha_time)
        if self.sec == 1:
            # print(self.sec)  # debug
            self.label.setText(_translate("MainWindow", "☒☒☒"))
            self.timer.stop()
            self.timer.start(self.cha_time)
        elif self.sec == 2:
            # print(self.sec)  # debug
            self.label.setText(_translate("MainWindow", true_lines[self.idx]))
            self.timer.stop()
            self.timer.start(self.cur_time)
        elif self.sec == 3:
            # print(self.sec)  # debug
            self.label.setText(_translate("MainWindow", "☒☒☒"))
            self.timer.stop()
            self.timer.start(self.cha_time)
        elif self.sec == 4:
            # print(self.sec)  # debug
            # global a
            self.a = random.choice([True, False])
            if self.a:
                self.label.setText(_translate("MainWindow", true_lines[self.idx]))
            else:
                self.label.setText(_translate("MainWindow", false_lines[self.idx]))
            self.timer.stop()
            self.timer.start(self.cur_time)
        else:
            # print(self.sec)  # debug
            self.label.setText(_translate("MainWindow", "   "))
            self.timer.stop()
            self.start_confirm_button.hide()
            self.trueButton.show()
            self.FalseButton.show()
            self.mutex = 1
            self.ans_timer.start(5000)

    # 开始计数
    def startCount(self):
        self.start_confirm_button.hide()
        # print("进入startcount")  # debug
        self.sec = 0
        # print(self.sec)  # debug
        self.it += 1
        self.idx = random.randint(0, 543)
        # print("startcount里面的it", self.it)  # debug
        self.trueButton.hide()
        self.FalseButton.hide()
        self.mutex = 0

        if self.it >= 25:
            self.summary()
            return

        # print("pos_list:", self.pos_list)
        # print("neg_list:", self.neg_list)

        if len(self.pos_list) >= 3 and len(self.neg_list) >= 3:
            # print("pop")  # debug
            self.cha_time = int(self.cha_time * 0.8)
            self.pos_list.pop()
            self.neg_list.pop()
            self.pos_list.pop()
            self.neg_list.pop()
            self.pos_list.pop()
            self.neg_list.pop()

        # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行，如果需要停止，可以调用timer.stop()进行停止
        # print("到这儿了")  # debug
        self.timer.start(self.cur_time)

    def summary(self):
        # print("进入survey")  # debug
        # print(self.change)
        positive = 0
        negative = 0
        correct = 0
        print(self.change)  # debug
        print(self.cur_time_list)  # debug
        tot = 0
        for i in range(15, 25):
            tot += self.cur_time_list[i]
            if self.change[i] == 1:
                positive += 1
            if self.change[i] == -1:
                negative += 1
            if self.change[i] < 0:
                correct += 1
        if positive == 0 and negative == 0:
            print("invalid")
            with open("output.csv", "a") as file:
                file.write('0,0,')
        else:
            print("valid")
            with open("output.csv", "a") as file:
                file.write(str(1.0 * tot / 10) + "," + str(1.0 * correct / 10) + ",")
        # self.close()
        self.survey()

    def statusTimeOut(self):
        _translate = QtCore.QCoreApplication.translate
        self.status_timer.stop()
        self.statusLabel.setText(_translate("MainWindow", "   "))

    def selectMode(self):
        if self.mode == 1:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 2:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 3:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 4:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 5:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 6:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 7:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 8:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 9:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 10:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 11:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 12:
            self.setStyleSheet("background-color:rgb(26,26,26)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 13:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 14:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 15:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 16:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(242,242,242);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 17:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 18:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 19:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 20:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(191,191,191);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(12)
            self.label.setFont(font)
        if self.mode == 21:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 22:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
            font.setPointSize(12)
            self.label.setFont(font)
        elif self.mode == 23:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(14)
            self.label.setFont(font)
        elif self.mode == 24:
            self.setStyleSheet("background-color:rgb(89,89,89)")
            self.label.setStyleSheet("color:rgb(140,140,140);\n"
                                     "border:2px solid rgb(255,255,255);")
            font = QtGui.QFont()
            font.setLetterSpacing(QFont.AbsoluteSpacing, 2)
            font.setPointSize(12)
            self.label.setFont(font)

    def run(self):
        _translate = QtCore.QCoreApplication.translate
        self.iteration += 1
        self.mode = self.mode_list[self.iteration]
        print(self.mode)  # debug
        self.selectMode()
        # print("self.mode+", self.mode)  # debug

        # print("进入run")  # debug
        self.cur_time = 1000
        self.cha_time = 200

        self.trueButton.hide()
        self.FalseButton.hide()
        self.quiz.hide()
        self.commitButton.hide()

        self.mutex = 0
        self.sec = None

        self.tot_prac = 0
        self.it = -1

        self.true_count = 0
        self.false_count = 0
        self.change = list()

        self.pos_list = list()
        self.neg_list = list()
        self.cur_time_list = list()

        self.a = True
        self.start_confirm_button.show()

        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'楷体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; color:#ffffff;\">您已经成功完成第" + str(
                                                self.iteration - 1) + "组测试模块。在第" + str(
                                                self.iteration) + "组测试中，您将看到一串非汉字的遮挡性字符串，分别在中文词汇的先后持续展200 ms左右。该组测试完成后，屏幕右侧将弹出一份问卷，请您根据体验情况填写，并点击提交。</span></p></body></html>"))

        # # 每秒计数器计数结束后更新计数板数字
        # self.timer.timeout.connect(self.setText)
        # self.ans_timer.timeout.connect(self.timeOut)
        # self.status_timer.timeout.connect(self.statusTimeOut)
        # # 单击按钮计数开始
        # self.start_confirm_button.clicked.connect(self.startCount)
        #
        # self.trueButton.clicked.connect(self.clickT)
        # self.FalseButton.clicked.connect(self.clickF)
        # self.commitButton.clicked.connect(self.surveySummary)

    # 绑定信号与槽
    def init_run(self):

        # print("进入run")  # debug
        self.iteration = 1
        random.shuffle(self.mode_list)
        self.mode = self.mode_list[self.iteration]
        # print(self.mode)  # debug

        self.selectMode()
        # print("self.mode", self.mode)  # debug

        self.cur_time = 1000
        self.cha_time = 200

        self.trueButton.hide()
        self.FalseButton.hide()
        self.quiz.hide()
        self.commitButton.hide()

        self.mutex = 0
        self.sec = None

        self.tot_prac = 0
        self.it = -1

        self.true_count = 0
        self.false_count = 0
        self.change = list()

        self.pos_list = list()
        self.neg_list = list()

        self.a = True


        # 每秒计数器计数结束后更新计数板数字
        self.timer.timeout.connect(self.setText)
        self.ans_timer.timeout.connect(self.timeOut)
        self.status_timer.timeout.connect(self.statusTimeOut)
        # 单击按钮计数开始
        self.start_confirm_button.clicked.connect(self.startCount)

        self.trueButton.clicked.connect(self.clickT)
        self.FalseButton.clicked.connect(self.clickF)
        self.commitButton.clicked.connect(self.surveySummary)
        self.exitButton.clicked.connect(self.exit)

    def clickT(self):
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        self.status_timer.start(500)
        if self.a:
            self.statusLabel.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
            if self.true_count == 3:
                if self.cur_time == 17:
                    self.change.append(-2)
                elif self.cur_time > 17:
                    self.cur_time -= self.cha_time
                    if self.cur_time < 17:
                        self.cur_time = 17
                    self.change.append(-1)
                    self.neg_list.append(-1)
                self.true_count = 0
            else:
                self.change.append(-2)
        else:
            self.statusLabel.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0

            if self.cur_time == 1200:
                self.change.append(2)
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
        # print("clickt 调用startcount")  # debug
        self.cur_time_list.append(self.cur_time)
        self.startCount()

    def clickF(self):
        self.mutex = 0
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        self.status_timer.start(500)
        if not self.a:
            self.statusLabel.setText(_translate("MainWindow", "回答正确"))
            # global true_count
            self.true_count += 1
            if self.true_count == 3:
                if self.cur_time == 17:
                    self.change.append(-2)
                elif self.cur_time > 17:
                    self.cur_time -= self.cha_time
                    if self.cur_time < 17:
                        self.cur_time = 17
                    self.change.append(-1)
                    self.neg_list.append(-1)
                self.true_count = 0
            else:
                self.change.append(-2)
        else:
            self.statusLabel.setText(_translate("MainWindow", "回答错误"))
            # global false_count
            self.true_count = 0

            if self.cur_time == 1200:
                self.change.append(2)
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
        # print("clickf 调用startcount")  # debug
        self.cur_time_list.append(self.cur_time)
        self.startCount()

    def timeOut(self):
        self.ans_timer.stop()
        _translate = QtCore.QCoreApplication.translate
        self.status_timer.start(500)
        self.statusLabel.setText(_translate("MainWindow", "作答超时"))

        self.true_count = 0

        if self.cur_time == 1200:
            self.change.append(2)
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
        # print("timeout 调用startcount")  # debug
        self.cur_time_list.append(self.cur_time)
        self.startCount()

    def surveySummary(self):
        quiz1 = self.comboBox.currentText()
        quiz2 = self.comboBox_2.currentText()
        quiz3 = self.comboBox_3.currentText()
        quiz4 = self.comboBox_4.currentText()
        with open("output.csv", "a") as file:
            file.write(str(self.mode) + ',' + quiz1 + ',' + quiz2 + ',' + quiz3 + ',' + quiz4 + "\n")

        # print(quiz1, quiz2, quiz3, quiz4)  # debug
        self.run()
        # print(self.it)  # debug
        # return
        # pass

    def exit(self):
        self.close()

    def survey(self):
        self.quiz.show()
        self.commitButton.show()


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
