import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.util as util
from scipy import ndimage

# load the image and turn it to grayscale
lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)

grayscaleMean = np.mean(grayscale)
grayscaleVariance = np.var(grayscale)

grayscaleMeans = ndimage.mean(grayscale)
grayscaleVariances = ndimage.variance(grayscale)

print(grayscaleMean, grayscaleVariance)
print(grayscaleMeans, grayscaleVariances)
