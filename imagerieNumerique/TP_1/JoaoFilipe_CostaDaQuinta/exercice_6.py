'''
TP1 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 6
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.util as util

# load the image and turn it to grayscale
lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)

# the variace and mean
grayscaleMean = np.mean(grayscale)
grayscaleVariance = np.var(grayscale)

print('the mean for the original grayscale image is : ', grayscaleMean, ' and variance is : ', grayscaleVariance)

step = [1, 3]
grayscaleWindowResult = []
label = []
for i in range(0, len(step)):
    grayscaleWindow = util.shape.view_as_windows(grayscale, (5, 5), step=step[i])

    meanC = np.zeros((grayscaleWindow.shape[0], grayscaleWindow.shape[1]))
    varC = np.zeros((grayscaleWindow.shape[0], grayscaleWindow.shape[1]))

    for j in range(0, grayscaleWindow.shape[0]):
        for t in range(0, grayscaleWindow.shape[1]):
            meanC[j][t] = np.mean(grayscaleWindow[j][t])
            varC[j][t] = np.var(grayscaleWindow[j][t])

    grayscaleWindowResult.append(meanC)
    label.append(str(step[i]))
    grayscaleWindowResult.append(varC)
    label.append(str(step[i]))

meanVar = ['mean', 'variance', 'mean', 'variance']
rows = 2
cols = 2
axes = []
fig = plt.figure()
for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(grayscaleWindowResult[a], cmap='gray')
    plt.title(meanVar[a] + "  step =" + label[a])
    # plt.legend(labelImagesDone[a])
fig.tight_layout()
plt.show()
