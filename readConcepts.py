import os 
import utils

import random


from constt import *




def getPaths(path):
	paths = []
	for i,j,k in os.walk(path):
		for im in k : 
			paths.append("/".join([path,im]))
	return paths


import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import numpy as np
# from skimage import io, transform


class ConceptData(Dataset):

	def __init__(self, CONCEPT_NAME, transform=None, neg_limit=100, seed=1):

		pospath = "runs/"+CONCEPT_NAME+"/pos"
		negpath = "runs/"+CONCEPT_NAME+"/neg"

		self.pospaths = getPaths(pospath)
		self.negpaths_full = getPaths(negpath)
		neg_limit = min(neg_limit, len(self.negpaths_full))

		self.negpaths = random.sample(self.negpaths_full, neg_limit)


		self.labels = np.hstack((   np.ones(len(self.pospaths)),  np.zeros(len(self.negpaths))  ))
		
		self.allpaths = self.pospaths + self.negpaths

		


		self.transform = transform

	def __len__(self):
		return len(self.allpaths)

	def __getitem__(self, idx):
		if torch.is_tensor(idx):
			idx = idx.tolist()

		img_name = self.allpaths[idx]
		image = utils.read_img(img_name)
		label = self.labels[idx]

		if self.transform:
			image = self.transform(image)

		return  (image, label)




# data = ConceptData("box_above", None)


# for ix in data :
	# print (ix[1])