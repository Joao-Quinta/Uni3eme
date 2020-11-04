'''
TP3 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 3
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy
import numpy as np

# we start by sampling the interval -5,5
sampling = 0.1
valuesXY = np.arange(-5, 5, sampling)
axeX, axeY = np.meshgrid(valuesXY, valuesXY)
# axeX is a matrix NxN where each line is valuesXY
# axeY is a matrix NxN where each column is valuesXY
axeZ = np.sin(axeX) + np.cos(axeY)

# now we need to quantize
quantize = 10
step = (2 - (-2)) / (quantize - 1)

axeZQuantized = np.floor((axeZ / step) + 0.5)
# print(axeX)
# print(axeY)
# print(axeZ)

fig = plt.figure()
ax = fig.gca(projection='3d')
surface = ax.plot_surface(axeX, axeY, axeZQuantized, linewidth=0, antialiased=False)
fig.colorbar(surface, shrink=0.5, aspect=5)
ax.set_title('Surface plot || quantize : ' + str(quantize) + ' || sample : ' + str(sampling))
plt.show()
