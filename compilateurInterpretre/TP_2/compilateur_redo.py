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
def enleveNonTer(arbreArg):
    arbre = arbreArg.copy()
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


def opArbre(arbreAppel, quoi, valeur, op):
    arbre = arbreAppel.copy()
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
    for i in range(0, len(ligne)):
        if i % 2 == 0:
            test = getIndexListeOperation(list(ligne[i]))  # [1]
            s = 0
            isOP = False
            for z in range(0, len(test)):
                if not isOP:
                    arbre = opArbre(arbre, "nb", ligne[i][s:test[z]], "")
                    arbre = opArbre(arbre, "op", nb, str(ligne[i][test[z]]))
                    s = test[z] + 1
            arbre = opArbre(arbre, "nb", ligne[i][test[-1] + 1:len(ligne[i])], "")
            arbre.append(arbre[-1].replace("G", "e"))
            print(arbre)

        elif i % 2 == 1:
            arbre = opArbre(arbre, "op", nb, "(")
            test = getIndexListeOperation(list(ligne[i]))  # [1]
            s = 0
            isOP = False
            for z in range(0, len(test)):
                if not isOP:
                    arbre = opArbre(arbre, "nb", ligne[i][s:test[z]], "")
                    arbre = opArbre(arbre, "op", nb, str(ligne[i][test[z]]))
                    s = test[z] + 1
                arbre = opArbre(arbre, "nb", ligne[i][test[-1] + 1:len(ligne[i])], "")
                arbre.append(arbre[-1].replace("G", "e"))

        arbre[-1] = arbre[-1].replace("D", "e")
    return arbre


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


def transformListe(listeParenthesesIci2, liste):
    newListeIci = liste.copy()
    if len(listeParenthesesIci2) == 1:
        newListeIci.append(listeParenthesesIci2[0])
    else:
        for i in range(0, 3):
            if listeParenthesesIci2[i][0] != 0 and len(listeParenthesesIci2[i]) == 1:
                newListeIci.append(listeParenthesesIci2[i][0])
            elif len(listeParenthesesIci2[i]) > 1:
                newListeIci = transformListe(listeParenthesesIci2[i], newListeIci)
    return newListeIci


def getIndexListeOperation(liste_input):
    index = 0
    listeIndexOperateur = []
    debutFinString = [34, 39, 44, 96, 8216, 8217]  # " ' ‘
    multiAddSpaceEqual = [32, 42, 43, 61]
    while index < len(liste_input):
        # for element in liste_input:
        if (ord(liste_input[index]) in range(65, 91)) or (ord(liste_input[index]) in range(97, 123)) or (
                ord(liste_input[index]) in debutFinString):
            isItAString = False
            isThereAnErrorInVariable = False
            isItTheEndOfListe = False
            compteurDebutFinString = 0
            if ord(liste_input[index]) in debutFinString:
                compteurDebutFinString += 1
                isItAString = True
            if index + 1 >= len(liste_input):
                isItTheEndOfListe = True
                index_copy = copy.deepcopy(index)
            else:
                index_copy = copy.deepcopy(index) + 1
            myString = str(liste_input[index])
            myVar = str(liste_input[index])
            # variable
            if not isItAString:
                while (ord(liste_input[index_copy]) in range(65, 91)) or (
                        ord(liste_input[index_copy]) in range(97, 123)) or ord(liste_input[index_copy]) in range(48,
                                                                                                                 58):
                    # 1 nombre dans liste, break tout de suite
                    if isItTheEndOfListe:
                        index_copy += 1
                        break
                    myVar = myVar + str(liste_input[index_copy])

                    if index_copy + 1 < len(liste_input):
                        index_copy += 1
                    else:
                        index_copy += 1
                        break
            # string
            else:
                isThereErrorAfterString = False
                while (ord(liste_input[index_copy]) in range(65, 91)) or (
                        ord(liste_input[index_copy]) in range(97, 123)) or (
                        ord(liste_input[index_copy]) in debutFinString) or (
                        ord(liste_input[index_copy]) in range(48, 58)):
                    # si on a un élément après le string -> error : exemple : 'abcd'6
                    if compteurDebutFinString >= 2:
                        isThereErrorAfterString = True
                    # si on trouve le 2ème guillemet pour fermer le string, on l'indique
                    if ord(liste_input[index_copy]) in debutFinString:
                        compteurDebutFinString += 1

                    myString = myString + str(liste_input[index_copy])
                    if index_copy + 1 != len(liste_input):
                        index_copy += 1
                    else:
                        index_copy += 1
                        break
                # si le string n'est pas fermée on l'indique

            index = copy.deepcopy(index_copy)
        # space
        elif ord(liste_input[index]) == 32:

            index += 1
        # numbers, real, negatifs
        elif ord(liste_input[index]) == 45 or ord(liste_input[index]) in range(48, 58):
            startsWithNegation = False
            isItTheEndOfListe = False
            isThereAnErrorInVariable = False
            if ord(liste_input[index]) == 45:
                startsWithNegation = True
            isItAreal = False
            if index + 1 >= len(liste_input):
                isItTheEndOfListe = True
                index_copy = copy.deepcopy(index)
            else:
                index_copy = copy.deepcopy(index) + 1
            myNumber = str(liste_input[index])
            while ord(liste_input[index_copy]) in range(48, 58) or ord(liste_input[index_copy]) == 46 or (
                    ord(liste_input[index_copy]) in range(65, 91)) or (
                    ord(liste_input[index_copy]) in range(97, 123)) or (ord(liste_input[index_copy]) in debutFinString):

                if (ord(liste_input[index_copy]) in range(65, 91)) or (
                        ord(liste_input[index_copy]) in range(97, 123)) or (
                        ord(liste_input[index_copy]) in debutFinString):
                    isThereAnErrorInVariable = True

                # 1 nombre dans liste, break tout de suite
                if isItTheEndOfListe:
                    index_copy += 1
                    break
                # si possède un '.' -> réel
                if ord(liste_input[index_copy]) == 46:
                    isItAreal = True
                myNumber = myNumber + str(liste_input[index_copy])
                # si dernier élément liste break sinon continue
                if index_copy + 1 < len(liste_input):
                    index_copy += 1
                else:
                    index_copy += 1
                    break

            index = copy.deepcopy(index_copy)
        # elif ord(liste_input[index]) in range(48,58):
        #    print(liste_input[index], " est un entier.")
        #    index+=1
        elif ord(liste_input[index]) == 43:
            listeIndexOperateur.append(index)
            index += 1
        elif ord(liste_input[index]) == 42:
            listeIndexOperateur.append(index)
            index += 1
        else:
            index += 1
    return listeIndexOperateur


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
        # checkOrderOperations = checkOperationsOrder(listeParentheses)
        # if checkOrderOperations[0] and checkOrderOperations[1]:
        newListe = transformListe(listeParentheses, [])
        print(newListe)
        arbre = checkNextOp(newListe, arbre)
        arbre.append(arbre[-1].replace("e", ""))
        print(arbre, " hallo marche")
        print(eval(arbre[-1]), " s")
        # else:
        #     print("la formule est non accepte par la grammaire")
