import random
# from typing import List, Tuple

import gym
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.autograd as autograd 
import torch.optim as optim

import gym_sokoban_mod

from constt import *

#from scipy.misc import imresize # preserves single-pixel info _unlike_ img = img[::2,::2]



import os
dirsCreate = ["runs", "runs/"+CONCEPT_NAME, "runs/"+CONCEPT_NAME+"/pos", "runs/"+CONCEPT_NAME+"/neg"]
for dirName in dirsCreate :
	if not os.path.exists(dirName):
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ")


ACTION_LOOKUP = {
0: "no operation",
1: "push up",
2: "push down",
3: "push left",
4: "push right",
5: "move up",
6: "move down",
7: "move left",
8: "move right",
}



env_name = 'Sokoban-mod-v0'
env = gym.make(env_name) ; 



env.seed(seed)
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)


# ------- CODE STARTS HERE -----


import utils
import logics



# since neg are ALOT we can take only 10% of those....


def sample_states(eps, iters):
	pos = 0
	neg = 0
	ac_neg = 0 

	for ep in range(eps):
		for i in range(iters):
			print ("ep",ep,"iteration", i, "Count pos -- neg/actualneg", pos,"--", neg,"/", ac_neg)

			
			action = random.randint(0,8) 

			
			done = True
			env.step(action)
			img = env.render(mode="rgb_array")


			if (logics.box_above(env.room_state)):
				path = "runs/"+CONCEPT_NAME+"/pos"
				path += "/"+ str(pos)+".png"
				# save for pos

				utils.save_img(img, path)
				pos += 1

			else :
				ac_neg+=1
				# save for neg
				# select only 10% of these...
				if random.random() > 0.1 : 
					continue

				path = "runs/"+CONCEPT_NAME+"/neg"
				path += "/"+ str(neg)+".png"

				utils.save_img(img, path)
				neg += 1



sample_states(eps=100, iters=100)















