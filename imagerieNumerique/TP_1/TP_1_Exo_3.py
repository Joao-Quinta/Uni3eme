import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


x = np.linspace(0, 1, 100)

image = np.tile(x, (25, 1)).T
print(image)
print(len(image))
print(len(image[0]))
print(image[0][0])
print(image[0][24])
print(image[99][0])
plt.imshow(image, cmap='gray')
plt.show()
