from gmpy2 import *
from algeo import *
import numpy as np
import matplotlib.pyplot as plt
import cv2
import scipy
import _pickle as pickle
import random
import os

# Variable Global
images_path = 'TEST/'
files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

# Inisiasi precision
get_context().precision = 1000

def extract(image_path, vsize=100):
	img = cv2.imread(image_path, 0)
	img = img[int(len(img)*0.1):int(len(img)*0.9), int(len(img[0])*0.1):int(len(img[0])*0.9)]
	kaze = cv2.KAZE_create()
	kps = kaze.detect(img)
	kps = sorted(kps, key=lambda x: -x.response)[:vsize]
	kps, dsc = kaze.compute(img, kps)
	dsc = dsc.flatten('K')
	needed_size = (vsize * 64)
	if dsc.size < needed_size:
		dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
	return dsc

def createDB(images_path, db_path="features.pck"):
	result = {}
	for f in files:
		name = f.split('/')[-1].lower()
		result[name] = extract(f)
	pickle.dump(result, open(db_path, 'wb'))


class Matcher(object):
	def __init__(self, db_path="features.pck"):
		self.data = pickle.load(open(db_path, "rb"))
		self.names, self.db = map(np.array, zip(*self.data.items()))

	def cosineSim(self, vector):
		v = vector.reshape(1, -1)
		return CosineSimilarityMat(self.db, v).reshape(-1)

	def match(self, image_path, topn=5):
		features = extract(image_path)
		img_distances = self.cosineSim(features)
		# getting top 5 records
		nearest_ids = np.argsort(img_distances)[:topn].tolist()
		nearest_img_paths = self.names[nearest_ids].tolist()
		return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
	img = cv2.imread(path, 0)
	cv2.imshow('IMAGE', img)
	cv2.waitKey(0)
   
def run():
    # getting 3 random images 
    sample = [files[8],files[4]]
    
    createDB(images_path)

    ma = Matcher('features.pck')
    
    for s in sample:
        print('Query image ==========================================')
        show_img(s)
        names, match = ma.match(s, topn=5)
        print('Result images ========================================')
        for i in range(5):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
            print('Match %s' % (1-match[i]))
            show_img(os.path.join(images_path, names[i]))

run()