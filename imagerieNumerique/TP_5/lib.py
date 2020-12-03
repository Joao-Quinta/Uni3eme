import matplotlib.pyplot as plt
import skimage as ski
import skimage.io as skio
import skimage.exposure as expo
import skimage.transform as transfo
import numpy as np
import cv2
import copy
import skimage.color as color


def read_image_cv2(path, flag):
    return cv2.imread(path, flags=flag)


def read_image_ski_no_multiply(path):
    return skio.imread(path)


def read_image_ski_multiply(path, flag):
    return (skio.imread(path, as_gray=flag) * 255).astype("uint8")


def affine_transformation(A, val, b):
    x = []
    for i in range(A.shape[0]):
        result = 0
        for j in range(A.shape[1]):
            result = result + ((A[i][j] * val[j]) + b[j])
        x.append(result)
    return x


def rotation_image(image, rota):
    return transfo.rotate(image, rota)


def projective_transformation_handmade(rectangle, Transformation):
    x_y_p_tilda = np.dot(Transformation, rectangle)
    x_y = copy.deepcopy(x_y_p_tilda)
    for i in range(len(x_y_p_tilda)):
        x_y[i] = np.divide(x_y_p_tilda[i], x_y_p_tilda[-1])
    x_y = x_y[:-1]
    return x_y


def projective_transformation(image, transformation):
    transformed = transfo.ProjectiveTransform(transformation)
    return transfo.warp(image, transformed)


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


def affiche_rectangles(rectangles_liste, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for axis in rectangles_liste:
        ax.add_patch(plt.Polygon(xy=list(zip(axis[0], axis[1])), fill=False))
    plt.axis("on")
    ax.set_xlim((-2, 6))
    ax.set_ylim((-2, 6))
    plt.show()
