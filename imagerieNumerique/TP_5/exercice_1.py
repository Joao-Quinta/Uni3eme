'''
TP5 imagerie numerique
Costa da Quinta, Joao Filipe
exercice 1
'''

import lib

triangle = lib.np.float32([[0, 3, 2], [0, 2, 4]])

# a

liste_triangle = [triangle]
labels = ["orginal"]
scale = [1 / 2, 2]

for val in scale:
    liste_triangle.append(lib.scaling(triangle, val, val))
    label = "scale" + str(val)
    labels.append(label)

lib.afficher_triangle_plot(liste_triangle, labels)

# b

horizontal_translation = [2]
vertical_translation = [4]
both_translation = [1.5]

liste_triangle = [triangle]
labels = ["orginal"]

for i in range(len(horizontal_translation)):
    liste_triangle.append(lib.translation(triangle, horizontal_translation[i], "horizontal"))
    label = "translation horizontal " + str(horizontal_translation[i])
    labels.append(label)

for i in range(len(vertical_translation)):
    liste_triangle.append(lib.translation(triangle, vertical_translation[i], "vertical"))
    label = "translation vertical " + str(vertical_translation[i])
    labels.append(label)

for i in range(len(both_translation)):
    liste_triangle.append(lib.translation(triangle, both_translation[i], "both"))
    label = "translation both " + str(both_translation[i])
    labels.append(label)

lib.afficher_triangle_plot(liste_triangle, labels)

# c

# left is positive right is negative
liste_triangle = [triangle]
labels = ["orginal"]
rotation = [55, -180]

for rota in rotation:
    liste_triangle.append(lib.rotation_triangle(triangle, rota))
    label = "rotation : " + str(rota)
    labels.append(label)

lib.afficher_triangle_plot(liste_triangle, labels)

# d

liste_triangle = [triangle]
labels = ["original"]
flips = ['vertical', 'horizontal']

for flip in flips:
    liste_triangle.append(lib.flip_triangle(triangle, flip))
    label = "flip = " + flip
    labels.append(label)

lib.afficher_triangle_plot(liste_triangle, labels)

# e

liste_triangle = [triangle]
labels = ["original"]
bend_horizontal = [2.0]
bend_vertical = [1.5]
bend_both = [[1.5, 2.5]]

for i in range(len(bend_horizontal)):
    liste_triangle.append(lib.triangle_bend(triangle, bend_horizontal[i], "horizontal"))
    label = "bend horizontal " + str(bend_horizontal[i])
    labels.append(label)

for i in range(len(bend_vertical)):
    liste_triangle.append(lib.triangle_bend(triangle, bend_vertical[i], "vertical"))
    label = "bend vertical " + str(bend_vertical[i])
    labels.append(label)

for i in range(len(bend_both)):
    liste_triangle.append(lib.triangle_bend(triangle, bend_both[i], "both"))
    label = "bend both: hori = " + str(bend_both[i][0]) + " verti = " + str(bend_both[i][1])
    labels.append(label)

lib.afficher_triangle_plot(liste_triangle, labels)