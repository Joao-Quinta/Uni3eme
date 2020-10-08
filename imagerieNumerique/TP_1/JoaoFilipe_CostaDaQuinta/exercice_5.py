'''
TP1 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 5
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.util as util
import skimage.metrics as metric

# load the image and turn it to grayscale
lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)

# for us row = col
row = grayscale.shape[0]
col = grayscale.shape[1]

# centralized normal distribution with the different sigma values
density = [0.0013, 0.031, 0.113]
listeImages = []
listLabels = []

for i in range(0, len(density)):
    # we creat the noisy image using the function random_noise with the different densities
    noiseD = util.random_noise(grayscale, mode='s&p', amount=density[i])
    # we calculate the mse value for each calculated "noised" image, comparing it with grayscale image
    mse = metric.mean_squared_error(grayscale, noiseD)
    listeImages.append(noiseD)
    listLabels.append([str(density[i]), str(mse)])

rows = 1
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(listeImages[a], cmap='gray')
    plt.title(' Density: ' + listLabels[a][0] + ' ||  MSE: ' + listLabels[a][1])
    # plt.legend(labelImagesDone[a])
fig.tight_layout()
plt.show()
