from gmpy2 import *
from algeo import *
import numpy as np
import cv2
import _pickle as pickle
import os

# Inisiasi precision
get_context().precision = 100

# Variable Global
images_path = 'HUHU/'
uvDB_dir = 'UVDB/'
dirs = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

class Matcher(object):
	def __init__(self, path, db_path="features.pck"):
		try:
			print("Trying to read data from "+db_path+"....")
			self.data = pickle.load(open(db_path, "rb"))
			print("*SUCCESS*")
		except:
			print("*FAILED*")
			print("Creating data from "+path+" to "+db_path+"....")
			createDB(path, db_path)
			self.data = pickle.load(open(db_path, "rb"))
		self.names, self.db = map(np.array, zip(*self.data.items()))
		self.names = np.array(list(map(lambda x: os.path.join(path,x), self.names)))
		'''
		try:
			print("Trying to read data from "+uvDB_dir+db_path.split("/")[1].split(".")[0]+"....")
			self.uniqueVector = pickle.load(open(uvDB_dir+db_path.split("/")[1].split(".")[0]+".uv", "rb"))
			print("*SUCCESS*")
		except:
			print("*FAILED*")
			print("Creating data from "+path+" to "+uvDB_dir+db_path.split("/")[1].split(".")[0]+"....")
			self.uniqueVector = []
			self.findUniqueVector()
			pickle.dump(self.uniqueVector, open(uvDB_dir+db_path.split("/")[1].split(".")[0]+".uv", "wb"))
		print(self.uniqueVector)
		'''

	def cosineSim(self, vector):
		return cosineSimilarity(self.db, np.array(vector))
	'''
	def findUniqueVector(self):
		init = 1
		cvec = 30
		while (len(self.uniqueVector) < cvec):
			self.uniqueVector = []
			for i in range(len(self.db[0])):
				tc = self.db[0][i]
				unique = True
				j = 0
				val = 0
				while(j < len(self.db) and unique):
					unique = (init <= (self.db[j][i]/tc) <= (1/init))
					val += (self.db[j][i]/tc)
					j += 1
				if (unique):
					self.uniqueVector.append([i,val/len(self.db)])
			init -= 0.01
		self.uniqueVector = list(zip(*sorted(self.uniqueVector,key=lambda x: abs(1-x[1]))[:cvec]))[0]
	'''
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
	kps_temp = sorted(kps, key=lambda x: x.size)[:vsize//3]
	#kps_temp = sorted(kps_temp, key=lambda x: abs(x.response))[:vsize//2]
	dsc2 = kaze.compute(img, kps_temp)[1]
	kps_temp = sorted(kps, key=lambda x: x.angle)[:vsize//2]
	#kps_temp = sorted(kps_temp, key=lambda x: abs(x.response))[:vsize//3]
	dsc3 = kaze.compute(img, kps_temp)[1]
	kps_temp = sorted(kps, key=lambda x: -x.response)[:vsize//2]
	dsc4 = kaze.compute(img, kps_temp)[1]
	dsc = np.concatenate([dsc.flatten('C'),dsc2.flatten('C'),dsc3.flatten('C'),dsc4.flatten('C')], axis=None)
	#Grayscale
	'''
	img = cv2.imread(image_path, 0)
	#if (cv2.countNonZero(cv2.imread(image_path, 0)) < int(img.size*0.7)):
	#	img = img[int(len(img)*0.05):int(len(img)*0.95), int(len(img[0])*0.05):int(len(img[0])*0.95)]
	#img = cv2.GaussianBlur(img, (5,5), 0)
	#img =cv2.resize(img, (img.shape[0], img.shape[1]))
	kps = kaze.detect(img)
	kps_temp = sorted(kps, key=lambda x: abs(x.response))[:vsize//2]
	dsc2 = kaze.compute(img, kps_temp)[1]
	kps_temp = sorted(kps, key=lambda x: x.size)[:vsize//3]
	kps_temp = sorted(kps_temp, key=lambda x: abs(x.response))[:vsize//2]
	dsc3 = kaze.compute(img, kps_temp)[1]
	kps_temp = sorted(kps, key=lambda x: x.angle)[:vsize//2]
	#kps_temp = sorted(kps_temp, key=lambda x: abs(x.response))[:vsize//3]
	dsc4 = kaze.compute(img, kps_temp)[1]
	dsc2 = np.concatenate([dsc,dsc2.flatten('C'),dsc3.flatten('C'),dsc4.flatten('C')], axis=None)
	'''
	'''
	kaze = cv2.KAZE_create()
	kps = kaze.detect(img)
	kps_temp = sorted(kps, key=lambda x: abs(x.response))[:vsize]
	dsc = kaze.compute(img, kps_temp)[1]
	kps = kaze.detect(img)
	kps_temp = sorted(kps, key=lambda x: abs(x.response))[:vsize]
	img = cv2.imread(image_path, 0)
	dsc2 = kaze.compute(img, kps_temp)[1]
	'''
	#dsc = np.concatenate([dsc.flatten('K'),dsc2.flatten('K')],axis=None)
	needed_size = (vsize * 2 * 64)
	if dsc.size < needed_size:
		dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
	return dsc

def createDB(path,db_path="features.pck"):
	result = {}
	files_db = [os.path.join(path, p) for p in sorted(os.listdir(path))]
	i = 1
	mark = 1
	for f in files_db:
		name = f.split('/')[-1].lower()
		result[name] = extract(f)
		pr = (i/len(files_db))*100
		if (pr > mark):
			print("EXTRACTING %.2f%c..." % (pr,'%'))
			mark += 1
		i += 1
	pickle.dump(result, open(db_path, 'wb'))


