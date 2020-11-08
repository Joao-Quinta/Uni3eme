'''
Compilateurs et interprètes TP_2

Travail développé par:
Joao Quinta
Edin Sulejmani
'''

import copy


# string est une simple string, old est un symbole qu on veut enlever, new, le symbole qui remplavce old
def replaceString(string, old, new):
    string1 = ""
    string2 = ""
    for i in range(0, len(string)):
        if string[i] == old:
            string1 = string[0:i]
            string2 = string[i + 1: len(string)]
    return string1 + new + string2


def supprimeEpsilon(string):
    return string.replace("e", "")


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


def evaluation(formule):
    print(eval(formule))


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    for i in range(0, len(lignes)):
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    for i in range(0, len(lignes)):
        print(lignes[i])
        arbre = developpeE(["E"])
        while len(lignes[i]) > 0:
            lignes[i], firstTerminal = getFirstTerminal(lignes[i])
            if firstTerminal == "D":
                arbre.append(replaceString(arbre[-1], "D", "+E"))
                arbre = developpeE(arbre)
            elif firstTerminal == "G":
                arbre.append(replaceString(arbre[-1], "G", "*E"))
                arbre = developpeE(arbre)
            elif firstTerminal == "(":
                pass
            else:
                arbre.append(replaceString(arbre[-1], "F", firstTerminal))
        arbre.append(supprimeNonTer(arbre[-1]))
        arbre.append(supprimeEpsilon(arbre[-1]))
        print(arbre)
        evaluation(arbre[-1])
