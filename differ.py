from gmpy2 import *
from algeo import *
import numpy as np
import cv2
import _pickle as pickle
import os

# Inisiasi precision
get_context().precision = 100

# Variable Global
images_path = 'TC/'
dirs = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

class Differ(object):
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
		self.uniqueVector = []

	def cosineSim(self, vector):
		v = vector.reshape(1, -1)
		return CosineSimilarityMat(self.db, v).reshape(-1)

	def findUselessVector(self, id=1):
		for i in range(len(self.db[0])):
			tc = self.db[0][i]
			val = 0
			arr = []
			for j in range(len(self.db)):
				val += self.db[j][i]
				arr.append(self.db[j][i])
			val = div(val,len(arr))/(max(arr)*min(arr))
			self.uniqueVector.append([i,val])
		with open("res"+str(id)+".txt","w") as f:
			for i in self.uniqueVector:
				f.write(str(i)+",\n")
		self.uniqueVector = list(zip(*sorted(self.uniqueVector,key=lambda x: x[1])))

	def matchCosine(self, image_path):
		features = extract(image_path)
		distanceRange = self.cosineSim(features)
		#similarIdx = np.argsort(distanceRange)
		#print(distanceRange)
		return self.names, distanceRange

def extract(image_path, vsize=16):
	img = cv2.imread(image_path, 1)
	#img = img[int(len(img)*0.05):int(len(img)*0.95), int(len(img[0])*0.05):int(len(img[0])*0.95)]
	kaze = cv2.KAZE_create()
	kps = kaze.detect(img)
	kps = sorted(kps, key=lambda x: -x.response)[:vsize]
	kps, dsc = kaze.compute(img, kps)
	dsc = dsc.flatten('K')
	needed_size = (vsize * 64)
	if dsc.size < needed_size:
		dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
	return dsc

def createDB(path,db_path="features.pck"):
	result = {}
	files_db = [os.path.join(path, p) for p in sorted(os.listdir(path))]
	for f in files_db:
		name = f.split('/')[-1].lower()
		result[name] = extract(f)
	pickle.dump(result, open(db_path, 'wb'))


