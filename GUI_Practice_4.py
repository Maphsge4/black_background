# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Practice_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 363)
        MainWindow.setStyleSheet("background-color:rgb(98,98,98)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 5, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 131))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 131))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 4, 1, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setMinimumSize(QtCore.QSize(75, 52))
        self.statusLabel.setMaximumSize(QtCore.QSize(75, 52))
        self.statusLabel.setStyleSheet("color:rgb(255, 255, 255);\n"
                                       "font-size:20")
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_2.addWidget(self.statusLabel, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(75, 44))
        self.label.setMaximumSize(QtCore.QSize(75, 44))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,255,255);\n"
                                 "border:2px solid rgb(255,255,255);\n"
                                 "font-size:14pt")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 3, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2.addWidget(self.widget_5, 0, 6, 5, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 73))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 73))
        font = QtGui.QFont()
        font.setFamily("楷体")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 1, 1, 5)
        self.FalseButton = QtWidgets.QPushButton(self.centralwidget)
        self.FalseButton.setMinimumSize(QtCore.QSize(121, 131))
        self.FalseButton.setStyleSheet("color:rgb(255, 12, 12)")
        self.FalseButton.setObjectName("FalseButton")
        self.gridLayout_2.addWidget(self.FalseButton, 4, 4, 1, 1)
        self.trueButton = QtWidgets.QPushButton(self.centralwidget)
        self.trueButton.setMinimumSize(QtCore.QSize(131, 131))
        self.trueButton.setStyleSheet("color:rgb(85, 255, 0)")
        self.trueButton.setObjectName("trueButton")
        self.gridLayout_2.addWidget(self.trueButton, 4, 2, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet("color:rgb(255,255,255)")
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_2.addWidget(self.exitButton, 4, 5, 1, 1)
        self.quiz = QtWidgets.QWidget(self.centralwidget)
        self.quiz.setMinimumSize(QtCore.QSize(242, 221))
        self.quiz.setObjectName("quiz")
        self.layoutWidget = QtWidgets.QWidget(self.quiz)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 1, 242, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(240, 16))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(174, 16))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setStyleSheet("color:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMaximumSize(QtCore.QSize(204, 16))
        self.label_8.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(162, 16))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMaximumSize(QtCore.QSize(228, 16))
        self.label_9.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(162, 16))
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(204, 16))
        self.label_10.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(174, 16))
        self.label_6.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 7, 1, 1, 1)
        self.gridLayout_2.addWidget(self.quiz, 0, 7, 3, 1)
        self.start_confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_confirm_button.setMaximumSize(QtCore.QSize(75, 23))
        self.start_confirm_button.setStyleSheet("color:rgb(255,255,255)")
        self.start_confirm_button.setObjectName("start_confirm_button")
        self.gridLayout_2.addWidget(self.start_confirm_button, 4, 3, 1, 1)
        self.commitButton = QtWidgets.QPushButton(self.centralwidget)
        self.commitButton.setMaximumSize(QtCore.QSize(75, 23))
        self.commitButton.setStyleSheet("color:rgb(255, 255, 255)")
        self.commitButton.setObjectName("commitButton")
        self.gridLayout_2.addWidget(self.commitButton, 4, 7, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'楷体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; color:#ffffff;\">现在是练习模式。在练习模式中，</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; font-weight:600; color:#ffffff;\">请您判断每组中的两个中文词汇是否相同，相同请按键盘</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:12pt; font-weight:600; color:#ffffff;\">Y</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; font-weight:600; color:#ffffff;\">键，不相同请按键盘</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:12pt; font-weight:600; color:#ffffff;\">N</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; font-weight:600; color:#ffffff;\">键</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; color:#ffffff;\">。连续答对</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:12pt; color:#ffffff;\">5</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; color:#ffffff;\">道题后，屏幕右侧将弹出一份问卷，请您根据体验情况填写，并点击提交。提交后将进入主测试环节。若没有连续答对</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:12pt; color:#ffffff;\">5</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; color:#ffffff;\">道题，请您点击</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:12pt; color:#ffffff;\">“</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; color:#ffffff;\">开始</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:12pt; color:#ffffff;\">”</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:12pt; color:#ffffff;\">重新练习。</span></p></body></html>"))

        self.FalseButton.setText(_translate("MainWindow", "N 错误"))
        self.trueButton.setText(_translate("MainWindow", "Y 正确"))
        self.exitButton.setText(_translate("MainWindow", "退出测试"))
        self.label_2.setText(_translate("MainWindow", "1.你认为这种颜色组合中的字符易读性如何？"))
        self.label_3.setText(_translate("MainWindow", "非常不清楚 1 2 3 4 5 非常清楚"))
        self.comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox.setItemText(1, _translate("MainWindow", "4"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "2"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "2.你认为这种颜色组合的外观美观吗？"))
        self.label_4.setText(_translate("MainWindow", "很不美观 1 2 3 4 5 非常美观"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "3.你认为这种颜色组合的视觉舒适度如何？"))
        self.label_5.setText(_translate("MainWindow", "很不舒服 1 2 3 4 5 非常舒适"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "4.你对这种颜色组好的喜好程度如何？"))
        self.label_6.setText(_translate("MainWindow", "很不喜欢 1 2 3 4 5 非常喜欢"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "4"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "1"))
        self.start_confirm_button.setText(_translate("MainWindow", "开始"))
        self.commitButton.setText(_translate("MainWindow", "提交"))
