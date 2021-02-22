'''
TP6 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 4
'''

import lib

cameraMan = lib.read_image_ski_no_multiply('images/cameraman.jpg')

# a - laplacian filter

filterrLap = lib.np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

images_padded_lap = lib.padding(cameraMan, filterrLap, 'constant')
images_padded_filtered_lap = lib.image_filtering(images_padded_lap,filterrLap)
toPlot = [cameraMan, images_padded_lap, images_padded_filtered_lap]
labels = ["original", "padded image", "filtered image"]

row = 1
cols = 3
lib.affichage_rows_cols(row, cols, toPlot, labels, row * cols, 'gray')
