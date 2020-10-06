import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

lena = mpimg.imread("lena.png")
print(len(lena))
print(len(lena[0]))
print(lena[0][0])
plt.imshow(lena)

