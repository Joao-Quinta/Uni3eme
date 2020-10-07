import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy


def transformImage(images):
    for j in range(0, len(images[0])):
        for z in range(0, len(images[0][j])):
            for t in range(0, len(images)):
                for i in range(0, len(images[0][j][z])):
                    if i != t:
                        images[t][j][z][i] = 0
    return images


lenaRGB = mpimg.imread("lena.png")
lenaR = copy.deepcopy(lenaRGB)
lenaG = copy.deepcopy(lenaRGB)
lenaB = copy.deepcopy(lenaRGB)
[lenaR, lenaG, lenaB] = transformImage([lenaR, lenaG, lenaB])

fig, axes = plt.subplots(nrows=2, ncols=2)
plt.show()