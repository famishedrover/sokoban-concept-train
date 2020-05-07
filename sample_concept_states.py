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


import utils
import logics

import os

import pprint 




#from scipy.misc import imresize # preserves single-pixel info _unlike_ img = img[::2,::2]
# 
# --- Find all concepts
allConceptsFuncs = utils.findAllConcepts()

# resfunc = getattr(logics, 'concept_box_below')

utils.createDirs(allConceptsFuncs,ROOT="runs")


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







# since neg are ALOT we can take only 10% of those....


def randomStartAgent(env, STEP_LIMIT=20):
	# 

	steps = random.randint(0, STEP_LIMIT)
	# read the prioritydqn agent for this map & run according to its policy 
	for step in steps :
		# state = env.room_state
		state = env.render(mode="rgb_array")
		action = RLAgentPolicy(state)
		env.step(action)

	return env  



def sample_states(env, eps, iters, randomStart=False):
	logger = {}
	# idx 0 is pos, idx 1 is neg, idx 2 is ACTUTAL_NEG
	POSIDX = 0
	NEGIDX = 1
	AC_NEGIDX = 2
	for concept in allConceptsFuncs : 
		logger[concept] = [0,0,0]

	for ep in range(eps):

		print ("ep",ep, "Count pos/neg/actualneg")
		pprint.pprint(logger)


		if randomStart :
			env = randomStartAgent(env, STEP_LIMIT=20)

		for i in range(iters):
			action = random.randint(0,8) 

			
			done = True
			env.step(action)
			img = env.render(mode="rgb_array")

			state = env.room_state


			for concept in allConceptsFuncs :
				func = getattr(logics, concept)

				if (func(state)):
					path = "runs/"+concept+"/pos"
					path += "/"+ str(logger[concept][POSIDX])+".png"
					# save for pos

					utils.save_img(img, path)
					logger[concept][POSIDX] += 1

				else :
					logger[concept][AC_NEGIDX]+=1
					# save for neg
					# select only 10% of these...
					if random.random() > 0.1 : 
						continue

					path = "runs/"+concept+"/neg"
					path += "/"+ str(logger[concept][NEGIDX])+".png"

					utils.save_img(img, path)
					logger[concept][NEGIDX] += 1



sample_states(env, eps=100, iters=100, randomStart=False)
















