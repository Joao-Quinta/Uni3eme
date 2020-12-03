'''
TP5 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 2
'''


import lib


# exo a


image_1 = lib.read_image_ski_no_multiply('images/img_1.png', 'False')

# angles : 30 a gauche -> 30
# 45 a droite -> -45

images = [image_1]
labels = ["original image 1"]

rotation = [30, -45]

for angle in rotation:
    images.append(lib.rotation_image(image_1, angle))
    label = "rotation = " + str(angle)
    labels.append(label)

row = 1
col = 3

lib.affichage_rows_cols(row, col, images, labels, row * col, 'gray')


# exo b

image_lena = lib.read_image_ski_no_multiply('images/lena.png', 'False')

# angles : 30 a gauche -> 30
# 45 a droite -> -45

images = [image_lena]
labels = ["original lena"]

rotation = [30, -45]

for angle in rotation:
    images.append(lib.rotation_image(image_lena, angle))
    label = "rotation = " + str(angle)
    labels.append(label)

row = 1
col = 3

lib.affichage_rows_cols(row, col, images, labels, row * col, 'gray')