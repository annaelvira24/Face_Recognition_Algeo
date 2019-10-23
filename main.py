from gmpy2 import *
from matcher import *
import numpy as np
import cv2
import random

# Inisiasi precision
get_context().precision = 100

# Variable Global
matcherDB = []
db_dir = 'DB/'

'''
ma = Matcher('features.pck')
names, match = ma.matchCosine(files[0])
'''
def show_img(path):
	img = cv2.imread(path, 1)
	cv2.imshow('IMAGE', img)
	cv2.waitKey(0)

def createMatcherDB():
	for i in range(len(dirs)):
		matcherDB.append(Matcher(dirs[i],db_dir+dirs[i].split("/")[1].split(".")[0]+'.pck'))

def main():
	createMatcherDB()
	sample = ['TEST/test1.jpg','TEST/test3.jpg','TEST/test2.jpg','TEST/test4.jpg','TEST/test6.jpg','TEST/test5.jpg']
	for s in sample[0:3]:
		print("Sample Image")
		show_img(s)
		print("Sorting Time")
		names, match = np.concatenate([matcherDB[i].matchCosine(s)[0] for i in range(len(matcherDB))], axis=None), np.concatenate([matcherDB[i].matchCosine(s)[1] for i in range(len(matcherDB))], axis=None)
		sortidx = np.argsort(match)
		names = names[sortidx]
		match = match[sortidx]
		print("*DONE*")
		for i in range(3):
			print('Match %s' % (1-match[i]))
			show_img(names[i])

main()
'''
def run():
    # getting 3 random images 
    sample = ['TEST/huhu.jpg']
    p1 = Matcher('1/','1.pck')
    p2 = Matcher('2/','2.pck')
    
    for s in sample:
        print('Query image ==========================================')
        show_img(s)
        names, match = np.concatenate((p1.matchCosine(s)[0],p2.matchCosine(s)[0]), axis=None), np.concatenate((p1.matchCosine(s)[1],p2.matchCosine(s)[1]), axis=None)
        #print(match)
        #match = np.array(map(mpfr,match))
        print(len(match))
        sortidx = np.argsort(match)
        names = names[sortidx]
        match = match[sortidx]
        print('Result images ========================================')
        for i in range(5):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
            print('Match %s' % (1-match[i]))
            try:
                show_img(os.path.join('1/', names[i]))
            except:
                show_img(os.path.join('2/', names[i]))

run()
'''