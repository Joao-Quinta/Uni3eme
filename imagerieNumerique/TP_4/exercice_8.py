'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 8
'''

import lib

image10 = lib.read_image_ski_1('images/img_10.png', False)
values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

images = [image10]
labels = ["original"]
for threshold in values:
    images.append(lib.treshold(image10, threshold))
    string = "threshold : " + str(threshold)
    labels.append(string)

# print(images[1])

lib.affichage_rows_cols(4, 3, images, labels, 4 * 3, "gray")

for i in range(1, len(images)):
    images[i] = lib.pixel_wise_multiplication(images[0], images[i])


lib.affichage_rows_cols(4, 3, images, labels, 4 * 3, "gray")

# image_good = images[3]
# label_good = labels[3]
# images1 = [image10, images[1], image_good]
# labels1 = ["original", labels[1], label_good]
# lib.affichage_rows_cols(1, 3, images1, labels1, 1 * 3, "gray")
