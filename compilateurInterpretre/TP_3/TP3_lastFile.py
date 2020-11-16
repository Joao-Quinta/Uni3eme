'''
Compilateurs et interprètes TP_2
Travail développé par:
Joao Quinta
Edin Sulejmani
'''

import copy


def checkIfValidExpression(expression):
    # liste_input = list(input())
    # print(liste_input)
    isThereAnErrorInExpression = False
    listeIndexHashtag = []
    listeIndexEgal = []
    listeIndexEspace = []
    compteurHashtag = 0
    compteurParenthese = 0
    index = 0
    listeIndexOperateur = []
    debutFinString = [34, 39, 44, 96, 8216, 8217]  # " ' ‘
    multiAddSpaceEqual = [32, 42, 43, 61]
    while index < len(expression):
        # for element in liste_input:
        if (ord(expression[index]) in range(65, 91)) or (ord(expression[index]) in range(97, 123)) or (
                ord(expression[index]) in debutFinString):
            isItAString = False
            isThereAnErrorInVariable = False
            isItTheEndOfListe = False
            compteurDebutFinString = 0
            if ord(expression[index]) in debutFinString:
                compteurDebutFinString += 1
                isItAString = True
            if index + 1 >= len(expression):
                isItTheEndOfListe = True
                index_copy = copy.deepcopy(index)
            else:
                index_copy = copy.deepcopy(index) + 1
            myString = str(expression[index])
            myVar = str(expression[index])
            # variable
            if not isItAString:
                while (ord(expression[index_copy]) in range(65, 91)) or (
                        ord(expression[index_copy]) in range(97, 123)) or ord(expression[index_copy]) in range(48,
                                                                                                               58):
                    # 1 nombre dans liste, break tout de suite
                    if isItTheEndOfListe:
                        index_copy += 1
                        break
                    myVar = myVar + str(expression[index_copy])

                    if index_copy + 1 < len(expression):
                        index_copy += 1
                    else:
                        index_copy += 1
                        break

            else:
                isThereErrorAfterString = False
                while (ord(expression[index_copy]) in range(65, 91)) or (
                        ord(expression[index_copy]) in range(97, 123)) or (
                        ord(expression[index_copy]) in debutFinString) or (
                        ord(expression[index_copy]) in range(48, 58)):
                    # si on a un élément après le string -> error : exemple : 'abcd'6
                    if compteurDebutFinString >= 2:
                        isThereErrorAfterString = True
                    # si on trouve le 2ème guillemet pour fermer le string, on l'indique
                    if ord(expression[index_copy]) in debutFinString:
                        compteurDebutFinString += 1

                    myString = myString + str(expression[index_copy])
                    if index_copy + 1 != len(expression):
                        index_copy += 1
                    else:
                        index_copy += 1
                        break
                # si le string n'est pas fermée on l'indique
                if compteurDebutFinString < 2 or isThereErrorAfterString:
                    isThereAnErrorInExpression = True
                    # print(myString, " : erreur string non fermée")
                else:
                    pass
            index = copy.deepcopy(index_copy)
        # space
        elif ord(expression[index]) == 32:
            # print("space")
            listeIndexEspace.append(index)
            index += 1
        # numbers, real, negatifs
        elif ord(expression[index]) == 45 or ord(expression[index]) in range(48, 58):
            startsWithNegation = False
            isItTheEndOfListe = False
            isThereAnErrorInVariable = False
            if ord(expression[index]) == 45:
                startsWithNegation = True
            isItAreal = False
            if index + 1 >= len(expression):
                isItTheEndOfListe = True
                index_copy = copy.deepcopy(index)
            else:
                index_copy = copy.deepcopy(index) + 1
            myNumber = str(expression[index])
            while ord(expression[index_copy]) in range(48, 58) or ord(expression[index_copy]) == 46 or (
                    ord(expression[index_copy]) in range(65, 91)) or (
                    ord(expression[index_copy]) in range(97, 123)) or (ord(expression[index_copy]) in debutFinString):

                if (ord(expression[index_copy]) in range(65, 91)) or (
                        ord(expression[index_copy]) in range(97, 123)) or (
                        ord(expression[index_copy]) in debutFinString):
                    isThereAnErrorInVariable = True

                # 1 nombre dans liste, break tout de suite
                if isItTheEndOfListe:
                    index_copy += 1
                    break
                # si possède un '.' -> réel
                if ord(expression[index_copy]) == 46:
                    isItAreal = True
                myNumber = myNumber + str(expression[index_copy])
                # si dernier élément liste break sinon continue
                if index_copy + 1 < len(expression):
                    index_copy += 1
                else:
                    index_copy += 1
                    break
            if isThereAnErrorInVariable:
                isThereAnErrorInExpression = True

            index = copy.deepcopy(index_copy)
        # pour compter le nombre de variables (#)
        elif ord(expression[index]) == 35:
            compteurHashtag += 1
            listeIndexHashtag.append(index)
            index += 1
        # pour =
        elif ord(expression[index]) == 61:
            listeIndexEgal.append(index)
            index += 1
        # pour "(" et ")"
        elif (ord(expression[index]) in [40, 41]) and (len(listeIndexEspace) > 0):
            compteurParenthese += 1
            index += 1
        # pour éviter l'erreur "++" ou "**"
        elif (ord(expression[index]) in [42, 43]) :
            if index+1 < len(expression):
                if (ord(expression[index + 1])) == (ord(expression[index])):
                    isThereAnErrorInExpression = True
            index += 1
        else:
            # print(expression[index], " est un symbole réservé")
            index += 1
    return compteurHashtag, compteurParenthese, listeIndexHashtag, listeIndexEgal, listeIndexEspace, isThereAnErrorInExpression


# string est une simple string, old est un symbole qu on veut enlever, new, le symbole qui remplavce old
def replaceString(string, old, new):
    index = string.find(old)
    return string[0:index] + new + string[index + 1: len(string)]


def supprimeEpsilon(string):
    return string.replace("e", "")


def supprimeNonTerParenthese(string):
    stringTer = ""
    index = string.find(")")
    if string[0:index].find("G") != -1:
        stringAvant = string[0:index]
        stringApres = string[index:]
        stringAvant = stringAvant.replace("D", "e")
        stringAvant = stringAvant.replace("G", "e")
        return stringAvant + stringApres
    else:
        return string[0:index + 1] + supprimeNonTerParenthese(string[index + 1:])


# utilise par developpeE pour faire tache (1)
def supprimeNonTer(string):
    for i in range(0, len(string)):
        if string[i] in "GD":
            string = string[0:i] + "e" + string[i + 1: len(string)]
    return string


# recoit tout l arbre, commence par "chasser" le premier E :
# (1) suprime les non remineaux avant le E
# (2)transforme le E en TD et finalement le T en FG
def developpeE(arbreEntier):
    for i in range(0, len(arbreEntier[-1])):
        if arbreEntier[-1][i] == "E":
            preE = supprimeNonTer(arbreEntier[-1][0:i])
            if preE != '':
                arbreEntier.append(preE + arbreEntier[-1][i:len(arbreEntier[-1])])
                if arbreEntier[-1] == arbreEntier[-2]:
                    arbreEntier.pop()
            arbreEntier.append(arbreEntier[-1][0:i] + "TD" + arbreEntier[-1][i + 1:len(arbreEntier[-1])])
            arbreEntier.append(arbreEntier[-1][0:i] + "FG" + arbreEntier[-1][i + 1:len(arbreEntier[-1])])
            return arbreEntier
    return arbreEntier


# (1) retourne le reste de la fomrule apres le premier non terminal (2) retourne aussi "D" pour dire que c est une
# somme, "G" une multiplication, "(" parenthese, ou alors, le chiffre en question
def getFirstTerminal(formule):
    if formule[0] == "+":
        return formule[1:len(formule)], "D"
    elif formule[0] == "*":
        return formule[1:len(formule)], "G"
    elif formule[0] == "(":
        return formule, "("
    else:
        for i in range(1, len(formule)):
            if formule[i] in "+*":
                return formule[i:len(formule)], formule[0:i]
        return formule[len(formule):len(formule)], formule


# 2+22+(2+2)+2
def findParenthese(formule):
    count = 0
    for i in range(0, len(formule)):
        if formule[i] == "(":
            count = count + 1
        elif formule[i] == ")" and count == 1:
            return formule[i + 1:], formule[1:i]
        elif formule[i] == ")":
            count = count - 1
    return None


def evaluation(formule, dico):
    #print("dico", dico)
    #print(formule)
    #print(dico)
    if len(dico) != 0:
        for value in dico:
            formule = formule.replace(value, dico.get(value))
        result = eval(formule)
    else:
        result = eval(formule)
    #print(formule)
    print("EVALUATION : ", result)
    print("")

def test(expression, compteurHashtag, listeIndexHashtag, listeIndexEspace, arbre):
    index1 = 0
    for hashtag in range(compteurHashtag):
        if hashtag != compteurHashtag - 1:
            arbre.append(
                arbre[-1].replace("DECLVAR", str(expression[listeIndexHashtag[index1]:listeIndexEspace[index1]])))
            arbre.append(arbre[-1].replace("LISTVAR", "DECLVAR LISTVAR"))
        else:
            arbre.append(
                arbre[-1].replace("DECLVAR", str(expression[listeIndexHashtag[index1]:listeIndexEspace[index1]])))
        index1 += 1
    if 'LISTVAR' in arbre[-1]:
        arbre.append(arbre[-1].replace("LISTVAR", "e"))
    if 'FORM' in arbre[-1]:
        arbre.append(arbre[-1].replace("FORM", "E"))

    return arbre


def main(formule, arbreDerivation):
    compteurHashtag, compteurParenthese, listeIndexHashtag, listeIndexEgal, listeIndexEspace, isThereAnErrorInExpression = checkIfValidExpression(
        formule)

    if len(arbreDerivation) == 0:
        arbreDerivation = developpeE(["E"])
    while len(formule) > 0:
        formule, firstTerminal = getFirstTerminal(formule)
        if firstTerminal == "D":
            arbreDerivation.append(replaceString(arbreDerivation[-1], "D", "+E"))
            arbreDerivation = developpeE(arbreDerivation)
        elif firstTerminal == "G":
            arbreDerivation.append(replaceString(arbreDerivation[-1], "G", "*E"))
            arbreDerivation = developpeE(arbreDerivation)
        elif firstTerminal == "(":
            arbreDerivation.append(replaceString(arbreDerivation[-1], "F", "(E)"))
            arbreDerivation = developpeE(arbreDerivation)
            formule, formuleParenthese = findParenthese(formule)
            arbreDerivation = main(formuleParenthese, arbreDerivation)
        else:
            arbreDerivation.append(replaceString(arbreDerivation[-1], "F", firstTerminal))
    arbreDerivation.append(supprimeNonTerParenthese(arbreDerivation[-1]))
    return arbreDerivation


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    #print("lignes", lignes)
    for i in range(0, len(lignes)):
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    listeDeDictVariable = []
    for i in range(0, len(lignes)):
        print(lignes[i])
        compteurHashtag, compteurParenthese, listeIndexHashtag, listeIndexEgal, listeIndexEspace, isThereAnErrorInExpression = checkIfValidExpression(
            lignes[i])
        if (not isThereAnErrorInExpression) and (compteurParenthese %2 == 0):
            arbre = []
            dictVariable = dict()
            if compteurHashtag != 0:

                arbre.append('PROG')
                arbre.append('LISTVAR FORM')
                arbre.append('DECLVAR LISTVAR FORM')
                arbre = test(lignes[i], compteurHashtag, listeIndexHashtag, listeIndexEspace, arbre)

                index = 0
                # récupère les variables dans un dictionnaire
                for hashtag in range(compteurHashtag):
                    dictVariable[str(lignes[i][listeIndexHashtag[index] + 1:listeIndexEgal[index]])] = lignes[i][
                                                                                                       listeIndexEgal[
                                                                                                           index] + 1:
                                                                                                       listeIndexEspace[
                                                                                                           index]]
                    index += 1
                listeDeDictVariable.append(dictVariable)
            else:
                arbre.append('PROG')
                arbre.append('LISTVAR FORM')
                if 'LISTVAR' in arbre[-1]:
                    arbre.append(arbre[-1].replace("LISTVAR", "e"))
                if 'FORM' in arbre[-1]:
                    arbre.append(arbre[-1].replace("FORM", "E"))
            if compteurHashtag != 0:
                expression = lignes[i][listeIndexEspace[-1] + 1:len(lignes[i])]
            else:
                expression = lignes[i]
            beforeFORM = arbre[-1][0:len(arbre[-1]) - 1]
            indexBeforeFORM = len(arbre)
            x = main(expression, [])
            arbre.pop()
            for i in range(len(x)):
                arbre.append(beforeFORM + x[i])
            arbre.append(supprimeNonTer(arbre[-1]))
            arbre.append(supprimeEpsilon(arbre[-1]))
            print(arbre)
            evaluation(expression, dictVariable)
        else:
            print("there is an error in :", lignes[i])
            print("")
            pass