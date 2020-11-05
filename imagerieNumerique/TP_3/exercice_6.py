'''
TP3 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 6
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy
import numpy as np
import skimage.color as ski
import skimage.transform as transform
from math import log10, sqrt
import scipy.ndimage as spy


# (a)


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
noisy = plt.imread("noisy.bmp")

# rR, rG, rB = transformImageSplit(reference)
# print("stf")
# nR, nG, nB = transformImageSplit(noisy)
# allImages = [reference, rR, rG, rB, noisy, nR, nG, nB]
# for i in range(0, len(allImages)):
#     allImages[i] = ski.rgb2gray(allImages[i])
#
# mse = []
# psnr = []
# for i in range(0, int(len(allImages) / 2)):
#     mse.append(np.mean((allImages[i] - allImages[i + 4]) ** 2))
#     maxPixel = 255.0
#     psnr.append(20 * log10(maxPixel / sqrt(mse[i])))
#
# print(mse)
# print(psnr)
#
# '''
#
# all in grayscale:
#
#     ORIGINAL                  RED                 GREEN                  BLUE
# [0.01400454892523029, 2.992768566451479e-17, 1.8399993849718415e-16, 6.900877226524659e-18]
# [66.668112357439,     213.37007227121347,    205.48262683023253,     219.74176059924332]
#
# '''
#
# allLabels = ["original", "red", "green", "blue", "noisy", "noisy Red", "noisy Green", "noisy Blue"]
# rows = 2
# cols = 4
# axes = []
# fig = plt.figure()
#
# for a in range(rows * cols):
#     axes.append(fig.add_subplot(rows, cols, a + 1))
#     plt.imshow(allImages[a], cmap='gray')
#     plt.title(allLabels[a])
# plt.show()

# (b)
print((213.37007227121347 + 205.48262683023253 + 219.74176059924332) / 3, " psnr avg")
x = noisy
y = transform.downscale_local_mean(transform.downscale_local_mean(x, (2, 2, 1)), (2, 2, 1))
print("ALLLL")
z = spy.zoom(spy.zoom(y, (2.0, 2.0, 1.0), order=0), (2.0, 2.0, 1.0), order=0)
print(" ALLLLL 2 ")

mseXR = np.mean((reference - x) ** 2)
maxPixel = 255.0
psnrXR = 20 * log10(maxPixel / sqrt(mseXR))

mseZR = np.mean((reference - z) ** 2)
maxPixel = 255.0
psnrZR = 20 * log10(maxPixel / sqrt(mseZR))
print(" mse X : ", mseXR, " || mse Z : ", mseZR)
print(" psnr X : ", psnrXR, " || psnr Z : ", psnrZR)
print(z.shape)
print(x[0][0])
print(z[0][0])
allImages = [reference, x, z]
rows = 1
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(allImages[a])
plt.show()
