import numpy as np
import cv2
from matplotlib import pyplot as plt


class brute_force_function():

	def __init__(self,parent = None):
		self.file = file_1
		self.file = file_2


	def open_picture_1(self,file_1):
		img1 = cv2.imread(file_1,0)

		return img1


	def open_picture_2(self,file_2):
		img2 = cv2.imread(file_2,0)

		return img2


	def method_call(self,img1,img2):

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

		return img3
