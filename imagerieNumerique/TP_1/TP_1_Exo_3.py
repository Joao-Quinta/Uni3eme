import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage.color as ski
import skimage

lena = mpimg.imread("lena.png")
grayscale = ski.rgb2gray(lena)
# plt.imshow(grayscale, cmap='gray')
# plt.show()


cropped_imageA = skimage.util.crop(grayscale, ((100, 116), (150, 121)), copy=False)
# plt.imshow(cropped_imageA, cmap='gray')
# plt.show()
cropped_imageB = grayscale[100:380,150:375]

# plt.imshow(cropped_imageB, cmap='gray')
# plt.show()

imagesDone = [grayscale,cropped_imageA,cropped_imageB]
labelImagesDone = ["grayscale","(a)","(b)"]
rows = 1
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(imagesDone[a], cmap='gray')
    #plt.legend(labelImagesDone[a])
fig.tight_layout()
plt.show()