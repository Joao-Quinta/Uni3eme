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


def read_image_cv2(path, flag):
    return cv2.imread(path, flags=flag)


def read_image_ski_no_multiply(path):
    return skio.imread(path)


def read_image_ski_multiply(path, flag):
    return (skio.imread(path, as_gray=flag) * 255).astype("uint8")


def scaling(forme, alpha, beta):
    scale_matrix = np.float32([[alpha, 0], [0, beta]])
    return np.dot(scale_matrix, forme)


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


def translation(triangle, value, type_trans):
    triangle_rescale = scaling(triangle, 1, 1)
    if type_trans == 'horizontal':
        triangle_rescale[0] = np.add(triangle_rescale[0], value)
    elif type_trans == 'vertical':
        triangle_rescale[1] = np.add(triangle_rescale[1], value)
    elif type_trans == 'both':
        triangle_rescale[0] = np.add(triangle_rescale[0], value)
        triangle_rescale[1] = np.add(triangle_rescale[1], value)
    return triangle_rescale


def projective_transformation_handmade(rectangle, Transformation):
    x_y_p_tilda = np.dot(Transformation, rectangle)
    x_y = copy.deepcopy(x_y_p_tilda)
    for i in range(len(x_y_p_tilda)):
        x_y[i] = np.divide(x_y_p_tilda[i], x_y_p_tilda[-1])
    x_y = x_y[:-1]
    return x_y


def rotation_triangle(triangle, rotation):
    sin_r = np.sin(rotation)
    cos_r = np.cos(rotation)
    A = np.float32([[cos_r, -1 * sin_r], [sin_r, cos_r]])
    return np.dot(A, triangle)


def flip_triangle(triangle, type_flip):
    indice1 = -1
    indice2 = 1
    if type_flip == "horizontal":
        indice1 = 1
        indice2 = -1
    return np.dot(np.float32([[indice1, 0], [0, indice2]]), triangle)


def triangle_bend(triangle, value, bend_type):
    if bend_type == "horizontal":
        A = np.float32([[1, value], [0, 1]])
    elif bend_type == "vertical":
        A = np.float32([[1, 0], [value, 1]])
    elif bend_type == "both":
        A = np.float32([[1, value[0]], [value[1], 1]])
    return np.dot(A, triangle)


def projective_transformation(image, transformation):
    transformed = transfo.ProjectiveTransform(transformation)
    return transfo.warp(image, transformed)


def downscale(image):
    liste_garder = [x for x in range(len(image)) if x % 3 == 0]
    image_down = [[pix for index, pix in enumerate(image[row]) if index in liste_garder] for row in liste_garder]
    return np.array(image_down)


def upscale_linear(image):
    return image.repeat(3, axis=0).repeat(3, axis=1)


def resize_openCV(image, what, val, flag):
    dim = (int(image.shape[1] * val / 100), int(image.shape[0] * val / 100))
    if what == "up":
        dim = (int(image.shape[1] * val / 100), int(image.shape[0] * val / 100))
    return cv2.resize(image, dim, interpolation=flag)


def bilinear_resize(image, height, width):
    img_height, img_width = image.shape[:2]
    resized = np.empty([height, width])
    x_ratio = float(img_width - 1) / (width - 1) if width > 1 else 0
    y_ratio = float(img_height - 1) / (height - 1) if height > 1 else 0
    for i in range(height):
        for j in range(width):
            x_l, y_l = math.floor(x_ratio * j), math.floor(y_ratio * i)
            x_h, y_h = math.ceil(x_ratio * j), math.ceil(y_ratio * i)
            x_weight = (x_ratio * j) - x_l
            y_weight = (y_ratio * i) - y_l
            a = image[y_l, x_l]
            b = image[y_l, x_h]
            c = image[y_h, x_l]
            d = image[y_h, x_h]
            pixel = a * (1 - x_weight) * (1 - y_weight) \
                    + b * x_weight * (1 - y_weight) + \
                    c * y_weight * (1 - x_weight) + \
                    d * x_weight * y_weight
            resized[i][j] = pixel
    return resized


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


def affiche_rectangles_plot(rectangles_liste, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for i in range(len(rectangles_liste)):
        ax.add_patch(
            plt.Polygon(xy=list(zip(rectangles_liste[i][0], rectangles_liste[i][1])), fill=False, label=labels[i]))
    plt.axis("on")
    plt.grid("on")
    plt.legend()
    ax.set_xlim((-2, 6))
    ax.set_ylim((-2, 6))
    plt.show()


def afficher_triangle_plot(triangles, labels):
    for i in range(len(triangles)):
        plt.triplot(triangles[i][0], triangles[i][1], label=labels[i])
    plt.grid("on")
    plt.axis("on")
    plt.legend()
    plt.show()
