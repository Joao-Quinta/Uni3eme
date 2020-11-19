'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 6
'''
import lib

image3 = lib.read_image_cv2('images/img_3.png', 0)

images = [image3]
labels = ["original"]
gamma = [0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0, 1.5, 2.0]

for i in gamma:
    images.append(lib.gamma_correction(image3, i))
    labels.append("gamma = " + str(i))

rows = 3
cols = 3
lib.affichage_rows_cols(rows, cols, images, labels, rows * cols, "gray")
rows = 1
cols = 2
lib.affichage_rows_cols(rows, cols, [images[0], images[2]], [labels[0], "chosen " + labels[2]], rows * cols, "gray")
