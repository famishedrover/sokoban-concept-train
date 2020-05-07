import numpy as np

import os

# you can define a new concept function -- just remember to name is as concept_*


# x increases to right 
# y increases to down 

def concept_box_above(state):
	# assumes room state

	# returns true if box is above...

	try : 

		player_idx = np.argwhere(state == 5)[0]

		try : 
			box_idx = np.argwhere(state == 4)[0]
		except : 
			box_idx = np.argwhere(state == 3)[0]

		# print (player_idx)
		# print (box_idx)

		py,px = player_idx
		by,bx = box_idx

		if (bx == px) and (by+1 == py) :
			return True
		else :
			return False
	except : 
		print (state)



def concept_box_below(state):
	# assumes room state

	player_idx = np.argwhere(state == 5)[0]
	try : 
		box_idx = np.argwhere(state == 4)[0]
	except : 
		box_idx = np.argwhere(state == 3)[0]

	py,px = player_idx
	by,bx = box_idx

	if (bx == px) and (by-1 == py) :
		return True
	else :
		return False


def concept_switch_on(state):
	# 7 when off, 8 on
	# not present when box on it.

	# assume : when box on switch -- 'its on!'

	status = True 
	switch_state = np.argwhere(state == 8)
	if len(switch_state) == 0 :
		status = False

	return status



















def getMask(state):
	player_idx = np.argwhere(state == 5)[0]
	pmask = np.zeros_like(state)
	pmask[player_idx[0], player_idx[1]] = 1 

	bmask = np.zeros_like(state)

	try : 
		box_idx = np.argwhere(state == 4)[0]
	except : 
		box_idx = np.argwhere(state == 3)[0]

	bmask[box_idx[0], box_idx[1]] = 1 

	return pmask, bmask 

def updateMask(state, pmask, bmask):
	player_idx = np.argwhere(state == 5)[0]

	try : 
		box_idx = np.argwhere(state == 4)[0]
	except : 
		box_idx = np.argwhere(state == 3)[0]


	pmask[player_idx[0], player_idx[1]] += 1
	bmask[box_idx[0], box_idx[1]] += 1 

	return pmask, bmask

# def concept_box_left(state):
# 	print ("working")
# 	return True

# def concept_box_right(state):
# 	print ("working")
# 	return True


# we can do class stuff - but is it worth it? since like 3 concepts --- 


# class Logic:
# 	def __init__(self, name="box_above"):
# 		self.name = name

# 	def run(self, state):
# 		pass





# class Box_Above(Logic):
# 	def run(self, state):

	



# def sample(a):
# 	print (a*2)

# eval("sample")(2)