# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

#from PyQt4 import QtCore, QtGui

try:
    from PySide import QtCore, QtGui
except ImportError:
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(388, 251)
        self.pushButton = QtGui.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 111, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(About)
        self.label.setGeometry(QtCore.QRect(160, 20, 71, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 101, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 91, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(120, 140, 161, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(About)
        self.label_5.setGeometry(QtCore.QRect(170, 110, 71, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "Dialog", None))
        self.pushButton.setText(_translate("About", "Close", None))
        self.label.setText(_translate("About", "Create By", None))
        self.label_2.setText(_translate("About", "Rifqi Muttaqin", None))
        self.label_3.setText(_translate("About", "0651-14-039", None))
        self.label_4.setText(_translate("About", "https://github.com/rifqi31", None))
        self.label_5.setText(_translate("About", "Github", None))

