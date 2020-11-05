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
import skimage.metrics as metrics
import skimage.util as util
from math import log10


# PSNR FUNCTION
def psnr(image1, image2):
    mse = metrics.mean_squared_error(image1, image2)
    if mse == 0:
        return 100
    maxSize = 255.0
    return 10 * log10((maxSize ** 2) / mse)


# load LENA
imageLena = plt.imread('lena.png')
grayLena = ski.rgb2gray(imageLena)
images = [grayLena]
psnrAll = []
for j in [10]:
    # (a)
    # we need to create the 10 noisy images, deviation 25
    imagesNoisy = []
    for i in range(j):
        # we use util.random_noise function
        noisyGrayLena = util.random_noise(grayLena, var=(25 / 255) ** 2)
        imagesNoisy.append(noisyGrayLena)

    # (b)
    # we calculate avc PSNR using the function we created earlier
    totalPsnr = 0
    for i in range(0, len(imagesNoisy)):
        totalPsnr = totalPsnr + psnr(grayLena, imagesNoisy[i])

    avgPsnr = totalPsnr / len(imagesNoisy)
    print(j, " : avg PSNR : ", avgPsnr)

    # (c)
    # we now need to denoise every image with frame averaging approach
    # what we will do is to average the value of each pixel from the 10 noised images
    totalImage = np.zeros(grayLena.shape)
    for i in range(0, len(imagesNoisy)):
        totalImage = totalImage + imagesNoisy[i]

    avgImage = totalImage / len(imagesNoisy)

    # (d)
    # we now need to compute psnr between the denoised image and the original
    newPsnr = psnr(avgImage, grayLena)
    psnrAll.append(newPsnr)
    print(j, " : PSNR after denoise : ", newPsnr)
    images.append(avgImage)

labels = ["Original image", "n = 10 noisy images || PSNR : " + str(psnrAll[0])]
rows = 1
cols = 2
axes = []
fig = plt.figure()
for i in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, i + 1))
    plt.imshow(images[i], cmap='gray')
    plt.title(labels[i])
fig.tight_layout()
plt.show()
