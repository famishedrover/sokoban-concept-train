from PIL import Image
import numpy as np

from constt import *


def save_img(img, path):
	im = Image.fromarray(img)
	im.save(path)


def read_img(path):
	im = np.array(Image.open(path))
	return im 
