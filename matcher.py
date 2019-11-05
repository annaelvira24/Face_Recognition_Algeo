from gmpy2 import *
from algeo import *
import numpy as np
import cv2
import _pickle as pickle
import os

# Inisiasi precision
get_context().precision = 100

class Matcher(object):
	def __init__(self, path, db_path="features.pck"):
		try:
			print("Trying to read data from "+db_path+"....")
			self.data = pickle.load(open(db_path, "rb"))
			print("*SUCCESS*")
		except:
			print("*FAILED*")
			print("Creating data from "+path+" to "+db_path+"....")
			createDB(db_path)
			self.data = pickle.load(open(db_path, "rb"))
		self.names, self.db = map(np.array, zip(*self.data.items()))

	def cosineSim(self, vector):
		return cosineSimilarity(self.db, np.array(vector))

	def normEuclid(self, vector):
		return normEuclidean(self.db, np.array(vector))

	def matchCosine(self, image_path):
		features = extract(image_path)
		distanceRange = self.cosineSim(features)
		sortidx = np.argsort(distanceRange)
		return self.names[sortidx], distanceRange[sortidx]

	def matchEuclid(self, image_path):
		features = extract(image_path)
		distanceRange = self.normEuclid(features)
		sortidx = np.argsort(distanceRange)
		return self.names[sortidx], distanceRange[sortidx]

def extract(image_path, vsize=8):
	#RGB
	img = cv2.imread(image_path, 1)
	#if (cv2.countNonZero(cv2.imread(image_path, 0)) < int(img.size*0.7)):
	#	img = img[int(len(img)*0.05):int(len(img)*0.95), int(len(img[0])*0.05):int(len(img[0])*0.95)]
	#img = cv2.GaussianBlur(img, (5,5), 0)
	#img =cv2.resize(img, (img.shape[0], img.shape[1]))
	kaze = cv2.KAZE_create()
	kps = kaze.detect(img)
	kps_temp = sorted(kps, key=lambda x: abs(x.response))[:vsize//2]
	dsc = kaze.compute(img, kps_temp)[1]
	kps_temp = sorted(kps, key=lambda x: x.size)[:vsize//2]
	#kps_temp = sorted(kps_temp, key=lambda x: abs(x.response))[:vsize//2]
	dsc2 = kaze.compute(img, kps_temp)[1]
	kps_temp = sorted(kps, key=lambda x: x.angle)[:vsize//4]
	#kps_temp = sorted(kps_temp, key=lambda x: abs(x.response))[:vsize//3]
	dsc3 = kaze.compute(img, kps_temp)[1]
#	kps_temp = sorted(kps, key=lambda x: -x.response)[:vsize//2]
#	dsc4 = kaze.compute(img, kps_temp)[1]
	dsc = np.concatenate([dsc.flatten('C'),dsc2.flatten('C'),dsc3.flatten('C')], axis=None)
	needed_size = (vsize * 2 * 64)
	if dsc.size < needed_size:
		dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
	return dsc

def createDB(db_path="features.pck"):
	result = {}
	try:
		files_db = pickle.load(open("DB/listdataset","rb"))
	except:
		files_db = []
		for path in os.listdir("DataSet"):
			for image in os.listdir(os.path.join("DataSet",path)):
				files_db.append(os.path.join(os.path.join("DataSet",path),image))
		pickle.dump(files_db, open("DB/listdataset", 'wb'))
	i = 1
	mark = 1
	for f in files_db:
		result[f] = extract(f)
		pr = (i/len(files_db))*100
		if (pr > mark):
			print("EXTRACTING %.2f%c..." % (pr,'%'))
			mark += 1
		i += 1
	pickle.dump(result, open(db_path, 'wb'))


