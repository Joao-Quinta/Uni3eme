'''
TP5 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 4
'''


import lib


T1 = lib.np.float32([[1, 0.5, 1], [0.5, 1, 0], [0, 0, 1]])

T2 = lib.np.float32([[1.5, -0.5, 0], [0, 0.5, 0], [0, -0.002, 1]])

trans = [T1, T2]


# a


image_lena_grix = lib.read_image_ski_multiply('images/lena.png', 'True')
images = [image_lena_grix]
labels = ["lena original (grix)"]

for i in range(len(trans)):
    images.append(lib.projective_transformation(image_lena_grix, trans[i]))
    label = " transformation T" + str(i + 1)
    labels.append(label)

row = 1
col = 3

lib.affichage_rows_cols(row, col, images, labels, row * col, 'gray')


# b


image_lena_grix = lib.read_image_ski_no_multiply('images/lena.png')
images = [image_lena_grix]
labels = ["lena original"]

for i in range(len(trans)):
    images.append(lib.projective_transformation(image_lena_grix, trans[i]))
    label = " transformation T" + str(i + 1)
    labels.append(label)

row = 1
col = 3

lib.affichage_rows_cols(row, col, images, labels, row * col, 'gray')
