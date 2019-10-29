# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 17:08
# @Author  : Jiaping Xiao
# @File    : Main.py
import sys
from UI import Windows as W

if __name__== '__main__':
    app = W.QtGui.QApplication(sys.argv)
    MainWindows = W.QtGui.QMainWindow()
    ui = W.Ui_MainWindow()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())