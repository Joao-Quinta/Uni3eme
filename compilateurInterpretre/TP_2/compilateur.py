def parserP(ligne):
    parentheseGauche = False
    parentheseDroite = False
    avantParenthese = 0
    apresParenthese = 0
    indiceParentheseGauche = 0
    indiceParentheseDroite = len(ligne) - 1
    for j in range(0, len(ligne)):
        if ligne[j] == "(":
            indiceParentheseGauche = j
            for z in range(j + 1, len(ligne)):
                p = j + 1 - z
                pp = len(ligne) - 1 - abs(p)
                if ligne[pp] == ")":
                    indiceParentheseDroite = pp

                    break
            break
    if indiceParentheseGauche != 0:
        avantParenthese = ligne[0:indiceParentheseGauche]
        parentheseDroite = True
    elif indiceParentheseDroite != len(ligne) - 1:
        apresParenthese = ligne[indiceParentheseDroite + 1:len(ligne)]
        parentheseGauche = True
    enParenthese = ligne[indiceParentheseGauche + 1:indiceParentheseDroite]

    # CBA
    if indiceParentheseGauche == 0 and indiceParentheseDroite == len(ligne) - 1 and ligne[0] != '(':
        # pas de parenthese dans E
        # enParenthese = E
        return
    else:
        # parenthese dans E
        # avantParenthese is text before first opening parenthese -> 3+(3) will be: avantParenthese = 3+
        # apresParenthese is text after last closing parenthese -> (3)+3 will be: apresParenthese = +3
        # enParenthese is whats between first opening and last closing parenthese -> ((2+2)) will be : en parenthese = (2+2)
        # parentheseDroite = False by default, if its final value is True then : E is of type: (E) + E
        # parentheseGauche = False by default, if its final value is True then : E is of type: E + (E)
        return


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    print(lignes)
    for i in range(0, len(lignes)):
        print("E = ", lignes[i])
        parserP(lignes[i])
