# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_gui.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(857, 586)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gambar_ke1 = QtGui.QGraphicsView(self.centralwidget)
        self.gambar_ke1.setGeometry(QtCore.QRect(110, 30, 351, 371))
        self.gambar_ke1.setObjectName(_fromUtf8("gambar_ke1"))
        self.gambar_ke2 = QtGui.QGraphicsView(self.centralwidget)
        self.gambar_ke2.setGeometry(QtCore.QRect(490, 30, 351, 371))
        self.gambar_ke2.setObjectName(_fromUtf8("gambar_ke2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 30, 101, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.brute_force_button = QtGui.QPushButton(self.groupBox)
        self.brute_force_button.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.brute_force_button.setObjectName(_fromUtf8("brute_force_button"))
        self.Flann_button = QtGui.QPushButton(self.groupBox)
        self.Flann_button.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.Flann_button.setObjectName(_fromUtf8("Flann_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 10, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 430, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.output_calc = QtGui.QTextBrowser(self.centralwidget)
        self.output_calc.setGeometry(QtCore.QRect(110, 450, 511, 101))
        self.output_calc.setObjectName(_fromUtf8("output_calc"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOpen = QtGui.QMenu(self.menuFile)
        self.menuOpen.setObjectName(_fromUtf8("menuOpen"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuMethod = QtGui.QMenu(self.menuEdit)
        self.menuMethod.setObjectName(_fromUtf8("menuMethod"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.File_New = QtGui.QAction(MainWindow)
        self.File_New.setObjectName(_fromUtf8("File_New"))
        self.File_Quit = QtGui.QAction(MainWindow)
        self.File_Quit.setObjectName(_fromUtf8("File_Quit"))
        self.Help_About = QtGui.QAction(MainWindow)
        self.Help_About.setObjectName(_fromUtf8("Help_About"))
        self.actionBrute_Force = QtGui.QAction(MainWindow)
        self.actionBrute_Force.setObjectName(_fromUtf8("actionBrute_Force"))
        self.actionFlann = QtGui.QAction(MainWindow)
        self.actionFlann.setObjectName(_fromUtf8("actionFlann"))
        self.actionBrute_force = QtGui.QAction(MainWindow)
        self.actionBrute_force.setObjectName(_fromUtf8("actionBrute_force"))
        self.actionMatch = QtGui.QAction(MainWindow)
        self.actionMatch.setObjectName(_fromUtf8("actionMatch"))
        self.Upload_Pic1 = QtGui.QAction(MainWindow)
        self.Upload_Pic1.setObjectName(_fromUtf8("Upload_Pic1"))
        self.Upload_Pic2 = QtGui.QAction(MainWindow)
        self.Upload_Pic2.setObjectName(_fromUtf8("Upload_Pic2"))
        self.menuOpen.addAction(self.Upload_Pic1)
        self.menuOpen.addAction(self.Upload_Pic2)
        self.menuFile.addAction(self.File_New)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.File_Quit)
        self.menuMethod.addAction(self.actionBrute_force)
        self.menuEdit.addAction(self.menuMethod.menuAction())
        self.menuEdit.addAction(self.actionMatch)
        self.menuHelp.addAction(self.Help_About)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Matcher", None))
        self.groupBox.setTitle(_translate("MainWindow", "Tools", None))
        self.brute_force_button.setText(_translate("MainWindow", "Brute-Force", None))
        self.Flann_button.setText(_translate("MainWindow", "FLANN", None))
        self.label.setText(_translate("MainWindow", "Gambar 1", None))
        self.label_2.setText(_translate("MainWindow", "Gambar 2", None))
        self.label_3.setText(_translate("MainWindow", "Hasil Matching", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOpen.setTitle(_translate("MainWindow", "Open", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuMethod.setTitle(_translate("MainWindow", "Method", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.File_New.setText(_translate("MainWindow", "New", None))
        self.File_Quit.setText(_translate("MainWindow", "Quit", None))
        self.Help_About.setText(_translate("MainWindow", "About", None))
        self.actionBrute_Force.setText(_translate("MainWindow", "Brute-Force", None))
        self.actionFlann.setText(_translate("MainWindow", "Flann", None))
        self.actionBrute_force.setText(_translate("MainWindow", "Brute-force", None))
        self.actionMatch.setText(_translate("MainWindow", "Match..", None))
        self.Upload_Pic1.setText(_translate("MainWindow", "Upload Pic1", None))
        self.Upload_Pic2.setText(_translate("MainWindow", "Upload Pic2", None))

