# il manque faire :
# (1) faire les parentheses
# (2) evaluer l equation


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


def checkNextOp(ligne):
    # fonction qui recoit la ligne, detecte la premiere operation, et appelle recursiveConstruction avec les bonnes infos

    # ligne est la ligne de code

    # elle retourne la ligne de code apres l evaluation ->
    # si elle recoit "3+3" -> recursiveConstruction("3","+"), et retorune "3"
    # si elle recoit "3" -> recursiveConstruction("3","over"), et retorune ""
    j = 1
    while j < len(ligne):
        if ligne[j] in "+*(":
            # print("is the number : ", ligne[0:i])
            # print("is the op : ", ligne[i])
            # print("we return this : ", ligne[i + 1:len(ligne)])

            # si ligne = "01234" -> ligne[0:1] = "0"
            recursiveConstruction(ligne[0:j], ligne[j])
            # comme ca on retourne le reste de eval si ligne = "01234" -> ligne[1:len(ligne)] = 1234 (no need len ligne en vrai)
            return ligne[j + 1:len(ligne)]
        # check si c est nombre
        elif ligne[j] in "-0123456789":
            # on garde le - ici pour les nb negatifs
            j = j + 1
            # tant que c est pas une operation, c est un nb, donc on itére
    recursiveConstruction(ligne[0:j], "over")
    return ""


with open("salut.txt", "r") as f:
    lignes = f.readlines()
    for i in range(0, len(lignes)):
        # sil y a plusieurs lignes, alors la fin des lignes cest \n, cette boucle if enleve les \n justement (s il y en a)
        if lignes[i][-1] == "\n":
            lignes[i] = lignes[i][:-1]
    print(lignes)
    for i in range(0, len(lignes)):
        print("E = ", lignes[i])
        string = checkNextOp(lignes[i])
        while len(string) > 0:
            string = checkNextOp(string)
        print("E = ", lignes[i], " -> ")


