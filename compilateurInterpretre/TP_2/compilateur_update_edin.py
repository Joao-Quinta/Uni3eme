# il manque faire :
# (1) faire les parentheses
# (2) evaluer l equation

import copy
'''
#333+((2+1)+2) -> ['333','+', '(2+1)', '((2+1)+2)']
def evaluer(expression):
    i = 0
    listeIndiceParentheses = [i for i in range(len(expression)) if "(" in expression[i]]
    while i < len(expression):
        if len(listeIndiceParentheses) != 0:
            print()
'''
def remplacer(listeExpression, expression,aRemplacer) :
    #if expression[0] in expression[1]:
    print("listeExpression",listeExpression)
    if len(listeExpression) == 0:
        return expression
    if listeExpression[1] == "+":
        result = int(listeExpression[0]) + int(listeExpression[2])
    else:
        result = int(listeExpression[0]) * int(listeExpression[2])
    expression = expression.replace(aRemplacer, str(result))
    print("expression",expression)
    return expression


def recursiveConstruction(number, op):
    # fonction qui print les derivations de l arbre selon l opération

    # number est le nombre le plus à gauche ("1234567890-")
    # op est la première opération depuis la gauche ("*+")

    # elle retourne rien pour l instant faudra p-e faire passer l'évaluation par la
    if op == "+":
        print("E -> TD || E -> FGD || E -> ", number, "GD || E -> ", number, "eD || E -> ", number, "e + E")
    elif op == "*":
        print("E -> TD || E -> FGD || E -> ", number, "GD || E -> ", number, " * ED || E -> ", number, " * Ee")
    elif op == "over":
        # "triche" l opération over symboliser quand nous sommes au dernier chiffre de l operation
        print("E -> TD || E -> FGD || E -> ", number, "GD || E -> ", number, "eD || E -> ", number, "ee")
    elif op == "(" or op == ")":
        print("E -> TD || E -> FGD || E -> (", number, ")GD || E -> ", number, "eD || E -> (", number, ")ee")


def checkNextOp(ligne, isThereParenthese):
    # fonction qui recoit la ligne, detecte la premiere operation, et appelle recursiveConstruction avec les bonnes infos

    # ligne est la ligne de code

    # elle retourne la ligne de code apres l evaluation ->
    # si elle recoit "3+3" -> recursiveConstruction("3","+"), et retorune "3"
    # si elle recoit "3" -> recursiveConstruction("3","over"), et retorune ""
    j = 1
    compteurParentheses = 0
    print("ligne", ligne)
    print("len(ligne)",len(ligne))
    while j < len(ligne):
        if ligne[j] in "+*" or compteurParentheses == 2:

            # print("is the number : ", ligne[0:i])
            # print("is the op : ", ligne[i])
            # print("we return this : ", ligne[i + 1:len(ligne)])

            # si ligne = "01234" -> ligne[0:1] = "0"
            #print("ligne[0:j]",ligne[0:j])
            #print("ligne[j + 1:len(ligne)]",ligne[j + 1:len(ligne)])

            if compteurParentheses == 2:
                recursiveConstruction(ligne[1:j], ligne[0])
            else:
                recursiveConstruction(ligne[0:j], ligne[j])
            # comme ca on retourne le reste de eval si ligne = "01234" -> ligne[1:len(ligne)] = 1234 (no need len ligne en vrai)
            return ligne[j + 1:len(ligne)], ligne[0:j], ligne[j]
        # check si c est nombre
        elif ligne[j] in "-0123456789":
            # on garde le - ici pour les nb negatifs
            j = j + 1
            # tant que c est pas une operation, c est un nb, donc on itére

        elif ligne[j] == "(" or ligne[j] == ")":
            compteurParentheses +=1
            j = j + 1

    recursiveConstruction(ligne[0:j], "over")
    return "", ligne[0:j], ""


with open("/Users/edin/Desktop/salut.txt", "r") as f:
    lignes = f.readlines()
    listeKeepTrackParenthesis = []
    listeKeepTrackWOParenthesis = []
    for i in range(len(lignes)):
        # sil y a plusieurs lignes, alors la fin des lignes cest \n, cette boucle if enleve les \n justement (s il y en a)
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    print(lignes)
    for i in range(len(lignes)):
        compteurParentheseColler = 0
        groupeDeParenthese = []
        if "(" and ")" in lignes[i]: # TEST AVEC : E = 333+(((2+1)+2)+2)
            #on garde que l'expression avec parenthèses : ex : (((2+1)+2)+2)
            test = lignes[i][lignes[i].index("("):lignes[i].rindex(")")+1]
            numberOfParentheses = test.count("(")
            compteur = 0
            #on compte combien de parenthèse à la suite on a, ex : (((2+1)+2)+2) ici : 3
            while compteur < len(test):
                if test[compteur] == "(":
                    compteurParentheseColler+=1

                if test[compteur] == ")":
                    groupeDeParenthese.append(compteurParentheseColler)
                    compteurParentheseColler = 0
                compteur+=1
            print("groupeDeParenthese",groupeDeParenthese)
            print("test",test)
            aRemplacerFinal = copy.deepcopy(test)
            #pour chaque groupe on va évaluer les expression
            for groupe in groupeDeParenthese:
                if groupe == 0:
                    pass

                for k in range(groupe):
                    listeForEvaluation = []
                    #on retient que la premiere parenthese du calcul, ici : 2+1
                    firstParentheseNumber = test[test.rindex("(")+1:test.index(")")]
                    #on sauvegarde cette parenthèse qu'on va remplacer, ici : (2+1)
                    aRemplacer = test[test.rindex("("):test.index(")")+1]
                    #index = test.index("(") + compteurIndexParenthese
                    print("firstParentheseNumber",firstParentheseNumber)
                    print("aRemplacer",aRemplacer)
                    print(numberOfParentheses)
                    #on va checker chaque expression dans la parenthèse
                    while len(firstParentheseNumber) > 0:
                        print("test",test)
                        #on retourne l'élément suivant du check, le nombre d'avant l'opération, et le signe, ici : 1, 2, +
                        firstParentheseNumber, number, signe = checkNextOp(firstParentheseNumber,True)
                        #on enregistre le nombre avant l'opération
                        listeForEvaluation.append(number)
                        #on enregistre le signe
                        if signe != "":
                            listeForEvaluation.append(signe)
                        print("firstParentheseNumber, number, signe",firstParentheseNumber, number, signe)
                    #on va évaluer notre parenthèse et la remplacer pour pouvoir évaluer la parenthèse suivante
                    test = remplacer(listeForEvaluation, test,aRemplacer)
                    print("test after = ",test)
                print("aRemplacerFinal",aRemplacerFinal)
                print("lignes[i]",lignes[i])
            #une fois toutes les parenthèses remplacées, on va remplacer le résultat des parenthèses dans la liste principale.
            lignes[i] = lignes[i].replace(str(aRemplacerFinal), test)





        print("lignes", lignes)
        print("E = ", lignes[i])
        string, ok,signe = checkNextOp(lignes[i],False)
        print("string", string)
        print("ok",ok)
        print("signe", signe)

        while len(string) > 0:
            '''
            if "(" and ")" in string:
                #((2+1)+2)
                temp = string.rindex(")")
                stringWOend = string[:temp] + ')'
                stringWOend = checkNextOp(stringWOend,False)
                #stringWOend =  string[:temp].replace("(","",1)
                print("resr",stringWOend)
                print("there are parenthesis")
                listeKeepTrackWOParenthesis.append(stringWOend)
                listeKeepTrackParenthesis.append(string)
                #string = copy.deepcopy(stringWOend)
            '''
            string,ok,signe = checkNextOp(string,False)
            print("string",string)
            print("ok",ok)
            print("signe",signe)
        print("E = ", lignes[i], " -> ")
        print("listeKeepTrackWOParenthesis",listeKeepTrackWOParenthesis)
        print(listeKeepTrackParenthesis)
# def parserP(ligne):
#     if ligne == 0:
#         return [ligne]
#     parentheseGauche = False
#     parentheseDroite = False
#     avantParenthese = 0
#     apresParenthese = 0
#     indiceParentheseGauche = 0
#     indiceParentheseDroite = len(ligne) - 1
#     for j in range(0, len(ligne)):
#         if ligne[j] == "(":
#             indiceParentheseGauche = j
#             i = j + 1
#             while i < len(ligne):
#                 if ligne[i] == ")":
#                     indiceParentheseDroite = i
#                     break
#                 elif ligne[i] == "(":
#                     for z in range(i + 1, len(ligne)):
#                         p = j + 1 - z
#                         pp = len(ligne) - 1 - abs(p)
#                         if ligne[pp] == ")":
#                             indiceParentheseDroite = pp
#                             break
#                     break
#                 i = i + 1
#             break
#     if indiceParentheseGauche != 0:
#         avantParenthese = ligne[0:indiceParentheseGauche]
#         parentheseDroite = True
#     if indiceParentheseDroite != len(ligne) - 1:
#         apresParenthese = ligne[indiceParentheseDroite + 1:len(ligne)]
#         parentheseGauche = True
#     # CBA
#     if indiceParentheseGauche == 0 and indiceParentheseDroite == len(ligne) - 1 and ligne[0] != '(':
#         # pas de parenthese dans E
#         # enParenthese = E
#         enParenthese = ligne
#         return [enParenthese]
#
#     else:
#         enParenthese = ligne[indiceParentheseGauche + 1:indiceParentheseDroite]
#         # parenthese dans E
#         # avantParenthese is text before first opening parenthese -> 3+(3) will be: avantParenthese = 3+
#         # apresParenthese is text after last closing parenthese -> (3)+3 will be: apresParenthese = +3
#         # enParenthese is whats between first opening and last closing parenthese -> ((2+2)) will be : en parenthese = (2+2)
#         # parentheseDroite = False by default, if its final value is True then : E is of type: E + (E)
#         # parentheseGauche = False by default, if its final value is True then : E is of type: (E) + E
#         return [parserP(avantParenthese), parserP(enParenthese), parserP(apresParenthese),
#                 [parentheseDroite, parentheseGauche]]
#
#
# def checkOrder(ligne, start):
#     last = "Op"
#     end = "Op"
#     if start == 0:
#         last = "Int"
#         end = "Int"
#     i = 0
#     while i < len(ligne):
#         if ligne[i] in "+*," and last == "Int":
#             last = "Op"
#             i = i + 1
#         elif ligne[i] in "0123456789" and last == "Op":
#             j = i + 1
#             while j < len(ligne) and ligne[j] in "0123456789":
#                 j = j + 1
#             last = "Int"
#             i = j
#         else:
#             return False
#     if last == end:
#         return True
#     else:
#         return False
#
#
# def checkOpPrio(ligne):
#     return None
#
#
# with open("salut.txt", "r") as f:
#     lignes = f.readlines()
#     for i in range(0, len(lignes)):
#         if lignes[i][-1] == "\n":
#             lignes[i] = lignes[i][:-1]
#     print(lignes)
#
#     for i in range(0, len(lignes)):
#         print("E = ", lignes[i])
#         listeParentheses = parserP(lignes[i])
#         print(listeParentheses)
#         checkOrderOperations = [0, 0]
#         if len(listeParentheses) > 1:
#             if listeParentheses[3][0]:
#                 checkOrderOperations[0] = checkOrder(listeParentheses[0][0], 1)
#                 # if not checkOrderOperations[0]:
#                 #     print("forme non valide ")
#                 #     break
#                 # this check has to e done when continuing next step
#             else:
#                 checkOrderOperations[0] = True
#             if listeParentheses[3][1]:
#                 checkOrderOperations[1] = checkOrder(listeParentheses[2][0], 0)
#                 # if not checkOrderOperations[1]:
#                 #     print("forme non valide ")
#                 #     break
#                 # this check has to e done when continuing next step
#             else:
#                 checkOrderOperations[1] = True
#         else:
#             checkOrderOperations[0] = True
#             checkOrderOperations[1] = True
#
#         if checkOrderOperations[0] and checkOrderOperations[1]:
#             checkOpPrio()
