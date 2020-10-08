import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy
import numpy as np


# to creat the images with the different accents
def transformImage(images):
    for j in range(0, len(images[0])):
        for z in range(0, len(images[0][j])):
            for t in range(0, len(images)):
                for i in range(0, len(images[0][j][z])):
                    if i != t:
                        images[t][j][z][i] = 0
    return images


# load lena, copy it to the different colors, and call the function
lenaRGB = mpimg.imread("lena.png")
lenaR = copy.deepcopy(lenaRGB)
lenaG = copy.deepcopy(lenaRGB)
lenaB = copy.deepcopy(lenaRGB)
imagesDone = transformImage([lenaR, lenaG, lenaB])
imagesDone.insert(0, lenaRGB)

labelImagesDone = ['original', 'Red accent', 'Green accent', 'Blue accent']
rows = 2
cols = 2
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(imagesDone[a])
    plt.title(labelImagesDone[a])
fig.tight_layout()
plt.show()
