# fonction d'évaluation, avec les solutions pour chaque état hardcodé
def calculTransitionPossible(etat):
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
    return listeRes


def calculGreedy(res):
    if len(res) != 0:
        reponse = res[0][0]
        coutReponse = res[0][1]
        for i in range(1, len(res)):
            if res[i][1] < coutReponse:
                coutReponse = res[i][1]
                reponse = res[i][0]
        return [reponse, coutReponse]
    return None


def calculSolutionGreedy():
    etatCourant = None
    parentEtatCourant = None
    etatInitial = "S"
    etatFinal = "G"
    etatAVisiter = [[], []]
    etatDejaVisite = [[], []]
    etatCourant = etatInitial
    etatAVisiter[0].append(etatCourant)
    etatAVisiter[1].append([])
    while len(etatAVisiter) > 0:
        etatCourant = etatAVisiter[0].pop()
        parentEtatCourant = etatAVisiter[1].pop()
        print("courant : ", etatCourant, " pere : ", parentEtatCourant)
        if etatCourant == etatFinal:
            etatDejaVisite[0].append(etatCourant)
            etatDejaVisite[1].append(parentEtatCourant)
            break
        etatDejaVisite[0].append(etatCourant)
        etatDejaVisite[1].append(parentEtatCourant)
        listePossibilites = calculTransitionPossible(etatCourant)
        etatPossibleMin = calculGreedy(listePossibilites)
        if etatPossibleMin[0] not in etatDejaVisite[0]:
            etatAVisiter[0].append(etatPossibleMin[0])
            etatAVisiter[1].append(etatCourant)

    cheminEtats = []
    etatCourantBacktracking = etatCourant
    parentEtatCourantBacktracking = parentEtatCourant
    while etatCourantBacktracking != etatInitial:
        cheminEtats.insert(0, etatCourantBacktracking)
        etatCourantBacktracking = parentEtatCourantBacktracking
        parentEtatCourantBacktracking = etatDejaVisite[1][etatDejaVisite[0].index(etatCourantBacktracking)]
    cheminEtats.insert(0, etatCourantBacktracking)
    print()
    print("voici le chemin en etat depuis  initial à final :")
    print(cheminEtats)
    print()


calculSolutionGreedy()
