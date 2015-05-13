# -*- coding:utf-8 -*-
import sys
import math
from sklearn.cluster import KMeans
from random import sample

def tf(doc, term):
	n = 0
	for s in doc:
		if s.lower() == term:
			n += 1
	return float(n)/len(doc)

def idf(docs, term):
	n = 0
	for doc in docs:
		for s in doc:
			if s.lower() == term:
				n += 1
				break
	return math.log(len(docs)/(float(n)+1))


def cosSim(v1, v2):
	dotp, mag1, mag2 = 0.0, 0.0, 0.0
	for i in range(len(v1)):
		dotp += v1[i]*v2[i]
		mag1 += math.pow(v1[i], 2)
		mag2 += math.pow(v2[i], 2)
	mag1 = math.sqrt(mag1)
	mag2 = math.sqrt(mag2)
	try:
		return dotp/(mag1*mag2)
	except ZeroDivisionError:
		return 0

def loadDoc(filename):
	docs = []
	for line in file(filename):
		docs.append(line.strip().split())
	return docs

def loadTerms(docs):
	terms = set()
	for doc in docs:
		for s in doc:
			terms.add(s.lower())
	return terms


def loadVecSpace(docs):
	terms = list(loadTerms(docs))
	vecs = []

	for doc in docs:
		vec = []
		for i in range(len(terms)):
			f1 = tf(doc, terms[i])
			f2 = idf(docs, terms[i])
			vec.append(f1*f2)
		vecs.append(vec)
	return vecs

def calcTopSim(doc, docs, K):
	terms = list(loadTerms(docs))

	vec = []

	for i in range(len(terms)):
		f1 = tf(doc, terms[i])
		f2 = idf(docs, terms[i])
		vec.append(f1*f2)

	vecs = loadVecSpace(docs)

	scores = []
	for i in range(len(vecs)):
		scores.append(cosSim(vec, vecs[i]))
	
	scores_desc = sorted(list(enumerate(scores)), key=lambda d:d[1], reverse=True)

	for i in range(K):
		print i, scores_desc[i][1], " ".join(docs[scores_desc[i][0]])

def cluster(docs):
	est = KMeans(n_clusters=3, n_init=5, init='random')
	X = loadVecSpace(docs)
	est.fit(X)
	labels = est.labels_

	for i in range(len(labels)):
		print labels[i], " ".join(docs[i])

def euclideanDistance(v1, v2):
	mag = 0.0
	for i in range(len(v1)):
		mag += math.pow(v1[i]-v2[i], 2)
	return math.sqrt(mag)

def vecDistance(v1, v2):
	return euclideanDistance(v1, v2)

def loadDistance(vecs):
	distances = []
	for i in range(len(vecs)):
		distance = []
		for j in range(len(vecs)):
			distance.append(vecDistance(vecs[i], vecs[j]))
		distances.append(distance)
	return distances

def test_distance():
	docs = loadDoc(sys.argv[1])
	vecs = loadVecSpace(docs)
	distances = loadDistance(vecs)
	K = 10
	idxs = [9, 30, 48, 58, 87, 98, 147, 320, 347, 348, 358, 394, 433, 453, 462, 512, 533, 581, 608, 633]
	for i in range(len(idxs)):
		idx = idxs[i]
		distance = distances[idx]
		distance_inc = sorted(list(enumerate(distance)), key=lambda d:d[1])
		for i in range(K):
			print i, distance_inc[i][1], " ".join(docs[distance_inc[i][0]])
		print
		
def test():
	docs = loadDoc(sys.argv[1])

	#query = raw_input()
	query = "基本 款 情侣 短袖"
	calcTopSim(query.strip().split(), docs, 10)

def test_cluster():
	docs = loadDoc(sys.argv[1])
	cluster(docs)

if __name__ == "__main__":
	#test()
	#test_cluster()
	test_distance()
