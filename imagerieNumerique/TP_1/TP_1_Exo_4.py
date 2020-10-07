import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski

lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)

# for us row = col
row = lena.shape[0]
col = lena.shape[1]

mu = 0
sigma = [1, 25, 50]
listeGauss = []
for i in range(0, len(sigma)):
    gauss = np.random.normal(mu, sigma[i], (row, col, 1)).astype(np.float32)
    gaussian = np.concatenate((gauss, gauss, gauss), axis=2)
    listeGauss.append(gauss + lena)

rows = 1
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(listeGauss[a], cmap='gray')
    # plt.legend(labelImagesDone[a])
fig.tight_layout()
plt.show()
### marche pas 