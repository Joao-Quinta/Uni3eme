'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 4
'''
import lib

image11 = lib.read_image_cv2('images/img_11.png', 0)
image11_equalized_ski = lib.equalize_hist_ski(image11)

histogram_image11 = lib.get_image_histogram(image11)
histogram_image11_equalized_ski = lib.get_image_histogram(image11_equalized_ski)

images = [image11, image11_equalized_ski, histogram_image11, histogram_image11_equalized_ski]
labels = ["before equalized hist", "after equalized hist", "histogram before", "histogram after"]

lib.affichage_rows_cols(2, 2, images, labels, 2, 'gray')
