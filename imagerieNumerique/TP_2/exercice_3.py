'''
TP2 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 3
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.metrics as metric
import skimage
import copy


def rgb_2_yiq(rgb):
    matrixConv = np.array([[0.299, 0.587, 0.114], [0.596, -0.274, -0.322], [0.211, -0.523, 0.312]])
    yiq = np.dot(rgb, matrixConv.T) / 255
    return yiq


def transformImage(image):
    mnmsYL = np.zeros(image.shape, dtype=int)
    mnmsIL = np.zeros(image.shape, dtype=int)
    mnmsQL = np.zeros(image.shape, dtype=int)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            mnmsYL[i][j][0] = image[i][j][0] * 255
            mnmsIL[i][j][1] = image[i][j][1] * 255
            mnmsQL[i][j][2] = image[i][j][2] * 255
    return [mnmsYL, mnmsIL, mnmsQL]


mnmsRGB = mpimg.imread("mnms_512.jpg")
######                            B                            ######
mnmsYIQL = rgb_2_yiq(mnmsRGB)
imagesDone = transformImage(mnmsYIQL)
labels = ["channel Y", "channel I", "channel Q"]
for i in range(0, len(imagesDone)):
    imagesDone[i] = ski.rgb2gray(imagesDone[i])
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
mnmsYIQA = ski.rgb2yiq(mnmsRGB)


mnmsAgainRGB = ski.yiq2rgb(mnmsYIQA)
img = [mnmsRGB, mnmsYIQL, mnmsYIQA, mnmsAgainRGB]
msePython = metric.mean_squared_error(mnmsRGB, mnmsAgainRGB)

labels = ["original", "hand made conversion", "python function rgb2yiq", "python reconversion to RGB, MSE : " + str(msePython)]

rows = 1
cols = 4
axes = []
fig = plt.figure()
for i in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, i + 1))
    plt.imshow(img[i])
    plt.title(labels[i])
fig.tight_layout()
plt.show()


