'''
TP3 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 4
'''

import matplotlib.pyplot as plt
import numpy as np
import skimage.color as ski

# (a)

n = 100
m = 512
linearSp = np.linspace(0, 255, m)
# separates the interval 0 to 255 in m elements
gradient = np.tile(linearSp, (n, 1))  # this is our gradient with k = 8
# repeats linear space computed before a number of times => max(n,1)
# it is of size -> max(n,1) lines and m columns

images = [gradient]
labels = ['8']
for i in [7, 5, 3, 2, 1]:
    quantization = 2 ** i
    step = 256 / (quantization - 1)
    quantizedImage = np.floor((gradient / step) + 0.5)
    images.append(quantizedImage)
    labels.append(str(i))

rows = 2
cols = 3
axes = []
fig = plt.figure()
for i in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, i + 1))
    plt.imshow(images[i], cmap='gray')
    plt.title(labels[i] + '-bits')
fig.tight_layout()
plt.show()

# (b)

imageLena = plt.imread('lena.png')
grayIm=ski.rgb2gray(imageLena)*256

images = [grayIm]
labels = ['8']
for i in [7, 5, 3, 2, 1]:
    quantization = 2 ** i
    step = 256 / (quantization - 1)
    quantizedImage = np.floor((grayIm / step) + 0.5)
    images.append(quantizedImage)
    labels.append(str(i))

rows = 2
cols = 3
axes = []
fig = plt.figure()
for i in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, i + 1))
    plt.imshow(images[i], cmap='gray')
    plt.title(labels[i] + '-bits')
fig.tight_layout()
plt.show()
