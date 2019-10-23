from gmpy2 import *
import numpy as np

def EuclideanDist (u,v):
	distSquare = 0
	dist = 0
	for i in range (len(u)):
		distSquare += (u[i]-v[i])**2
		dist		= (distSquare)**(0.5)
	return dist

u = [-1,2,3]
v = [4,0,-3]
print(EuclideanDist(u,v))


def scalar(u):
	sqrscalar = 0
	for i in range(len(u)):
		sqrscalar += pow(u[i],2)
	return sqrt(sqrscalar)

def CosineSimilarity(u, v):
	dotProduct = 0
	assert(len(u)==len(v))
	for i in range(len(u)):
		dotProduct += u[i]*v[i]
	return div(dotProduct,mul(scalar(u),scalar(v)))

def CosineSimilarityMat(M1, M2):
	M = []
	for i in range(len(M1)):
		arr = []
		for j in range(len(M2)):
			arr.append(1-CosineSimilarity(M1[i],M2[j]))
		M.append(arr)
	return np.array(M)