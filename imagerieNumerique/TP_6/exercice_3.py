'''
TP6 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 3
'''

import lib

generated_image = lib.np.array([[1, 0], [0, 1]])

generated_image_big = lib.np.pad(generated_image, (255, 255), 'edge')

# filter as in exo 2 (not same size)
filterr = 1 / 9 * lib.np.ones([31, 31])

# a - 1 (zero padding filter)

images_padded_a_1 = lib.padding(generated_image_big, filterr, 'constant')
images_padded_filtered_a_1 = lib.image_filtering(images_padded_a_1, filterr)

# a - 2 (periodic filter)

images_padded_a_2 = lib.padding(generated_image_big, filterr, 'wrap')
images_padded_filtered_a_2 = lib.image_filtering(images_padded_a_2, filterr)

# a - 3 (symetric filter)

images_padded_a_3 = lib.padding(generated_image_big, filterr, 'symmetric')
images_padded_filtered_a_3 = lib.image_filtering(images_padded_a_3, filterr)

toPlot = [generated_image_big, images_padded_a_1, images_padded_filtered_a_1, generated_image_big, images_padded_a_2,
          images_padded_filtered_a_2, generated_image_big, images_padded_a_3, images_padded_filtered_a_3]
labels = ['original', "zero padding", "zero padding filter", "original", "padded periodic", "periodic filtered",
          "original", "padded symmetric", "symmetric filtered"]

row = 3
cols = 3
lib.affichage_rows_cols(row, cols, toPlot, labels, row*cols, 'gray')
