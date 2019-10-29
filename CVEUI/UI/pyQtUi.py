# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 22:37
# @Author  : Jiaping Xiao
# @File    : pyQtUi.py

# !/user/bin/python3
# -*- coding:utf-8 -*-
'''''
Creat a simple window
'''
__author__ = 'Tony Zhu'

import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__== '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    w.setGeometry(0,0,200,200);
    w.setWindowTitle("Hello PyQt5")

    sys.exit(app.exec_())
