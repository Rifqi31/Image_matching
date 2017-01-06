from __future__ import with_statement

import cv2
import numpy as np 
import sys
from PySide import QtCore,QtGui
from matplotlib import pyplot as plt

import os

from prototype import Ui_MainWindow

from main_about import main_about

#import a function
#from brute_force import brute_force_function


class main_function(QtGui.QMainWindow,Ui_MainWindow):
	"""docstring for Main_function"""
	def __init__(self, parent = None):
		super(main_function, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.setupUi(self)


		#menubar source code

		#File

		#File->New
		self.menuFile.addAction(self.File_New)
		self.File_New.triggered.connect(self.new_window)


		#File->Open->Open Picture 1
		self.menuOpen.addAction(self.Upload_Pic1)
		self.Upload_Pic1.triggered.connect(self.open_image_1)


		#File->Open->Open Picture 2
		self.menuOpen.addAction(self.Upload_Pic2)
		self.Upload_Pic2.triggered.connect(self.open_image_2)


		#File->Quit
		self.menuFile.addAction(self.File_Quit)
		self.File_Quit.triggered.connect(self.close_application)



		#Edit

		#Edit->Method->Brute-force
		self.menuMethod.addAction(self.actionBrute_force)
		self.actionBrute_force.triggered.connect(self.brute_force_function)


		#Edit->Method->Flann
		self.menuMethod.addAction(self.actionFlann)
		self.actionFlann.triggered.connect(self.flann_function)



		#Help

		#Help->About
		self.menuHelp.addAction(self.Help_About)
		self.Help_About.triggered.connect(self.about_out)



		#button function

		#Brute-force function
		QtCore.QObject.connect(self.brute_force_button,QtCore.SIGNAL("clicked()"),self.brute_force_function)

		#Flann function
		QtCore.QObject.connect(self.Flann_button,QtCore.SIGNAL("clicked()"),self.flann_function)






	#draw a function

	#function menu file in here

	def new_window(self):
		self.new = main_function(self)
		self.new.show()



	#gambar ke 1

	def open_image_1(self):

		self.file_1 = QtGui.QFileDialog.getOpenFileName()

		if self.file_1:
			self.scene = QtGui.QGraphicsScene()
			pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.file_1[0]))
			__width = pic_Item.boundingRect().width()
			__height = pic_Item.boundingRect().height()
			__x = self.gambar_ke1 .x()
			__y = self.gambar_ke1 .y()
			self.gambar_ke1.setGeometry(QtCore.QRect(__x, __y, __width, __height))

			__main_x = int(__x + __width + 20)
			__main_y = int(__y + __height + 50)
			self.resize(__main_x,__main_y)
			self.scene.addItem(pic_Item)
			self.gambar_ke1.setScene(self.scene)

			return self.file_1



	#gambar ke 2

	def open_image_2(self):

		self.file_2 = QtGui.QFileDialog.getOpenFileName()

		if self.file_2:
			self.scene = QtGui.QGraphicsScene()
			pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.file_2[0]))
			__width = pic_Item.boundingRect().width()
			__height = pic_Item.boundingRect().height()
			__x = self.gambar_ke2 .x()
			__y = self.gambar_ke2 .y()
			self.gambar_ke2.setGeometry(QtCore.QRect(__x, __y, __width, __height))

			__main_x = int(__x + __width + 20)
			__main_y = int(__y + __height + 50)
			self.resize(__main_x,__main_y)
			self.scene.addItem(pic_Item)
			self.gambar_ke2.setScene(self.scene)

			return self.file_2




	#close application
	def close_application(self):
		self.close()




	#function menu edit in here

	def brute_force_function(self):


		img1 = cv2.imread(self.file_1[0],0)

		# queryImage
		img2 = cv2.imread(self.file_2[0],0) # trainImage

		# Initiate SIFT detector
		orb = cv2.ORB_create()

		# find the keypoints and descriptors with SIFT
		kp1, des1 = orb.detectAndCompute(img1,None)
		kp2, des2 = orb.detectAndCompute(img2,None)

		# create BFMatcher object
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

		# Match descriptors.
		matches = bf.match(des1,des2)

		# Sort them in the order of their distance.
		matches = sorted(matches, key = lambda x:x.distance)

		# Draw first 10 matches.
		img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
		plt.imshow(img3)
		plt.show()



	def flann_function(self):


		img1 = cv2.imread(self.file_1[0],0)
		# queryImage
		img2 = cv2.imread(self.file_2[0],0) # trainImage

		# Initiate SIFT detector
		sift = cv2.xfeatures2d.SIFT_create()

		# find the keypoints and descriptors with SIFT
		kp1, des1 = sift.detectAndCompute(img1,None)

		kp2, des2 = sift.detectAndCompute(img2,None)

		# FLANN parameters
		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
		search_params = dict(checks=50)

		# or pass empty dictionary
		flann = cv2.FlannBasedMatcher(index_params,search_params)
		matches = flann.knnMatch(des1,des2,k=2)

		# Need to draw only good matches, so create a mask
		matchesMask = [[0,0] for i in xrange(len(matches))]

		# ratio test as per Lowe's paper
		for i,(m,n) in enumerate(matches):
			if m.distance < 0.7*n.distance:
				matchesMask[i]=[1,0]

		draw_params = dict(matchColor = (0,255,0),
							singlePointColor = (255,0,0),
							matchesMask = matchesMask,
							flags = 0)

		img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

		plt.imshow(img3,),plt.show()






	#function menu help in here

	def about_out(self):
		self.window_about = main_about(self)
		self.window_about.show()





if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = main_function()
	main.show()
	sys.exit(app.exec_())