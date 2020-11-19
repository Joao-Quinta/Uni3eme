'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 5
'''
import lib

image2 = lib.read_image_cv2('images/img_2.png', 0)
image4 = lib.read_image_cv2('images/img_4.png', 0)

image4_hist_match_image2 = lib.match_hist_ski(image4, image2, False)

histo_image2 = lib.get_image_histogram(image2)
histo_image4 = lib.get_image_histogram(image4)
histo_image4_hist_match_image2 = lib.get_image_histogram(image4_hist_match_image2)

images = [image2, image4, image4_hist_match_image2, histo_image2, histo_image4, histo_image4_hist_match_image2]
labels = ["image 2", "image 4 pre match", "image 4 post match", "histogram image2", "histogram image4 pre match",
          "histogram image4 post match"]

lib.affichage_rows_cols(2, 3, images, labels, 3, 'gray')
