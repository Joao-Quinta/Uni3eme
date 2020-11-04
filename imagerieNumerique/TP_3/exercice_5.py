'''
TP3 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 5
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy
import numpy as np
import skimage.color as ski


def transformImageSplit(image):
    c = np.zeros(image.shape, dtype=int)
    m = np.zeros(image.shape, dtype=int)
    y = np.zeros(image.shape, dtype=int)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            c[i][j][0] = image[i][j][0]
            m[i][j][1] = image[i][j][1]
            y[i][j][2] = image[i][j][2]
    return c, m, y


reference = plt.imread("reference.bmp")
rR, rG, rB = transformImageSplit(reference)
print("stf")
noisy = plt.imread("noisy.bmp")
nR, nG, nB = transformImageSplit(noisy)
print("sssss")
allImages = [reference, rR, rG, rB, noisy, nR, nG, nB]
for i in range(0,len(allImages)):
    allImages[i] = ski.rgb2gray(allImages[i])

allLabels = ["original", "red", "green", "blue", "noisy", "noisy Red", "noisy Green", "noisy Blue"]
rows = 2
cols = 4
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(allImages[a], cmap='gray')
    plt.title(allLabels[a])
plt.show()

