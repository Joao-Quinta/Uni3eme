'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 7
'''

import lib

image1 = lib.read_image_cv2('images/img_1.png', 1)
image2 = lib.read_image_cv2('images/img_2.png', 1)

image1_negative = lib.image_negative_one_channel(image1)
image2_negative = lib.image_negative_one_channel(image2)

images = [image1, image1_negative, image2, image2_negative]
labels = ["image 1 ", "image 1 negative", "image 2", "image 2 negative"]

rows = 2
cols = 2
lib.affichage_rows_cols(rows, cols, images, labels, rows * cols, "gray")
