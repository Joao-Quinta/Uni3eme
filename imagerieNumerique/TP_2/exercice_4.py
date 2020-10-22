'''
TP2 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 4
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.metrics as metric
import skimage
import copy


def rgb_2_yuv(rgb):
    matrixConv = np.array([[0.299, 0.587, 0.114], [-0.14713, -0.28886, 0.436], [0.615, -0.51499, -0.10001]])
    yuv = np.dot(rgb, matrixConv.T) / 255
    return yuv


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
mnmsYUVL = rgb_2_yuv(mnmsRGB)
imagesDone = transformImage(mnmsYUVL)
labels = ["channel Y", "channel U", "channel V"]
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
mnmsYUVA = ski.rgb2ycbcr(mnmsRGB)/255

mnmsAgainRGB = ski.ycbcr2rgb(mnmsYUVA*255)
img = [mnmsRGB, mnmsYUVL, mnmsYUVA, mnmsAgainRGB]
msePython = metric.mean_squared_error(mnmsRGB, mnmsAgainRGB)
labels = ["original", "hand made conversion", "python function ycbcr2rgb",
          "python reconversion to RGB, MSE : " + str(msePython)]

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
