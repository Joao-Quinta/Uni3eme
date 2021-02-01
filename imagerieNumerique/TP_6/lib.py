import matplotlib.pyplot as plt
import skimage as ski
import skimage.io as skio
import skimage.exposure as expo
import skimage.transform as transfo
import numpy as np
import cv2
import copy
import skimage.color as color
import skimage.metrics as metric
import math


def read_image_ski_no_multiply(path):
    return skio.imread(path)


def padding(images, filtre, mode):
    images_result = np.pad(images,
                           ((filtre.shape[0] - 1, filtre.shape[0] - 1), (filtre.shape[1] - 1, filtre.shape[1] - 1)),
                           mode)
    return images_result


def image_filtering(padded, filterr):
    image_copy = copy.deepcopy(padded)
    for index_row, row in enumerate(image_copy):
        if index_row + filterr.shape[0] >= len(image_copy):
            continue
        for index_pixel, pixel in enumerate(row):
            if index_pixel + filterr.shape[1] >= len(row):
                continue
            padded[index_row + (filterr.shape[0] // 2 - 1)][index_pixel + (filterr.shape[0] // 2 - 1)] = np.sum(
                np.multiply(filterr, image_copy[index_row:index_row + filterr.shape[0],
                                     index_pixel:index_pixel + filterr.shape[1]]))
    return padded


def median_filter(image, size):
    median = cv2.medianBlur(image, size)
    return median


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