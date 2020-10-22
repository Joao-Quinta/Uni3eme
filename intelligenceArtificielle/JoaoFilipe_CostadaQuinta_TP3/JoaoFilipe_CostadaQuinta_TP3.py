import copy


# fonction d'évaluation, avec les solutions pour chaque état hardcodé
def calculTransitionPossible(etat):
    if etat != "S":
        etat = etat[0]
    listeRes = []
    if etat == "S":
        listeRes.append(["A", 5])
        listeRes.append(["F", 4])
    elif etat == "A":
        listeRes.append(["C", 4])
        listeRes.append(["F", 4])
    elif etat == "F":
        listeRes.append(["A", 5])
        listeRes.append(["H", 2])
        listeRes.append(["G", 0])
    elif etat == "D":
        listeRes.append(["G", 0])
    elif etat == "C":
        listeRes.append(["D", 3])
        listeRes.append(["G", 0])
    elif etat == "H":
        listeRes.append(["F", 4])
    return listeRes


def calculGreedy(res, etatAVisiterX, courant, etatDejaVisite):
    etatAVisiter = copy.deepcopy(etatAVisiterX)
    for j in range(0, len(res)):
        if res[0] not in etatDejaVisite[0]:
            if len(etatAVisiter[0]) == 0:
                etatAVisiter[0].append(res[j])
                etatAVisiter[1].append(courant)
            else:
                i = 0
                while i < len(etatAVisiter[0]):
                    if res[j][1] < etatAVisiter[0][i][1] and i == len(etatAVisiter[0]) - 1:
                        etatAVisiter[0].append(res[j])
                        etatAVisiter[1].append(courant)
                        break
                    elif res[j][1] < etatAVisiter[0][i][1]:
                        i = i + 1
                    else:
                        etatAVisiter[0].insert(i, res[j])
                        etatAVisiter[1].insert(i, courant)
                        break
    return etatAVisiter


def calculSolutionGreedy():
    etatCourant = None
    parentEtatCourant = None
    chemin = "S"
    etatInitial = "S"
    etatFinal = "G"
    etatAVisiter = [[], []]
    etatDejaVisite = [[], []]
    etatCourant = etatInitial
    etatAVisiter[0].append(etatCourant)
    etatAVisiter[1].append([])
    while len(etatAVisiter) > 0:
        etatCourant = etatAVisiter[0].pop()
        print(etatCourant)
        if etatCourant != "S":
            chemin = chemin + " --> " + etatCourant[0]
        parentEtatCourant = etatAVisiter[1].pop()
        if etatCourant != "S" and etatCourant[0] == etatFinal:
            etatDejaVisite[0].append(etatCourant)
            etatDejaVisite[1].append(parentEtatCourant)
            break
        etatDejaVisite[0].append(etatCourant)
        etatDejaVisite[1].append(parentEtatCourant)
        listePossibilites = calculTransitionPossible(etatCourant)
        etatAVisiter = calculGreedy(listePossibilites, etatAVisiter, etatCourant, etatDejaVisite)

    print()
    print("voici l ordre dans lequel les etats ont ete visité :")
    print(chemin)
    print()


calculSolutionGreedy()
