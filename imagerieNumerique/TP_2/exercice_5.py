'''
TP2 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 5
'''
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.metrics as metric
import skimage
import copy


def rgb_2_cmy(red, green, blue):
    cyan = 1 - red / 255
    magenta = 1 - green / 255
    yellow = 1 - blue / 255
    return cyan, magenta, yellow


def cmy_2_rgb(cyan, magenta, yellow):
    red = (1 - cyan) * 255
    green = (1 - magenta) * 255
    blue = (1 - yellow) * 255
    return red, green, blue


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


def transformImageMerge(channel1, channel2, channel3):
    mergedImage = np.zeros(channel1.shape, dtype=int)
    for i in range(0, mergedImage.shape[0]):
        for j in range(0, mergedImage.shape[1]):
            mergedImage[i][j][0] = channel1[i][j][0]
            mergedImage[i][j][1] = channel2[i][j][1]
            mergedImage[i][j][2] = channel3[i][j][2]
    return mergedImage


mnmsRGB = mpimg.imread("mnms_512.jpg")  # good

######                            B                            ######
[R, G, B] = transformImageSplit(mnmsRGB)
C, M, Y = rgb_2_cmy(R, G, B)
labels = ["channel C", "channel M", "channel Y"]
grayC = ski.rgb2gray(C)
grayM = ski.rgb2gray(M)
grayY = ski.rgb2gray(Y)
imagesDone = [grayC, grayM, grayY]
rows = 1
cols = 3
axes = []
fig = plt.figure()
for i in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, i + 1))
    plt.imshow(imagesDone[i], cmap='gray')
    plt.title(labels[i])
fig.tight_layout()
plt.show()

######                            C                            ######

mnmsCMY = transformImageMerge(C, M, Y)
mnmsRGBAgainSplit = cmy_2_rgb(C, M, Y)
mnmsRGBAgain = transformImageMerge(mnmsRGBAgainSplit[0], mnmsRGBAgainSplit[1], mnmsRGBAgainSplit[2])
img = [mnmsRGB, mnmsRGBAgain]
msePython = metric.mean_squared_error(mnmsRGB, mnmsRGBAgain)
labels = ["original", "hand made reconversion to RGB, MSE : " + str(msePython)]

rows = 1
cols = 2
axes = []
fig = plt.figure()
for i in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, i + 1))
    plt.imshow(img[i])
    plt.title(labels[i])
fig.tight_layout()
plt.show()
