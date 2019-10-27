from gmpy2 import *
import numpy as np

# Inisiasi precision
get_context().precision = 100

def normEuclidean(M, v):
	res = []
	for i in range(len(M)):
		res.append(np.norm(M[i]-v))
	return np.array(res)

def cosineSimilarity(M, v):
	res = []
	for i in range(len(M)):
		res.append(1-((np.dot(M[i],v)/(np.linalg.norm(M[i])*np.linalg.norm(v)))))
	return np.array(res)