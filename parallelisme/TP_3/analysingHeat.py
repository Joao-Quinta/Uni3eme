with open("chaleur.dat", "r") as f:
    with open("chaleur1.dat", "r") as f1:
        lignes = f.readlines()
        lignes1 = f1.readlines()

        for i in range(len(lignes)):
            for j in range (len(lignes[i])):
                if lignes[i][j] != lignes1[i][j]:
                    print("MERDE")
                    break
        print("done")