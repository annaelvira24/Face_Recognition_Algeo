from gmpy2 import *
from matcher import *
import numpy as np
import cv2
import random
import datetime

# Inisiasi precision
get_context().precision = 100

# Variable Global
db_dir = 'DB/'
image_dir = 'PICS'
used_db = 'DB/final'
datauji = 'DataUji'

def showCmp(path,path2):
	img = np.hstack((cv2.imread(path, 1), cv2.imread(path2, 1)))
	cv2.imshow('IMAGE', img)
	cv2.waitKey(0)

def testrun():
	matcher = Matcher(datauji, used_db)
	try:
		images = pickle.load(open("DB/listdatauji","rb"))
	except:
		images = []
		for path in os.listdir("DataUji"):
			for image in os.listdir(os.path.join("DataUji",path)):
				images.append(os.path.join(os.path.join("DataUji",path),image))
		pickle.dump(images, open("DB/listdatauji", 'wb'))
	sample = random.choice(images)
	print("Starting the test....")
	names, match = matcher.matchCosine(sample)
	print('Match %s' % (1-match[0]))
	showCmp(sample,names[0])

def runWithCosineSim(sample):
	matcher = Matcher(datauji, used_db)
	names, match = matcher.matchCosine(sample)
	return names[0:10], match[0:10]

def runWithNormEuclid(sample):
	matcher = Matcher(datauji, used_db)
	names, match = matcher.matchEuclid(sample)
	return names[0:10], match[0:10], match[-1]

def pickSamples():
	paths = os.listdir(image_dir)
	os.system("rm -r DataUji")
	os.system("mkdir DataUji")
	os.system("rm -r DataSet")
	os.system("mkdir DataSet")
	for path in paths:
		images = os.listdir(os.path.join(image_dir,path))
		samples = []
		for _ in range(int(len(images)*0.2)):
			i = random.randint(0,len(images)-1)
			samples.append(images[i])
			images.pop(i)
		os.system("mkdir '"+os.path.join("DataUji",path)+"'")
		os.system("mkdir '"+os.path.join("DataSet",path)+"'")
		for i in images:
			os.system("cp '"+os.path.join(os.path.join(image_dir,path),i)+"' '"+os.path.join("DataSet",path)+"'")
		for i in samples:
			os.system("cp '"+os.path.join(os.path.join(image_dir,path),i)+"' '"+os.path.join("DataUji",path)+"'")
	images = []
	for path in os.listdir("DataUji"):
		for image in os.listdir(os.path.join("DataUji",path)):
			images.append(os.path.join(os.path.join("DataUji",path),image))
	pickle.dump(images, open("DB/listdatauji", 'wb'))
	images = []
	for path in os.listdir("DataSet"):
		for image in os.listdir(os.path.join("DataSet",path)):
			images.append(os.path.join(os.path.join("DataSet",path),image))
	pickle.dump(images, open("DB/listdataset", 'wb'))

def generateDB(save):
	if (save):
		x = "_".join(str(datetime.datetime.now()).split(".")[0].split(" "))
		os.system("mv "+used_db+" "+used_db+x)
	createDB(used_db)


def accurate():
	matcher = Matcher(datauji, used_db)
	benar = 0
	try:
		images = pickle.load(open("DB/listdatauji","rb"))
	except:
		images = []
		for path in os.listdir("DataUji"):
			for image in os.listdir(os.path.join("DataUji",path)):
				images.append(os.path.join(os.path.join("DataUji",path),image))
		pickle.dump(images, open("DB/listdatauji", 'wb'))
		
	for i in range(100):
		sample = [random.choice(images) for i in range(1)]
		for s in sample:
			names, match = matcher.matchCosine(s)
			if (s[:-13] in names[0]):
				benar += 1
	print("Tingkat akurasi program dengan cosine similarity: %.2f." % (benar/100))

	benar = 0
	for i in range(100):
		sample = [random.choice(images) for i in range(1)]
		for s in sample:
			names, match = matcher.matchEuclid(s)
			if (s[:-13] in names[0]):
				benar += 1
	print("Tingkat akurasi program dengan euclidean distance: %.2f." % (benar/100))