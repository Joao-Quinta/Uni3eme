'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 1
'''

import lib

image1 = lib.read_image_cv2('images/img_1.png', 1)
image2 = lib.read_image_cv2('images/img_2.png', 1)
image3 = lib.read_image_cv2('images/img_3.png', 1)
# image1 = lib.read_image('images/img_1.png')
# image2 = lib.read_image('images/img_2.png')
# image3 = lib.read_image('images/img_3.png')

image1_hist = lib.get_image_histogram(image1)
image2_hist = lib.get_image_histogram(image2)
image3_hist = lib.get_image_histogram(image3)

images = [image1, image2, image3, image1_hist, image2_hist, image3_hist]
labels = ["image 1", "image 2", "image 3", "histogram image 1", "histogram image 2", "histogram image 3"]

rows = 2
cols = 3
lib.affichage_rows_cols(rows, cols, images, labels, 3, "gray")
