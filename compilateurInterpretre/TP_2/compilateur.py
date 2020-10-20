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


def checkOrder(ligne, start):
    last = "Op"
    end = "Op"
    if start == 0:
        last = "Int"
        end = "Int"
    i = 0
    print(ligne, len(ligne), int(ligne[0]) % 1)
    while i < len(ligne):
        print(ligne[i], last)
        if ligne[i] in "+*," and last == "Int":
            last = "Op"
            i = i + 1
        elif ligne[i] in "0123456789" and last == "Op":
            j = i + 1
            while j < len(ligne) and ligne[j] in "0123456789":
                j = j + 1
            last = "Int"
            i = j
        else:
            print("probleme !")
    if last == end:
        print(ligne, " ok")
    else:
        print("probleme too")


def checkValid_and_Op(ligne, cote):
    if len(ligne) == 1:
        indice = -1
        if cote:
            indice = 0
        # if checkOrder(ligne[0],indice):

        # return ligne[0][indice]


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    print(lignes)
    for i in range(0, len(lignes)):
        print("E = ", lignes[i])
        listeParentheses = parserP(lignes[i])
        print(listeParentheses)
        checkOrder(listeParentheses[0][0], 1)
        # ope = [0, 0]
        # if listeParentheses[3][0]:
        #     ope[0] = checkValid_and_Op(listeParentheses[0], False)
        # if listeParentheses[3][1]:
        #     ope[1] = checkValid_and_Op(listeParentheses[2], True)
        # print(ope)
