from PIL import Image
import numpy as np
import os 

from constt import *


def save_img(img, path):
	im = Image.fromarray(img)
	im.save(path)


def read_img(path):
	im = np.array(Image.open(path))
	return im 


def createDirs(allConceptsFuncs, ROOT="runs"):

	if not os.path.exists(ROOT):
		os.mkdir(ROOT)
		print("Directory " , ROOT ,  " Created ")

	for concept in allConceptsFuncs: 

		dirsCreate = [ROOT, ROOT+"/"+concept, ROOT+"/"+concept+"/pos", ROOT+"/"+concept+"/neg"]
		for dirName in dirsCreate :
			if not os.path.exists(dirName):
				os.mkdir(dirName)
				print("Directory " , dirName ,  " Created ")


def findAllConcepts():
	import logics 
	allConceptsFuncs = []
	for x in dir(logics) :
		if "concept" in x :
			allConceptsFuncs.append(x)
	print ("All Concepts Found :", allConceptsFuncs)

	return allConceptsFuncs