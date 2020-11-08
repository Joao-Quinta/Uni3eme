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
import skimage.metrics as metrics


# PSNR FUNCTION
def psnr(image1, image2):
    mse = metrics.mean_squared_error(image1, image2)
    if mse == 0:
        return 100
    maxSize = 255.0
    return 10 * log10((maxSize ** 2) / mse)


# (a)
reference = plt.imread("reference.bmp")
noisy = plt.imread("noisy.bmp")

rR, rG, rB = reference[:, :, 0], reference[:, :, 1], reference[:, :, 2]
nR, nG, nB = noisy[:, :, 0], noisy[:, :, 1], noisy[:, :, 2]
allImages = [reference, rR, rG, rB, noisy, nR, nG, nB]
allImagesGray = []
for i in range(0, len(allImages)):
    allImagesGray.append(ski.rgb2gray(allImages[i]))

psnrL = []
for i in range(0, int(len(allImagesGray) / 2)):
    psnrL.append(psnr(allImagesGray[i], allImagesGray[i + 4]))
avgPSNR = 0
for i in range(1, len(psnrL)):
    avgPSNR = avgPSNR + psnrL[i]
avgPSNR = avgPSNR / 3
print("the avg PSNR in exercice A is : ", avgPSNR, " dB")

allLabels = ["original", "red", "green", "blue", "noisy - PSNR : " + str(psnrL[0]),
             "noisy Red - PSNR : " + str(psnrL[1]), "noisy Green - PSNR : " + str(psnrL[2]),
             "noisy Blue - PSNR : " + str(psnrL[3])]
rows = 2
cols = 4
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(allImagesGray[a], cmap='gray')
    plt.title(allLabels[a])
plt.show()

# (b)
real = [allImages[1], allImages[2], allImages[3]]
x = [allImages[5], allImages[6], allImages[7]]
y = []
z = []
for i in range(0, len(x)):
    y.append(transform.downscale_local_mean(transform.downscale_local_mean(x[i], (2, 2)), (2, 2)))
    z.append(spy.zoom(spy.zoom(y[i], (2.0, 2.0), order=0), (2.0, 2.0), order=0))

psnrLL = []
for i in range(0, len(real)):
    psnrLL.append(psnr(real[i], z[i]))

avgPSNRB = 0
for i in range(0, len(psnrLL)):
    avgPSNRB = avgPSNRB + psnrLL[i]

avgPSNRB = avgPSNRB / 3
print("the avg PSNR in exercice B is : ", avgPSNRB, " dB")
# (c)
realGray = [allImagesGray[0]]
xGray = [allImagesGray[4]]
yGray = []
zGray = []
for i in range(0, len(xGray)):
    yGray.append(transform.downscale_local_mean(transform.downscale_local_mean(xGray[i], (2, 2)), (2, 2)))
    zGray.append(spy.zoom(spy.zoom(yGray[i], (2.0, 2.0), order=0), (2.0, 2.0), order=0))

psnrLLL = []
for i in range(0, len(realGray)):
    psnrLLL.append(psnr(realGray[i], zGray[i]))
print("the PSNR in exercice C is : ", psnrLLL[0], " dB")
