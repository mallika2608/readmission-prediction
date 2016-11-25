import numpy as np
import math
import random
import itertools
import sys
import pylab
import os
import csv
import pickle
import warnings
from tempfile import TemporaryFile
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

from sklearn.model_selection import train_test_split

fileDir = os.path.dirname(os.path.realpath(__file__))
dataDir = os.path.join(fileDir, "dataset")

def readData(filePath):

	"""trainData = []

	with open(filePath, "rb") as csvFile:
		dataReader = csv.reader(csvFile, delimiter=",")

		for row in dataReader:
			trainData.append(row)
			#print row
			#break

	trainData = trainData[1:] #remove header row

	#print len(trainData)
	#print trainData[0]
	#print len(trainData[0])
	data = np.asarray(trainData)
	#print data[0]
	#print data.shape

	cols = data.shape[1]
	rows = data.shape[0]

	#remove payer code column
	data = np.delete(data, 10, 1)
	
	#remove weight column
	#print set(data[:, 5])
	#sys.exit()
	data = np.delete(data, 5, 1)
	
	#check medical specialty
	#print set(data[:, 9])
	#sys.exit()
	#Let '?' simply stay as another attribute 

	#print data.shape
	#sys.exit()

	#check unique patient ids
	uniquepatientids = (set(data[:, 1]))
	uniquepatientids = list(uniquepatientids)
	#print len(uniquepatientids)

	tobedeleted = []
	for rowidx in range(0, rows):
		if rowidx%10000==0:
			print rowidx
		thisrow = data[rowidx, :]
		patientid = thisrow[1]
		#patientid = 
		#print type(patientid)
		#print type(uniquepatientids)
		#sys.exit()
		#print rowidx
		#print patientid
		#sys.exit()
		if patientid in uniquepatientids:
			uniquepatientids.remove(patientid)
		else:
			#data = np.delete(data, rowidx, 0)
			tobedeleted.append(rowidx)

		#sys.exit()

	print len(tobedeleted)
	#sys.exit()
	data = np.delete(data, tobedeleted, 0)
	print data.shape
	
	pickle.dump(data, open(os.path.join(dataDir, "preprocessed1-4data"), "wb"))
	print "done"
	sys.exit()"""

	"""for i in range(2, cols):
		col = data[:,i]
		#print col.shape
		#sys.exit()
		print set(col)
		sys.exit()

	sys.exit()"""
	#print trainData.shape
	
	#rows = trainData.shape[0]
	#cols = trainData.shape[1]

	#X = trainData[:, 0:cols-1]
	#Y = trainData[:, cols-1]

	#print trainX.shape
	#print trainY.shape

	"""processeddata = pickle.load(open(os.path.join(dataDir, "preprocessed1-4data"), "rb"))
	rows, cols = processeddata.shape
	Xprocessed = processeddata[:, 0:cols-1]
	Yprocessed = processeddata[:, cols-1]

	print set(Yprocessed)
	print np.ndarray.tolist(Yprocessed).count('NO')/float(rows)
	print np.ndarray.tolist(Yprocessed).count('<30')/float(rows)
	print np.ndarray.tolist(Yprocessed).count('>30')/float(rows)
	
	X_train, X_test, y_train, y_test = train_test_split(
		Xprocessed, Yprocessed, test_size=0.2, random_state=49)

	print type(X_train)
	print type(y_train)

	rows = len(np.ndarray.tolist(y_train))
	print np.ndarray.tolist(y_train).count('NO')/float(rows)
	print np.ndarray.tolist(y_train).count('<30')/float(rows)
	print np.ndarray.tolist(y_train).count('>30')/float(rows)

	#return 0


	pickle.dump(((X_train, y_train),(X_test, y_test)),open("traintestsplit", "wb"))"""

	#dataset = pickle.load(open("traintestsplit", "rb")
	#outfile = TemporaryFile()

	return 0
	#return X, Y

def readfile():
	#filepath = os.path.join(dataDir, "diabetic_data.csv")
	#data = readData(filepath)

	#print type(data)
	print "hello"



def main():
	#readfile()

	dataset = pickle.load(open("traintestsplit", "rb"))
	print type(dataset)

if __name__ == '__main__':
	main()