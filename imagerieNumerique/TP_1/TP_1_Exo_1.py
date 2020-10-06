import matplotlib.pyplot as plt
import matplotlib.image as mpimg

lena = mpimg.imread("lena.png")#lecture de image (ouvre l image)
plt.imshow(lena)#ca va afficher l image, mais ca a besoin de la ligne 6
plt.colorbar()
plt.show()#sans cette ligne l image s affiche aps

