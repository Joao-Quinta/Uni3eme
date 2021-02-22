import matplotlib.pyplot as plt
import skimage as ski
import skimage.io as skio
import skimage.exposure as expo
import numpy as np
import cv2
import copy
import skimage.color as color


def get_image_histogram(image):
    counts, centers = expo.histogram(image, nbins=image.shape[0])
    return [counts, centers]


def read_image(path):
    return plt.imread(path)


def read_image_cv2(path, flag):
    return cv2.imread(path, flags=flag)


def read_image_ski_color(path):
    return skio.imread(path, as_gray=True)


def read_image_ski_gris(path):
    return (skio.imread(path, as_gray=False) * 255).astype("uint8")


def equalize_hist_ski(image):
    return expo.equalize_hist(image, nbins=image.shape[0])


def match_hist_ski(image, reference, multichannel):
    return expo.match_histograms(image, reference, multichannel=multichannel)


def gamma_correction(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


def image_negative_one_channel(image):
    image_negative = copy.deepcopy(image)
    for i in range(0, image_negative.shape[0] - 1):
        for j in range(0, image_negative.shape[1] - 1):
            pixel = image_negative[i, j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
            image_negative[i, j] = pixel
    return image_negative


def contrast_ajustment_one_channel(image):
    image_copy = copy.deepcopy(image)
    L = np.min(image_copy)
    H = np.max(image_copy)
    # print("dinamyc range pre : [", L, " , ", H, "]")
    for i in range(len(image)):
        for j in range(len(image[i])):
            image_copy[i][j] = (255 / (H - L)) * (image_copy[i][j] - L)
    L = np.min(image_copy)
    H = np.max(image_copy)
    # print("dinamyc range post : [", L, " , ", H, "]")
    return image_copy


def affichage_rows_cols(rows, cols, images, labels, lastImage, cmap):
    rows = rows
    cols = cols
    axes = []
    fig = plt.figure()
    for i in range(rows * cols):
        axes.append(fig.add_subplot(rows, cols, i + 1))
        if i < lastImage:
            plt.imshow(images[i], cmap=cmap)
        else:
            plt.bar(images[i][1], images[i][0])
        plt.title(labels[i])

    fig.tight_layout()
    plt.show()


def split_one_to_three(image):
    b, g, r = cv2.split(image)
    return [b, g, r]


def rescale_intensity_ski(image):
    return expo.rescale_intensity(image)


def rescale_intensity_percentile_ski(image, inf, sup):
    inf_, sup_ = np.percentile(image, (inf, sup))
    return expo.rescale_intensity(image, in_range=(inf_, sup_))


def convert_rgb_2_gray(image):
    return color.rgb2gray(image)


def treshold(image, threshold):
    image_r = copy.deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] >= threshold * 255:
                image_r[i][j] = 1
            else:
                image_r[i][j] = 0
    return image_r


def pixel_wise_multiplication(image1, image2):
    image_r = copy.deepcopy(image1)
    for i in range(image1.shape[0]):
        for j in range(image1.shape[1]):
            image_r[i][j] = image1[i][j] * image2[i][j]
    return image_r
