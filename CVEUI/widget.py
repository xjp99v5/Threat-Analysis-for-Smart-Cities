# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(696, 477)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(520, 450, 161, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 400, 381, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 61, 180, 311))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.figLabel = QtGui.QLabel(Form)
        self.figLabel.setGeometry(QtCore.QRect(220, 69, 455, 271))
        self.figLabel.setAutoFillBackground(False)
        self.figLabel.setText(_fromUtf8(""))
        self.figLabel.setObjectName(_fromUtf8("figLabel"))
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 20, 334, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.sysLabel = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sysLabel.setFont(font)
        self.sysLabel.setObjectName(_fromUtf8("sysLabel"))
        self.horizontalLayout_2.addWidget(self.sysLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(310, 350, 261, 26))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_3.addWidget(self.radioButton)
        spacerItem2 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        self.textBrowser.raise_()
        self.figLabel.raise_()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.update)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.show)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CVEDetection", None))
        self.label.setText(_translate("Form", "ISCAS CopyRight 2018-2020", None))
        self.pushButton.setText(_translate("Form", "更新数据库", None))
        self.pushButton_2.setText(_translate("Form", "漏洞威胁统计", None))
        self.pushButton_3.setText(_translate("Form", "威胁实时跟踪", None))
        self.sysLabel.setText(_translate("Form", "关键性基础设施漏洞实时追踪系统", None))
        self.radioButton.setText(_translate("Form", "柱状图", None))
        self.radioButton_2.setText(_translate("Form", "饼状图", None))

