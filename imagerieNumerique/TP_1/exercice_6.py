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

#the variace and mean
grayscaleMean = np.mean(grayscale)
grayscaleVariance = np.var(grayscale)

print('the mean for the original grayscale image is : ',grayscaleMean,' and variance is : ', grayscaleVariance)

step = [1, 2, 3]
grayscaleWindow = []
for i in range(0, len(step)):
    grayscaleWindow = util.shape.view_as_windows(grayscale, 5, step=step[i])
    print('for step = ', step[i], ' the Mean is : ', np.mean(grayscaleWindow), ' and the var is : ',
          np.var(grayscaleWindow))
