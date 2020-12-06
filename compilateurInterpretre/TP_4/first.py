import copy
import re
import math

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
        # pour éviter l'erreur "++" ou "**" ou manque d'opérande.
        elif (ord(expression[index]) in [42, 43]):
            liste_num_alphabet = list(range(48, 58))
            liste_num_alphabet.extend(list(range(65, 91)))
            liste_num_alphabet.extend(list(range(97, 123)))
            liste_num_alphabet.append(45)
            if index + 1 < len(expression):
                if (ord(expression[index + 1])) == (ord(expression[index])):
                    isThereAnErrorInExpression = True

                if (ord(expression[index + 1])) == 32:
                    compteurSpace = 0
                    n = 1

                    # compte le nombre d'espace entre l'opérateur et l'opérande, permet d'accepter : i = i +    1; par exemple.
                    while (ord(expression[index + n])) == 32:
                        compteurSpace += 1
                        if index + compteurSpace < len(expression):
                            n += 1
                        else:
                            break
                    # si après tous les espaces on a pas un nombre ou une lettre, -> il manque l'opérande -> erreur
                    if index + n < len(expression):
                        if ord(expression[index + n]) not in liste_num_alphabet:
                            print("test")
                            print(liste_num_alphabet)
                            isThereAnErrorInExpression = True
                # si on a pas d'espace après l'opérateur et qu'on a autre chose qu'un nombre ou une lettre -> erreur
                else:
                    if (ord(expression[index + 1])) not in liste_num_alphabet:
                        isThereAnErrorInExpression = True
            # si on atteint la fin de liste et on a un "+" ou un "*" -> Faux
            else:
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
    return string.replace("ε", "")


def supprimeNonTerParenthese(string):
    stringTer = ""
    index = string.find(")")
    if string[0:index].find("G") != -1:
        stringAvant = string[0:index]
        stringApres = string[index:]
        stringAvant = stringAvant.replace("D", "ε")
        stringAvant = stringAvant.replace("G", "ε")
        return stringAvant + stringApres
    else:
        return string[0:index + 1] + supprimeNonTerParenthese(string[index + 1:])


# utilise par developpeE pour faire tache (1)
def supprimeNonTer(string):
    for i in range(0, len(string)):
        if string[i] in "GD":
            string = string[0:i] + "ε" + string[i + 1: len(string)]
    return string


# recoit tout l arbre, commence par "chasser" le premier E :
# (1) suprime les non remineaux avant le E
# (2)transforme le E en TD et finalement le T en FG
def developpeE(arbreEntier, what):
    if what == "E":
        for i in range(len(arbreEntier[-1])):
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
    else:
        for i in range(len(arbreEntier[-1])):
            if arbreEntier[-1][i] == "T":
                preE = supprimeNonTer(arbreEntier[-1][0:i])
                if preE != '':
                    arbreEntier.append(preE + arbreEntier[-1][i:len(arbreEntier[-1])])
                    if arbreEntier[-1] == arbreEntier[-2]:
                        arbreEntier.pop()
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


def preBoucle(pre):
    dico = {}
    values = pre.split(";")
    for i in range(len(values) - 1):
        variables = values[i].split("=")
        dico[variables[0]] = variables[1]
    return dico, int(values[-1].replace("boucle", ""))


def transform_instructions(pos):
    liste = []
    for ele in pos:
        liste.append(ele.split("="))
    for i in range(len(liste)):
        if len(liste[i]) == 1:
            if "afficher" in liste[i][0]:
                valueAfficher = liste[i][0].replace("afficher", "")
            else:
                valueAfficher = "vide"
            liste[i] = ['print', valueAfficher]
    return liste


def evaluation_small(command, dico):
    real_command = ""
    i = 0
    while i < len(command):
        if command[i] in "+*":
            var = command[0:i]
            if var in dico:
                valeur = dico[var]
            else:
                valeur = var
            real_command = real_command + valeur + command[i]
            command = command[i+1:]
            i = 0
        else:
            i = i + 1
    if command in dico:
        valeur = dico[command]
    else:
        valeur = command
    real_command = real_command + valeur
    return eval(real_command)


def execute_instructions(instructions, dico):
    for instr in instructions:
        #print(instr)
        if instr[0] == "print":
            if instr[1] == "vide":
                print()
            else:
                value = evaluation_small(instr[1], dico)
                print(value)
        else:
            if "inv(" in instr[1]:
                real_ = instr[1].replace("inv(", "")
                real_ = real_.replace(")", "")
                value = 1/evaluation_small(real_, dico)
            elif "racine" in instr[1]:
                real_ = instr[1].replace("racine", "")
                value = math.sqrt(evaluation_small(real_, dico))
            else:
                value = evaluation_small(instr[1], dico)
            dico[instr[0]] = str(value)
    return dico


def evaluation(formule):
    stringSansEspace = arbre[-1].replace(" ", "")
    pre_boucle = stringSansEspace.split("{")
    dico, iterations = preBoucle(pre_boucle[0])
    pos = pre_boucle[1].split(";")
    pos = pos[:-1]
    instru_liste = transform_instructions(pos)
    print(dico)
    print(iterations)
    print(instru_liste)
    print()
    print("BOUCLE START")
    print()
    for i in range(iterations - 1):
        dico = execute_instructions(instru_liste, dico)

    print()


def tp2(formule, arbreDerivation):
    arbreDerivation = developpeE(arbreDerivation, "E")
    # évite d'avoir 2 fois : 'pi = E; LISTINSTR', 'pi = E; LISTINSTR' dans l'arbre final
    arbreDerivation.pop(0)
    while len(formule) > 0:
        formule, firstTerminal = getFirstTerminal(formule)
        if firstTerminal == "D":
            arbreDerivation.append(replaceString(arbreDerivation[-1], "D", "+E"))
            arbreDerivation = developpeE(arbreDerivation, "E")
        elif firstTerminal == "G":
            arbreDerivation.append(replaceString(arbreDerivation[-1], "G", "*T"))
            arbreDerivation = developpeE(arbreDerivation, "T")
        elif firstTerminal == "(":
            arbreDerivation.append(replaceString(arbreDerivation[-1], "F", "(E)"))
            arbreDerivation = developpeE(arbreDerivation, "E")
            formule, formuleParenthese = findParenthese(formule)
            arbreDerivation = tp2(formuleParenthese, arbreDerivation)
        else:
            arbreDerivation.append(replaceString(arbreDerivation[-1], "F", firstTerminal))
    arbreDerivation.append(supprimeNonTerParenthese(arbreDerivation[-1]))
    return arbreDerivation


# retourne le nombre qui suit le mot 'boucle'
def get_nb(instruction):
    '''exemple : "boucle 50" -> retourne "50" '''
    for element in instruction:
        if ord(element) in range(48, 58):
            return instruction[instruction.index(element) - 1:]


def get_id(instruction):
    '''exemple : "pi = 3.141592;" -> retourne "pi" '''
    for element in instruction:
        if ord(element) in range(65, 91) or ord(element) in range(97, 123):
            return instruction[instruction.index(element):instruction.index("=")]


def replaceInstruction(arbre, instruction):
    '''exemple : arbre = ['SCRIPT', 'LISTINSTR', 'INSTR LISTINSTR'], instruction = "pi = 3.141592;"
    retourne ['SCRIPT', 'LISTINSTR', 'INSTR LISTINSTR', 'pi = PD_AFF; LISTINSTR', 'pi = E; LISTINSTR', 'pi = TD; LISTINSTR', 'pi = FGD; LISTINSTR', 'pi = 3.141592GD; LISTINSTR', 'pi = 3.141592εε; LISTINSTR', 'pi = 3.141592εε; LISTINSTR', 'pi = 3.141592; LISTINSTR']
    '''
    # si on a '=' on est forcément dans le cas PD_AFF
    if '=' in instruction:
        id = get_id(instruction)
        arbre.append(re.sub(r"\b%s\b" % "INSTR", str(id) + "= PD_AFF;", arbre[-1]))
        # arbre.append(arbre[-1].replace("\bINSTR\b", "id = PD_AFF;"))

        '''petit problème -> comment différencier : invI4 et inv dans : "invI4 = inv (i*i*i*i);" ?
        du coup ici je demande qu'il y ait une "(" car inv() est une "fonction" qui aura toujours des ()
        et invI4 variable donc jamais de ()
        '''
        if 'inv' in instruction and '(' in instruction:
            arbre.append(re.sub(r"\b%s\b" % "PD_AFF", "inv E", arbre[-1]))
            ###################### on applique TP2 ici pour traduire E ###########################
            arbre.extend(tp2(instruction[instruction.index("("):len(instruction) - 1], [arbre[-1]]))
            arbre.append(supprimeNonTer(arbre[-1]))
            arbre.append(supprimeEpsilon(arbre[-1]))
        elif 'racine' in instruction:
            arbre.append(re.sub(r"\b%s\b" % "PD_AFF", "racine E", arbre[-1]))
            a = re.search(r'\b(racine)\b', instruction)
            ###################### on applique TP2 ici pour traduire E ###########################
            arbre.extend(tp2(instruction[a.end() + 1:len(instruction) - 1], [arbre[-1]]))
            arbre.append(supprimeNonTer(arbre[-1]))
            arbre.append(supprimeEpsilon(arbre[-1]))
        else:
            arbre.append(re.sub(r"\b%s\b" % "PD_AFF", "E", arbre[-1]))
            ###################### on applique TP2 ici pour traduire E ###########################
            arbre.extend(tp2(instruction[instruction.index("=") + 2:len(instruction) - 1], [arbre[-1]]))
            arbre.append(supprimeNonTer(arbre[-1]))
            arbre.append(supprimeEpsilon(arbre[-1]))

    # si on a 'boucle' on est forcément dans la boucle
    elif 'boucle' in instruction:
        nb = get_nb(instruction)
        arbre.append(re.sub(r"\b%s\b" % "INSTR", "boucle" + str(nb) + " { LISTINSTR }", arbre[-1]))

    # si on a 'afficher' on est forcément dans le cas afficher
    elif 'afficher' in instruction:
        arbre.append(re.sub(r"\b%s\b" % "INSTR", "afficher E;", arbre[-1]))
        a = re.search(r'\b(afficher)\b', instruction)
        ###################### on applique TP2 ici pour traduire E ###########################
        arbre.extend(tp2(instruction[a.end() + 1:len(instruction) - 1], [arbre[-1]]))
        arbre.append(supprimeNonTer(arbre[-1]))
        arbre.append(supprimeEpsilon(arbre[-1]))

    # si on a 'aff_ral' on est forcéement dans le cas afficher un retour à la ligne
    elif 'aff_ral' in instruction:
        arbre.append(re.sub(r"\b%s\b" % "INSTR", "aff_ral;", arbre[-1]))

    return arbre


with open("test.txt", "r") as f:
    lignes = f.readlines()
    # print("lignes", lignes)
    for i in range(len(lignes)):
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    arbre = []
    # ajoute la base de la grammaire
    arbre.append('SCRIPT')
    arbre.append('LISTINSTR')
    arbre.append('INSTR LISTINSTR')
    # 1 ligne = 1 instruction
    for index, instruction in enumerate(lignes):
        compteurHashtag, compteurParenthese, listeIndexHashtag, listeIndexEgal, listeIndexEspace, isThereAnErrorInExpression = checkIfValidExpression(
            instruction)
        if isThereAnErrorInExpression:
            pass
        # si on est dans une boucle on skip -> on remplace PAS  "LISTINSTR" par : "INSTR LISTINSTR" mais par ε
        if str(instruction) == "{" or str(instruction) == "}":
            if index == len(lignes) - 1:
                arbre.append(re.sub(r"\b%s\b" % "LISTINSTR", "ε", arbre[-1], 1))
            continue
        if index + 1 < len(lignes):
            if lignes[index + 1] == "}":
                arbre.append(re.sub(r"\b%s\b" % "LISTINSTR", "ε", arbre[-1], 1))

        # on remplace dans l'arbre en fonction de la grammaire
        arbre = replaceInstruction(arbre, instruction)

        # si on arrive à la fin de tout le script on va remplacer tous les LISTINSTR par 'e'
        if (index + 1 == len(lignes) - 1 and lignes[index + 1] == "}") or (index + 1 == len(lignes)):
            arbre.append(re.sub(r"\b%s\b" % "LISTINSTR", "ε", arbre[-1]))
        # sinon on continue a regarder l'instruction suivante
        else:
            arbre.append(re.sub(r"\b%s\b" % "LISTINSTR", "INSTR LISTINSTR", arbre[-1], 1))
    if 'ε' in arbre[-1]:
        arbre.append(re.sub(r"\b%s\b" % "ε", "", arbre[-1], 1))
    print(arbre)
    evaluation(arbre)

    '''arbre = main(lignes[i], [])
    arbre.append(supprimeNonTer(arbre[-1]))
    arbre.append(supprimeEpsilon(arbre[-1]))
    print(arbre)
    evaluation(arbre[-1])
    '''

'''
test = 'inverse de inv'
test.replace('inv', 'ok')
-> 'okerse de ok'
re.sub(r"\b%s\b" % "inv", "ok",test)
-> 'inverse de ok'
'''
