import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# exercice 2 partie 1
xAndY = []
y = np.linspace(0, 1, 100)
for i in range(0, 25):
    xAndY.append(y)

# uncomment lines 12 and 13 to get the image of the gradient
# plt.imshow(xAndY, cmap='gray')
# plt.show()


a = [[1, 0], [1, 0]]
# plt.imshow(a, cmap='gray')
# plt.show()

b = [[1, 1], [0, 0]]
# plt.imshow(b, cmap='gray')
# plt.show()

aArray = np.array(a)
bArray = np.array(b)
cArray = np.subtract((np.dot(aArray, bArray)), np.absolute(np.subtract(aArray, bArray)))

arrays = [aArray, bArray, cArray]

rows = 1
cols = 3
axes = []
fig = plt.figure()

for a in range(rows * cols):
    axes.append(fig.add_subplot(rows, cols, a + 1))
    plt.imshow(arrays[a], cmap='gray')
fig.tight_layout()
plt.show()