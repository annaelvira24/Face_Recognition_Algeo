from gmpy2 import *
from matcher import *
import numpy as np
import cv2
import random

# Inisiasi precision
get_context().precision = 100

# Variable Global
db_dir = 'DB/'

def showCmp(path,path2):
	img = np.hstack((cv2.imread(path, 1), cv2.imread(path2, 1)))
	cv2.imshow('IMAGE', img)
	cv2.waitKey(0)

def testrun():
	matcher = Matcher('DATA/DATASETS/', 'DB/real7.pck') #paling bagus db real6 - 4 4 (2)
	sample = random.choice(matcher.names)
	print("Starting the test....")
	names, match = matcher.matchCosine(sample)
	print('Match %s' % (1-match[1]))
	showCmp(sample,names[1])
    
    
def runWithCosineSim(sample):
	matcher = Matcher('DATA/DATASETS/', 'DB/real7.pck') #paling bagus db real6 - 4 4 (2)
	names, match = matcher.matchCosine(sample)
	return names[1:11]

def runWithNormEuclid(sample):
	matcher = Matcher('DATA/DATASETS/', 'DB/real7.pck') #paling bagus db real6 - 4 4 (2)
	names, match = matcher.matchEuclid(sample)
	return names[1:11]

def accurate():
	matcher = Matcher('DATA/DATASETS/', 'DB/real7.pck') #best so far temp5
	'''
	real7 4 (4) (2) best
	temp10 4 (8)/3 (2)
	temp9 4 (4) (8)/3
	temp8 4 (2) (2)
	temp7 4
	temp6 4 0 (2)
	temp5 4 (4) (2)
	temp4 4 4
	temp3 4 4 (2)
	temp2 4 4 4
	'''
	#sample = ['TEST/test1.jpg','TEST/huhu.jpg','TEST/test2.jpg','TEST/test4.jpg','TEST/test6.jpg','TEST/test5.jpg']
	benar = 0
	for i in range(100):
		sample = [random.choice(matcher.names) for i in range(1)]
		for s in sample:
			#print("Sample Image")
			#show_img(s)
			#print("Sorting Time")
			names, match = matcher.matchCosine(s)
			#print("*DONE*")
			for i in range(1,2):
				#print('Match %s' % (1-match[i]))
				if (s[:-13] in names[i]):
					benar += 1
	print("Tingkat akurasi program dengan cosine similarity: %.2f." % (benar/100))

	benar = 0
	for i in range(100):
		sample = [random.choice(matcher.names) for i in range(1)]
		for s in sample:
			#print("Sample Image")
			#show_img(s)
			#print("Sorting Time")
			names, match = matcher.matchEuclid(s)
			#print("*DONE*")
			for i in range(1,2):
				#print('Match %s' % (1-match[i]))
				if (s[:-13] in names[i]):
					benar += 1
	print("Tingkat akurasi program dengan euclidean distance: %.2f." % (benar/100))