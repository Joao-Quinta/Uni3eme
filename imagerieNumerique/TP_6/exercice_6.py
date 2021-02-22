'''
TP6 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 4
'''

import lib

# 1

tp6_005 = lib.read_image_ski_no_multiply('images/tp6_005.jpg')
tp6_006 = lib.read_image_ski_no_multiply('images/tp6_006.jpg')
image = [tp6_005, tp6_006]
filtre_avearaging_3 = 1 / 9 * lib.np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
filtre_avearaging_4 = 1 / 16 * lib.np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

filtre_avearaging_5 = 1 / (11*11) * lib.np.array(
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
filters = [filtre_avearaging_3, filtre_avearaging_4, filtre_avearaging_5]
toPlot = []

for imagee in image:
    toPlot.append(imagee)
    for filter in filters:
        padded = lib.padding(imagee, filter, 'constant')
        image_padded_filtered = lib.image_filtering(padded, filter)
        toPlot.append(image_padded_filtered)

row = 2
col = 4
labels = ['Original 5 ', "Average filter 3x3", "Average filter 4x4", "Average filter 11x11", 'Original 6 ',
          "Average filter 3x3", "Average filter 4x4", "Average filter 11x11"]
lib.affichage_rows_cols(row, col, toPlot, labels, row * col, 'gray')

# 2
#
# toPlot = []
# for imagee in image:
#     toPlot.append(imagee)
#     toPlot.append(lib.median_filter(imagee, 5))
#
# row = 2
# col = 2
# labels = ['Original 5 ', "median filter 5x5", "Original 6", "median filter 5x5"]
# lib.affichage_rows_cols(row, col, toPlot, labels, row * col, 'gray')
