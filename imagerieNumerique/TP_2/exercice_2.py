'''
TP2 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 2
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy
import numpy as np


def transformImage(image, indice):
    images = []
    for nb in range(0, 11):
        imageIt = copy.deepcopy(image)
        for i in range(0, len(image)):
            for j in range(0, len(image[i])):
                imageIt[i][j][indice] = nb * 0.1 * image[i][j][indice]
        images.append(imageIt)

    return images


# load lena, copy it to the different colors, and call the function
mnms = mpimg.imread("mnms_512.jpg")
mnmsR = transformImage(mnms, 0)
mnmsG = transformImage(mnms, 1)
mnmsB = transformImage(mnms, 2)
imagess = [mnmsR, mnmsG, mnmsB]

labelImagesDone = ['*0', '*0.1', '*0.2', '*0.3', '*0.4', '*0.5', '*0.6', '*0.7', '*0.8', '*0.9', '*1']
labelColors = ['RED -> ', 'GREEN -> ', 'BLUE -> ']
allLabels = []
allImages = []
for i in range(0, len(labelColors)):
    for j in range(0, len(labelImagesDone)):
        allLabels.append(labelColors[i] + labelImagesDone[j])
        allImages.append(imagess[i][j])

rows = 3
cols = 11
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(allImages[a])
    plt.title(allLabels[a])
plt.show()
