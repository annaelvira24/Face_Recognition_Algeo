from gmpy2 import *
from matcher import *
import numpy as np
import cv2
import random

# Inisiasi precision
get_context().precision = 100

# Variable Global
db_dir = 'DB/'

'''
ma = Matcher('features.pck')
names, match = ma.matchCosine(files[0])
'''
def show_img(path):
	img = cv2.imread(path, 1)
	cv2.imshow('IMAGE', img)
	cv2.waitKey(0)

def run(sample):
    matcher = Matcher('DATA/DATASETS/', 'DB/real5.pck')
    names, match = matcher.matchCosine(sample)
    return names[1]

def main():
	matcher = Matcher('DATA/DATASETS/', 'DB/real5.pck')
	#sample = ['TEST/test1.jpg','TEST/huhu.jpg','TEST/test2.jpg','TEST/test4.jpg','TEST/test6.jpg','TEST/test5.jpg']
	benar = 0
	for i in range(5):
		sample = [random.choice(matcher.names) for i in range(1)]
		for s in sample:
			print("Sample Image")
			#show_img(s)
			print("Sorting Time")
			names, match = matcher.matchCosine(s)
			print("*DONE*")
			for i in range(1,2):
				print('Match %s' % (1-match[i]))
				if (s[:-10] in names[i]):
					benar += 1
				#show_img(names[i])
		print(benar)

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