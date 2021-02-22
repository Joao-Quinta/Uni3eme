'''
TP6 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 2
'''

import lib
cameraMan = lib.read_image_ski_no_multiply('images/cameraman.jpg')


# a in lib


# b

filtre_b = 1 / 9 * lib.np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

image_padded_b = lib.padding(cameraMan, filtre_b, 'constant')

image_padded_filtered_b = lib.image_filtering(image_padded_b, filtre_b)


# c

filtre_c = 1 / 16 * lib.np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

image_padded_c = lib.padding(cameraMan, filtre_c, 'constant')

image_padded_filtered_c = lib.image_filtering(image_padded_c, filtre_c)


# affichage

row = 1
col = 3
toPlot = [cameraMan, image_padded_filtered_b, image_padded_filtered_c]
labels = ['Original', "Average filtre", "Gauss filtre"]
lib.affichage_rows_cols(row, col, toPlot, labels, row*col, 'gray')
