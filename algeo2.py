from gmpy2 import *
import numpy as np

# Inisiasi precision
get_context().precision = 100

def scalar(u,uVec):
	sqrscalar = 0
	for i in range(len(u)):
		if (i in uVec):
			sqrscalar += pow(u[i],2)
	return sqrt(sqrscalar)

def CosineSimilarity(u, v, uVec):
	dotProduct = 0
	assert(len(u)==len(v))
	for i in range(len(u)):
		if (i in uVec):
			dotProduct += u[i]*v[i]
	'''
	print()
	print(u[i],v[i])
	print(dotProduct,mul(scalar(u,uVec),scalar(v,uVec)))
	'''
	return div(dotProduct,mul(scalar(u,uVec),scalar(v,uVec)))

def CosineSimilarityMat(M1, M2, uVec):
	M = []
	for i in range(len(M1)):
		M.append(1-CosineSimilarity(M1[i],M2[0],uVec))
	return np.array(M)