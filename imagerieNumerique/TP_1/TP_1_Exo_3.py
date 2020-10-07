import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage

lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)
# plt.imshow(grayscale, cmap='gray')
# plt.show()


cropped_image = skimage.util.crop(grayscale, ((100, 116), (150, 121)), copy=False)
plt.imshow(cropped_image, cmap='gray')
plt.show()
