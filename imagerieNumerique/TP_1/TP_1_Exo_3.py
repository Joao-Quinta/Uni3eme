import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski

lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)
plt.imshow(grayscale)
plt.show()