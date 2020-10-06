import matplotlib.pyplot as plt
import matplotlib.image as mpimg

lena = mpimg.imread("lena.png")
plt.imshow(lena)
plt.colorbar()
plt.show()

