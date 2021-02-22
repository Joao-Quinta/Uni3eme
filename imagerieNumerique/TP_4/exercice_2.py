'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 2
'''

import lib

image4 = lib.read_image_cv2('images/img_4.png', 1)
image5 = lib.read_image_cv2('images/img_5.png', 1)
image6 = lib.read_image_cv2('images/img_6.png', 1)

image4_hist = lib.get_image_histogram(image4)
image5_hist = lib.get_image_histogram(image5)
image6_hist = lib.get_image_histogram(image6)

images = [image4, image5, image6, image4_hist, image5_hist, image6_hist]
labels = ["image 1", "image 2", "image 3", "histogram image 1", "histogram image 2", "histogram image 3"]

rows = 2
cols = 3
lib.affichage_rows_cols(rows, cols, images, labels, 3, "gray")
