from __future__ import with_statement

import sys
from PySide import QtCore,QtGui
import os

from about import Ui_About


class main_about(QtGui.QMainWindow,Ui_About):
	def __init__(self, parent = None):
		super(main_about, self).__init__(parent)
		self.ui = Ui_About()
		self.setupUi(self)

		#button close
		self.pushButton.clicked.connect(self.close_window)



	# draw a function
	def close_window(self):
		self.close()



if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = main_about()
	main.show()
	sys.exit(app.exec_())	