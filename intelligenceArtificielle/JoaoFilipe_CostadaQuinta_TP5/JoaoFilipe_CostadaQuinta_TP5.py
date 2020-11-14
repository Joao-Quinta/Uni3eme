import copy

listeRegions = ["CA", "MPLR", "NB", "PACA", "PLCB", "RAA", "V"]
nombreRegions = len(listeRegions)
contraintes = [[0, 1, 0, 0, 1, 1, 0],
               [1, 0, 0, 1, 0, 1, 0],
               [0, 0, 0, 0, 1, 0, 1],
               [0, 1, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 0, 1, 1],
               [1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 0, 1, 1, 0]]
couleurs = ["R", "G", "B"]


def initiateState():  # done
    etat = []
    for i in range(nombreRegions):
        val = listeRegions[i] + "="
        etat.append(val)
    return etat


def retourneHeuristique(etatS, heuristique):  # done
    etatsDone = []
    etatsLeft = []
    for i in range(nombreRegions):
        if etatS[i][-1] == "=":
            etatsLeft.append(listeRegions[i])
        else:
            etatsDone.append(listeRegions[i])

    if heuristique == "5.2":

        listeOrdre = ["NB", "CA", "V", "MPLR", "RAA", "PACA", "PLCB"]
        return listeOrdre[nombreRegions - len(etatsLeft)]

    elif heuristique == "5.3":

        if len(etatsLeft) == nombreRegions:
            return "NB"

        contraintesTotalEtat = []
        for i in range(nombreRegions):
            contraintesTotalEtat.append(couleurs.copy())

        for i in range(len(etatsDone)):
            indexEtat = listeRegions.index(etatsDone[i])
            contrainteEtat = contraintes[indexEtat]
            couleurEnlever = etatS[indexEtat][-1]
            for j in range(len(contrainteEtat)):
                if contrainteEtat[j] == 1:
                    if couleurEnlever in contraintesTotalEtat[j]:
                        contraintesTotalEtat[j].remove(couleurEnlever)

        for i in range(len(etatsDone)):
            indexEtat = listeRegions.index(etatsDone[i])
            contraintesTotalEtat[indexEtat] = couleurs.copy()

        contraintesTotalInt = []
        for i in range(len(contraintesTotalEtat)):
            contraintesTotalInt.append(len(contraintesTotalEtat[i]))

        return listeRegions[contraintesTotalInt.index(min(contraintesTotalInt))]

    elif heuristique == "5.4":

        contraignantTotalInt = []
        for i in range(nombreRegions):
            contraignantTotalInt.append(0)

        for i in range(len(etatsLeft)):
            indexEtat = listeRegions.index(etatsLeft[i])
            contrainteEtat = contraintes[indexEtat]
            for j in range(len(contrainteEtat)):
                if contrainteEtat[j] == 1 and listeRegions[j] not in etatsDone:
                    contraignantTotalInt[j] = contraignantTotalInt[j] + 1

        for i in range(len(etatsDone)):
            contraignantTotalInt[listeRegions.index(etatsDone[i])] = - 1

        return listeRegions[contraignantTotalInt.index(max(contraignantTotalInt))]

    elif heuristique == "5.5":
        bonneRegion = retourneHeuristique(etatS, "5.4")
        indexBonneRegion = listeRegions.index(bonneRegion)
        contraintesBonneRegion = contraintes[indexBonneRegion]

        domaineBase = couleurs.copy()

        for i in range(len(contraintesBonneRegion)):
            if contraintesBonneRegion[i] == 1 and listeRegions[i] in etatsDone:
                couleurVoisin = etatS[i][-1]
                if couleurVoisin in domaineBase:
                    domaineBase.remove(couleurVoisin)

        totalContraintesVoisionsRegion = []
        for i in range(len(domaineBase)):  # je mets une des couleurs
            totalContraintesVoisionsRegion.append(0)

            for j in range(len(contraintesBonneRegion)):
                if contraintesBonneRegion[j] == 1 and listeRegions[j] in etatsLeft:
                    # je regarde mes voisins, s il est pas fait
                    domaineVoisin = couleurs.copy()
                    contraintesVoisionBonneRegion = contraintes[j]

                    for z in range(len(contraintesVoisionBonneRegion)):  # je calcule le domaine du voisin pas fait
                        if contraintesVoisionBonneRegion[z] == 1 and listeRegions[z] in etatsDone:
                            couleurVoisinVoisin = etatS[z][-1]
                            if couleurVoisinVoisin in domaineVoisin:
                                domaineVoisin.remove(couleurVoisinVoisin)
                        elif z == indexBonneRegion:
                            couleurVoisinVoisin = domaineBase[i]
                            if couleurVoisinVoisin in domaineVoisin:
                                domaineVoisin.remove(couleurVoisinVoisin)

                    totalContraintesVoisionsRegion[i] = totalContraintesVoisionsRegion[i] + (
                            len(couleurs) - len(domaineVoisin))

        domaineFinal = []
        while len(domaineBase) > 0:
            indexMin = totalContraintesVoisionsRegion.index(min(totalContraintesVoisionsRegion))
            domaineFinal.append(domaineBase[indexMin])
            domaineBase.pop(indexMin)
            totalContraintesVoisionsRegion.pop(indexMin)

        return bonneRegion, domaineFinal


def getDomaine(region, heuristique):  # done
    return couleurs


def etatFinal(etat):  # done and tested
    for i in range(nombreRegions):
        if etat[i][-1] == "=":
            return False
    return True


def validationEtat(nouveauEtat, index):  # done and tested
    contraintesLocal = contraintes[index]
    for i in range(len(contraintesLocal)):
        if contraintesLocal[i] == 1:
            if nouveauEtat[index][-1] == nouveauEtat[i][-1]:
                return False
    return True


def backtracking(etatS):  # done
    heuristique = "5.2"
    # heuristique = "5.3"
    # heuristique = "5.4"
    # heuristique = "5.5"
    if not etatFinal(etatS):
        if heuristique == "5.5":
            regionChoisi, domaineRegionChoisi = retourneHeuristique(etatS, heuristique)
            indexRegionChoisi = listeRegions.index(regionChoisi)
        else:
            regionChoisi = retourneHeuristique(etatS, heuristique)
            indexRegionChoisi = listeRegions.index(regionChoisi)
            domaineRegionChoisi = getDomaine(regionChoisi, heuristique)
        for i in domaineRegionChoisi:
            nouveauEtat = etatS.copy()
            nouveauEtat[indexRegionChoisi] = nouveauEtat[indexRegionChoisi] + i
            if validationEtat(nouveauEtat, indexRegionChoisi):
                backtracking(nouveauEtat)

    else:
        solution.append(etatS)
        return etatS


solution = []
etatInitial = initiateState()

backtracking(etatInitial)
print()
for i in range(len(solution)):
    print(solution[i])
