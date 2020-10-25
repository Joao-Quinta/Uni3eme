# il manque faire :
# (1) faire les parentheses
# (2) evaluer l equation

import copy

def replaceString(string, old, new):
    string1 = ""
    string2 = ""
    for i in range(0, len(string)):
        if string[i] == old:
            string1 = string[0:i]
            string2 = string[i + 1: len(string)]
    return string1 + new + string2


# print(replaceString("abc", "b", "s"))
def enleveNonTer(arbre):
    i = 0
    for i in range(0, len(arbre[-1])):
        if arbre[-1][i] == "D":
            arbre[-1] = replaceString(arbre[-1], "D", "e")
        elif arbre[-1][i] == "G":
            arbre[-1] = replaceString(arbre[-1], "G", "e")
        elif arbre[-1][i] == "(":
            return arbre
        i = i + 1


def enleveNonTerEnP(arbre):
    j = 0
    for i in range(0, len(arbre[-1])):
        if arbre[-1][i] == "(":
            j = i + 1
            break
        else:
            i = i + 1
    for z in range(j, len(arbre[-1])):
        if arbre[-1][z] == "D":
            arbre[-1] = replaceString(arbre[-1], "D", "e")
        elif arbre[-1][z] == "G":
            arbre[-1] = replaceString(arbre[-1], "G", "e")
        elif arbre[-1][z] == ")":
            return arbre
        z = z + 1


def opArbre(arbre, quoi, valeur, op):
    print(arbre, quoi, "asdasdasd")
    if quoi == "nb":
        if "F" in arbre[-1]:
            arbre.append(replaceString(arbre[-1], "F", str(valeur)))
            return arbre
        elif "T" in arbre[-1]:
            arbre.append(replaceString(arbre[-1], "T", "FG"))
            arbre.append(replaceString(arbre[-1], "F", str(valeur)))
            return arbre
        elif "E" in arbre[-1]:
            arbre.append(replaceString(arbre[-1], "E", "TD"))
            arbre.append(replaceString(arbre[-1], "T", "FG"))
            arbre.append(replaceString(arbre[-1], "F", str(valeur)))
            return arbre
    if quoi == "op":
        if op == "+":
            if "D" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "D", "+E"))
                return arbre
            elif "E" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "E", "TD"))
                arbre.append(replaceString(arbre[-1], "D", "+E"))
                return arbre
        elif op == "*":
            if "G" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "G", "*T"))
                return arbre
            elif "T" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "T", "FG"))
                arbre.append(replaceString(arbre[-1], "G", "*T"))
            elif "E" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "E", "TD"))
                arbre.append(replaceString(arbre[-1], "T", "FG"))
                arbre.append(replaceString(arbre[-1], "G", "*T"))
                return arbre
        elif op == "(":
            if "F" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "F", "(E)"))
                arbre = enleveNonTer(arbre)
                return arbre
            elif "T" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "T", "FG"))
                arbre.append(replaceString(arbre[-1], "F", "(E)"))
                arbre = enleveNonTer(arbre)
                return arbre
            elif "E" in arbre[-1]:
                arbre.append(replaceString(arbre[-1], "E", "TD"))
                arbre.append(replaceString(arbre[-1], "T", "FG"))
                arbre.append(replaceString(arbre[-1], "F", "(E)"))
                arbre = enleveNonTer(arbre)
                return arbre
        elif op == ")":
            arbre = enleveNonTerEnP(arbre)
            return arbre



def checkNextOp(ligne, arbre):
    nb = 0
    parentheses = False
    if len(ligne) != 1:
        parentheses = True
    for i in range(0, len(ligne)):
        for j in range(0,ligne[i]):
            if ligne[i][j] in "+*":
                arbre = opArbre(arbre, "op", nb, ligne[i][j])
            elif ligne[j] in "-0123456789":


# # fonction qui recoit la ligne, detecte la premiere operation, et appelle recursiveConstruction avec les bonnes infos
#
# # ligne est la ligne de code
#
# # elle retourne la ligne de code apres l evaluation ->
# # si elle recoit "3+3" -> recursiveConstruction("3","+"), et retorune "3"
# # si elle recoit "3" -> recursiveConstruction("3","over"), et retorune ""
# j = 1
# while j < len(ligne):
#     if ligne[j] in "+*(":
#         # print("is the number : ", ligne[0:i])
#         # print("is the op : ", ligne[i])
#         # print("we return this : ", ligne[i + 1:len(ligne)])
#
#         # si ligne = "01234" -> ligne[0:1] = "0"
#         # recursiveConstruction(ligne[0:j], ligne[j])
#         # comme ca on retourne le reste de eval si ligne = "01234" -> ligne[1:len(ligne)] = 1234 (no need len ligne en vrai)
#         return ligne[j + 1:len(ligne)]
#     # check si c est nombre
#     elif ligne[j] in "-0123456789":
#         # on garde le - ici pour les nb negatifs
#         j = j + 1
#         # tant que c est pas une operation, c est un nb, donc on itére
# # recursiveConstruction(ligne[0:j], "over")
# return ""


def checkOrder(ligne, start):
    last = "Op"
    end = "Op"
    if start == 0:
        last = "Int"
        end = "Int"
    i = 0
    while i < len(ligne):
        if ligne[i] in "+*" and last == "Int":
            last = "Op"
            i = i + 1
        elif ligne[i] in "-0123456789" and last == "Op":
            j = i + 1
            while j < len(ligne) and ligne[j] in "-0123456789":
                j = j + 1
            last = "Int"
            i = j
        else:
            return False
    if last == end:
        return True
    else:
        return False


def checkOperationsOrder(listeParseParentheses):
    checkOrderOperationsIci = [0, 0]
    if len(listeParseParentheses) > 1:
        if listeParseParentheses[3][0]:
            checkOrderOperationsIci[0] = checkOrder(listeParseParentheses[0][0], 1)
            # if not checkOrderOperations[0]:
            #     print("forme non valide ")
            #     break
            # this check has to e done when continuing next step
        else:
            checkOrderOperationsIci[0] = True
        if listeParseParentheses[3][1]:
            checkOrderOperationsIci[1] = checkOrder(listeParseParentheses[2][0], 0)
            # if not checkOrderOperations[1]:
            #     print("forme non valide ")
            #     break
            # this check has to e done when continuing next step
        else:
            checkOrderOperationsIci[1] = True
    else:
        checkOrderOperationsIci[0] = True
        checkOrderOperationsIci[1] = True
    return checkOrderOperationsIci


def parserP(ligne):
    if ligne == 0:
        return [ligne]
    parentheseGauche = False
    parentheseDroite = False
    avantParenthese = 0
    apresParenthese = 0
    indiceParentheseGauche = 0
    indiceParentheseDroite = len(ligne) - 1
    for j in range(0, len(ligne)):
        if ligne[j] == "(":
            indiceParentheseGauche = j
            i = j + 1
            while i < len(ligne):
                if ligne[i] == ")":
                    indiceParentheseDroite = i
                    break
                elif ligne[i] == "(":
                    for z in range(i + 1, len(ligne)):
                        p = j + 1 - z
                        pp = len(ligne) - 1 - abs(p)
                        if ligne[pp] == ")":
                            indiceParentheseDroite = pp
                            break
                    break
                i = i + 1
            break
    if indiceParentheseGauche != 0:
        avantParenthese = ligne[0:indiceParentheseGauche]
        parentheseDroite = True
    if indiceParentheseDroite != len(ligne) - 1:
        apresParenthese = ligne[indiceParentheseDroite + 1:len(ligne)]
        parentheseGauche = True
    # CBA
    if indiceParentheseGauche == 0 and indiceParentheseDroite == len(ligne) - 1 and ligne[0] != '(':
        # pas de parenthese dans E
        # enParenthese = E
        enParenthese = ligne
        return [enParenthese]
    else:
        enParenthese = ligne[indiceParentheseGauche + 1:indiceParentheseDroite]
        # parenthese dans E
        # avantParenthese is text before first opening parenthese -> 3+(3) will be: avantParenthese = 3+
        # apresParenthese is text after last closing parenthese -> (3)+3 will be: apresParenthese = +3
        # enParenthese is whats between first opening and last closing parenthese -> ((2+2)) will be : en parenthese = (2+2)
        # parentheseDroite = False by default, if its final value is True then : E is of type: E + (E)
        # parentheseGauche = False by default, if its final value is True then : E is of type: (E) + E
        return [parserP(avantParenthese), parserP(enParenthese), parserP(apresParenthese),
                [parentheseDroite, parentheseGauche]]


def transformListe(listeParenthesesIci2):
    newListeIci = []
    if len(listeParenthesesIci2) == 1:
        newListeIci.append(listeParenthesesIci2[0])
    else:
        for i in range(0, 3):
            if listeParenthesesIci2[i][0] != 0:
                newListeIci.append(listeParenthesesIci2[i][0])

    return newListeIci


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    # cette boucle enleve tous les "\n" aux lignes s il y en a
    for i in range(0, len(lignes)):
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    print(lignes)

    for i in range(0, len(lignes)):
        print("E = ", lignes[i])
        listeParentheses = parserP(lignes[i])
        arbre = ["E", "TD"]
        print(listeParentheses)
        checkOrderOperations = checkOperationsOrder(listeParentheses)
        if checkOrderOperations[0] and checkOrderOperations[1]:
            newListe = transformListe(listeParentheses)
            print(newListe)
            #checkNextOp(newListe, arbre)
        else:
            print("la formule est non accepte par la grammaire")
