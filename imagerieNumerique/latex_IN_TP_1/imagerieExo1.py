import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

lena = mpimg.imread("lena.png")
print(lena)
print(len(lena))
lenaPlot = plt.imshow(lena)

