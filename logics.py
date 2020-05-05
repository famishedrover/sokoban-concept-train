import numpy as np


def box_above(state):
	# assumes room state

	# returns true if box is above...

	player_idx = np.argwhere(state == 5)[0]
	box_idx = np.argwhere(state == 4)[0]

	# print (player_idx)
	# print (box_idx)

	py,px = player_idx
	by,bx = box_idx

	if (bx == px) and (by+1 == py) :
		# print (True)
		return True
	else :
		# print (False)
		return False




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