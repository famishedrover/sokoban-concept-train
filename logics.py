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
	