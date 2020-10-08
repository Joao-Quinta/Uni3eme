'''
TP1 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 3
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage

# load the image and turn it to grayscale
lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)

################################## (A) ##################################
cropped_imageA = skimage.util.crop(grayscale, ((100, 116), (150, 121)), copy=False)

################################## (B) ##################################
cropped_imageB = grayscale[100:380, 150:375]

imagesDone = [grayscale, cropped_imageA, cropped_imageB]
labelImagesDone = ["grayscale Original", "method: a", "method: b"]
rows = 1
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(imagesDone[a], cmap='gray')
    plt.title(labelImagesDone[a])
fig.tight_layout()
plt.show()
