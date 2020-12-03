'''
TP5 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 5
'''

import lib

# a

image_1 = lib.read_image_ski_no_multiply('images/img_1.png')
downscale_image_1 = lib.downscale(image_1)
upscale_downscale_image_1 = lib.upscale_linear(downscale_image_1)

mse = lib.metric.mean_squared_error(image_1, upscale_downscale_image_1)

# b

cv2_downscale_image_1 = lib.resize_openCV(image_1, "down", 34, lib.cv2.INTER_NEAREST)
cv2_upscale_downscale_image_1 = lib.resize_openCV(cv2_downscale_image_1, "up", 300,lib.cv2.INTER_NEAREST)

mse1 = lib.metric.mean_squared_error(image_1, cv2_upscale_downscale_image_1)

images = [image_1, upscale_downscale_image_1, cv2_upscale_downscale_image_1]
labels = ["image 1", " upscale of downscale handmade" + str(mse), " upscale of downscale CV2 - mse = " + str(mse1)]

rows = 1
cols = 3
lib.affichage_rows_cols(rows, cols, images, labels, rows * cols, "gray")

# c


image_1 = lib.read_image_ski_multiply('images/lena.png', 'True')

# b

cv2_downscale_image_1 = lib.resize_openCV(image_1, "down", 34, lib.cv2.INTER_NEAREST)
cv2_upscale_downscale_image_1 = lib.resize_openCV(cv2_downscale_image_1, "up", 295.5, lib.cv2.INTER_NEAREST)

mse1 = lib.metric.mean_squared_error(image_1, cv2_upscale_downscale_image_1)

images = [image_1,  cv2_upscale_downscale_image_1]
labels = ["image 1", " upscale of downscale CV2 - mse = " + str(mse1)]

rows = 1
cols = 2
lib.affichage_rows_cols(rows, cols, images, labels, rows * cols, "gray")
