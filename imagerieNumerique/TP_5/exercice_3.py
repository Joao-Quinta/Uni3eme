'''
TP5 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 3
'''

import lib


T1 = lib.np.float32([[1, 0.5, 1], [0.5, 1, 0], [0, 0, 1]])

T2 = lib.np.float32([[1.5, -0.5, 0], [0, 0.5, 0], [0, -0.002, 1]])

trans = [T1, T2]

rectangle_base = lib.np.float32([[0, 2, 3, 1], [0, 0, 2, 2]])
rectangles = [rectangle_base]
labels = ["rectangle base"]
# we add the 3rd coordinate full of ones, first list is the X cc, 2nd the Y and the 3rd the ones
coordinates = lib.np.float32([[0, 2, 3, 1], [0, 0, 2, 2], [1, 1, 1, 1]])

for i in range(len(trans)):
    rectangles.append(lib.projective_transformation_handmade(coordinates, trans[i]))
    label = "transformation T"+str(i+1)
    labels.append(label)

lib.affiche_rectangles_plot(rectangles, labels)



