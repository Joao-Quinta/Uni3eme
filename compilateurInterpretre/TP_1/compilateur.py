with open("salut.txt", "r") as f:
    lignes = f.readlines()
    #print(lignes)
    for i in range (0,len(lignes)):
        x = lignes[i].split()
        for j in range(0, len(x)):
            #print(x[j][0], " <- this is x[j]")
            if x[j] in ["=","+","*","'"]:
                print(x[j], " est un symbole reserve")
            elif (96 < ord(x[j][0]) < 123) or (64 < ord(x[j][0]) < 91):
                print(x[j], " est une variable")
            elif ord(x[j][0]) == 39 and ord(x[j][0-1]) == 39:
                print(x[j], " est une string")
            else:
                posOrNeg = "positif"
                if x[j][0] == "-":
                    posOrNeg = "negatif"
                reelOrEntier = "entier"
                for z in range (0,len(x[j])):
                    if x[j][z] == ".":
                        reelOrEntier = "reel"
                print(x[j], " est ", reelOrEntier, posOrNeg)