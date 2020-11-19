'''
TP4 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 3
'''

import lib


# (b)


image9 = lib.read_image_cv2('images/img_9.png', 1)
image9_red, image9_green, image9_blue = lib.split_one_to_three(image9)

image9_red_stretch = lib.contrast_ajustment_one_channel(image9_red)
image9_green_stretch = lib.contrast_ajustment_one_channel(image9_green)
image9_blue_stretch = lib.contrast_ajustment_one_channel(image9_blue)

image9_red_hist = lib.get_image_histogram(image9_red)
image9_green_hist = lib.get_image_histogram(image9_green)
image9_blue_hist = lib.get_image_histogram(image9_blue)

image9_red_stretch_hist = lib.get_image_histogram(image9_red_stretch)
image9_green_stretch_hist = lib.get_image_histogram(image9_green_stretch)
image9_blue_stretch_hist = lib.get_image_histogram(image9_blue_stretch)

images = [image9_red, image9_green, image9_blue,
          image9_red_hist, image9_green_hist, image9_blue_hist,
          image9_red_stretch_hist, image9_green_stretch_hist, image9_blue_stretch_hist]

labels = ["image 9 red channel", "image 9 green channel", "image 9 blue channel",
          "image 9 red channel hist", "image 9 green channel hist", "image 9 blue channel hist",
          "image 9 red channel stretch hist", "image 9 green channel stretch hist", "image 9 blue channel stretch hist"]

lib.affichage_rows_cols(3, 3, images, labels, 3, 'gray')


# (c)


image9_stretch_rescale_intensity = lib.rescale_intensity_ski(image9)
image9_stretch_rescale_intensity_red, image9_stretch_rescale_intensity_green, image9_stretch_rescale_intensity_blue = lib.split_one_to_three(
    image9_stretch_rescale_intensity)

image9_stretch_rescale_intensity_red_gray = lib.convert_rgb_2_gray(image9_stretch_rescale_intensity_red)
image9_stretch_rescale_intensity_green_gray = lib.convert_rgb_2_gray(image9_stretch_rescale_intensity_green)
image9_stretch_rescale_intensity_blue_gray = lib.convert_rgb_2_gray(image9_stretch_rescale_intensity_blue)

image9_stretch_rescale_intensity_red_gray_hist = lib.get_image_histogram(image9_stretch_rescale_intensity_red_gray)
image9_stretch_rescale_intensity_green_gray_hist = lib.get_image_histogram(image9_stretch_rescale_intensity_green_gray)
image9_stretch_rescale_intensity_blue_gray_hist = lib.get_image_histogram(image9_stretch_rescale_intensity_blue_gray)

images = [image9_red_stretch_hist,
          image9_green_stretch_hist,
          image9_blue_stretch_hist,
          image9_stretch_rescale_intensity_red_gray_hist,
          image9_stretch_rescale_intensity_green_gray_hist,
          image9_stretch_rescale_intensity_blue_gray_hist]

labels = ["image 9 red channel stretch hist (handmade)",
          "image 9 green channel stretch hist (handmade)",
          "image 9 blue channel stretch hist (handmade)",
          "image 9 red channel stretch hist (rescale_intensity())",
          "image 9 green channel stretch hist (rescale_intensity())",
          "image 9 blue channel stretch hist (rescale_intensity())"]

lib.affichage_rows_cols(2, 3, images, labels, 0, 'gray')


# (d)

image9_stretch_rescale_intensity_percentile = lib.rescale_intensity_percentile_ski(image9, 5, 95)
image9_stretch_rescale_intensity_percentile_red, image9_stretch_rescale_intensity_percentile_green, image9_stretch_rescale_intensity_percentile_blue = lib.split_one_to_three(
    image9_stretch_rescale_intensity_percentile)

image9_stretch_rescale_intensity_percentile_red_gray = lib.convert_rgb_2_gray(image9_stretch_rescale_intensity_percentile_red)
image9_stretch_rescale_intensity_percentile_green_gray = lib.convert_rgb_2_gray(image9_stretch_rescale_intensity_percentile_green)
image9_stretch_rescale_intensity_percentile_blue_gray = lib.convert_rgb_2_gray(image9_stretch_rescale_intensity_percentile_blue)

image9_stretch_rescale_intensity_percentile_red_gray_hist = lib.get_image_histogram(image9_stretch_rescale_intensity_percentile_red_gray)
image9_stretch_rescale_intensity_percentile_green_gray_hist = lib.get_image_histogram(image9_stretch_rescale_intensity_percentile_green_gray)
image9_stretch_rescale_intensity_percentile_blue_gray_hist = lib.get_image_histogram(image9_stretch_rescale_intensity_percentile_blue_gray)

images = [image9_stretch_rescale_intensity_red_gray_hist,
          image9_stretch_rescale_intensity_green_gray_hist,
          image9_stretch_rescale_intensity_blue_gray_hist,
          image9_stretch_rescale_intensity_percentile_red_gray_hist,
          image9_stretch_rescale_intensity_percentile_green_gray_hist,
          image9_stretch_rescale_intensity_percentile_blue_gray_hist]

labels = ["image 9 red channel stretch hist (rescale_intensity())",
          "image 9 green channel stretch hist (rescale_intensity())",
          "image 9 blue channel stretch hist (rescale_intensity())",
          "image 9 red channel stretch hist (percentile())",
          "image 9 green channel stretch hist (percentile())",
          "image 9 blue channel stretch hist (percentile())"]

lib.affichage_rows_cols(2, 3, images, labels, 0, 'gray')
