import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.util as util

# load the image and turn it to grayscale
lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)