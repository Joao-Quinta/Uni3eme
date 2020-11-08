'''
Compilateurs et interprètes TP_2

Travail développé par:
Joao Quinta
Edin Sulejmani
'''

import copy


# string est une simple string, old est un symbole qu on veut enlever, new, le symbole qui remplavce old
def replaceString(string, old, new):
    index = string.find(old)
    return string[0:index] + new + string[index + 1: len(string)]


def supprimeEpsilon(string):
    return string.replace("e", "")


def supprimeNonTerParenthese(string):
    stringTer = ""
    index = string.find(")")
    if string[0:index].find("G") != -1 or string[0:index].find("G") != -1:
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
    return "", formule[1:len(formule)]


def evaluation(formule):
    print(eval(formule))


def main(formule, arbreDerivation):
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
            # print(arbreDerivation, " pre")
            arbreDerivation = main(formuleParenthese, arbreDerivation)
            # print(arbreDerivation, " post")
        else:
            arbreDerivation.append(replaceString(arbreDerivation[-1], "F", firstTerminal))
    arbreDerivation.append(supprimeNonTerParenthese(arbreDerivation[-1]))
    return arbreDerivation


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    for i in range(0, len(lignes)):
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    for i in range(0, len(lignes)):
        print(lignes[i])
        arbre = main(lignes[i], [])
        arbre.append(supprimeNonTer(arbre[-1]))
        arbre.append(supprimeEpsilon(arbre[-1]))
        print(arbre)
        evaluation(arbre[-1])
