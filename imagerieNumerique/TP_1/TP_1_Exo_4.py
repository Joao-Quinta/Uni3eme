import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage.util as util

# load the image and turn it to grayscale
lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)

# for us row = col
row = grayscale.shape[0]
col = grayscale.shape[1]

# centralized normal distribution with the different sigma values
mu = 0
sigma = [0.01, 0.09, 0.19]
listeGauss = []
listLabels = []

################################## (A) ##################################
for i in range(0, len(sigma)):
    # we create the matrices from random distributions
    gauss = np.random.normal(mu, sigma[i], (row, col))
    # we add the noise to the hrayscale image and put it in the list that will have the images
    listeGauss.append(gauss + grayscale)
    listLabels.append(str(sigma[i]))

################################## (B) ##################################
for i in range(0, len(sigma)):
    # we creat the noisy image using the function random_noise
    noiseB = util.random_noise(grayscale, var=sigma[i] ** 2, clip=True)
    listeGauss.append(noiseB)
    listLabels.append(str(sigma[i]))

ab = ['(a)', '(a)', '(a)', '(b)', '(b)', '(b)']
rows = 2
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(listeGauss[a], cmap='gray')
    plt.title(ab[a] + "  sigma=" + listLabels[a])
    # plt.legend(labelImagesDone[a])
fig.tight_layout()
plt.show()
