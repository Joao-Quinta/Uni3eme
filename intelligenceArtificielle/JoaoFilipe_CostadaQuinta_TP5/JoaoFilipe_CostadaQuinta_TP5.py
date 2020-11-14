import copy

# definition du probleme, si on veut faire un autre graphe, il suffit de changer ces 5 valeurs et tout marche
listeRegions = ["CA", "MPLR", "NB", "PACA", "PLCB", "RAA", "V"]
firstHeuristique53 = "NB"
nombreRegions = len(listeRegions)

# cette liste est dans l ordre de listesRegions -> la premeire sous liste, est la liste de contraintes de la premeire
# region de la listeRegions
contraintes = [[0, 1, 0, 0, 1, 1, 0],
               [1, 0, 0, 1, 0, 1, 0],
               [0, 0, 0, 0, 1, 0, 1],
               [0, 1, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 0, 1, 1],
               [1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 0, 1, 1, 0]]
couleurs = ["R", "G", "B"]


def initiateState():
    # etat initial est de la forme :
    # ["CA=", "MPLR=", "NB=", "PACA=", "PLCB=", "RAA=", "V="]
    # etat final est de la forme :
    # ["CA=C", "MPLR=C", "NB=C", "PACA=C", "PLCB=C", "RAA=C", "V=C"] -> ou C est une couleur

    etat = []
    for i in range(nombreRegions):
        val = listeRegions[i] + "="
        etat.append(val)
    return etat


def retourneHeuristique(etatS, heuristique):
    # on cree deux listes, une etatsDone -> les etats deja colories, et etatsLeft -> les etats non colories
    # etatsDone + etats Left = totues les regions  -> a tout moment
    etatsDone = []
    etatsLeft = []
    for i in range(nombreRegions):
        if etatS[i][-1] == "=":
            etatsLeft.append(listeRegions[i])
        else:
            etatsDone.append(listeRegions[i])

    if heuristique == "5.2":
        # lheuristique 5.2 est la plus simple, on fait que calculer cb de regions sont coloties
        # ca nous indique cb restent a colorier, et c est la réponse

        listeOrdre = ["NB", "CA", "V", "MPLR", "RAA", "PACA", "PLCB"]
        return listeOrdre[nombreRegions - len(etatsLeft)]

    elif heuristique == "5.3":
        # pour la 5.3 c est plus dur, d abbord on verifie si c'est la premeire, si oui alors c'est NB par defaut

        if len(etatsLeft) == nombreRegions:
            return firstHeuristique53  # "NB"

        # on initialise une liste par zone avc les 3 couleurs
        contraintesTotalEtat = []
        for i in range(nombreRegions):
            contraintesTotalEtat.append(couleurs.copy())

        # on regarde parmis les etats deja colories, sur qui ils imposent des contraintes,
        # en enlevant la couleur de la region colorié au domaine de la region voisine
        for i in range(len(etatsDone)):
            indexEtat = listeRegions.index(etatsDone[i])
            contrainteEtat = contraintes[indexEtat]
            couleurEnlever = etatS[indexEtat][-1]
            for j in range(len(contrainteEtat)):
                if contrainteEtat[j] == 1:
                    if couleurEnlever in contraintesTotalEtat[j]:
                        contraintesTotalEtat[j].remove(couleurEnlever)

        # pour pas qu on donne la mauvaise region, si une region est faite, alors on met sont domaine = couleurs
        # c'est un peu ma facon d eviter que je rechoisisse une regione deja colorie ->
        # il se peut qu une region deja faite ait plus de contraintes qu une non faite
        for i in range(len(etatsDone)):
            indexEtat = listeRegions.index(etatsDone[i])
            contraintesTotalEtat[indexEtat] = couleurs.copy()

        # ici on transofrme ["R" , "G" ] en 2, pour dire que y a plsu que 2 possibilites pour une certaine region
        # on le fait pour toute region, et mtn il suffit de prendre le min
        # vu que les etats sont de base organises par ordre alphabetique dans ma modelisation on a le bon
        # si y a en a 2 qui ont le meme nb de contraitnes
        contraintesTotalInt = []
        for i in range(len(contraintesTotalEtat)):
            contraintesTotalInt.append(len(contraintesTotalEtat[i]))

        # vu que le but est de a chaque fois tenter toute couleur sasns reflechir je le fais
        # mais en soi j ai acces ici au domaine de la region qu on va colorie
        return listeRegions[contraintesTotalInt.index(min(contraintesTotalInt))]

    elif heuristique == "5.4":
        # la 5.4 est un peu plus simple, il suffit de calculer le nb de contraintes qu on implique aux autres zones
        # (non colories)
        contraignantTotalInt = []
        for i in range(nombreRegions):
            contraignantTotalInt.append(0)

        # pour tout element dans etat left, on va chercher son index, et ainsi ses contraintes
        # pour toute contraintes = 1 -> si c ette zone est pas encore colorie, alors notre zone gagne un point de
        # "contraignance"
        for i in range(len(etatsLeft)):
            indexEtat = listeRegions.index(etatsLeft[i])
            contrainteEtat = contraintes[indexEtat]
            for j in range(len(contrainteEtat)):
                if contrainteEtat[j] == 1 and listeRegions[j] not in etatsDone:
                    contraignantTotalInt[j] = contraignantTotalInt[j] + 1

        # juste pour le cas ou toute est 0 -> on transforme les zones faites en -1
        # on evite ainsi les repetitions
        for i in range(len(etatsDone)):
            contraignantTotalInt[listeRegions.index(etatsDone[i])] = - 1

        return listeRegions[contraignantTotalInt.index(max(contraignantTotalInt))]

    elif heuristique == "5.5":
        # la 5.5 est la plus complex, d abbord pour choisir la region on utilise l heuristique 5.4
        bonneRegion = retourneHeuristique(etatS, "5.4")
        indexBonneRegion = listeRegions.index(bonneRegion)
        contraintesBonneRegion = contraintes[indexBonneRegion]

        # une fois qu on a la bonne region on doit chisir les bonnes couleurs
        domaineBase = couleurs.copy()

        # on calcule ici le domaine de base pour la region, en regardant ses voisins, et leurs couleurs
        # pour les enlever de notre propre domaine
        for i in range(len(contraintesBonneRegion)):
            if contraintesBonneRegion[i] == 1 and listeRegions[i] in etatsDone:
                couleurVoisin = etatS[i][-1]
                if couleurVoisin in domaineBase:
                    domaineBase.remove(couleurVoisin)

        # mtn qu on a les coulers, pour chaque couleur on simule qu on la metet on calcule en fait le nb de contraintes
        # que ca fait aux voisins
        # on prend ensuite la couleur qui a fait le moins de contraintes
        # la logique de l algo est explique dans le pdf
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

        # on reorganise le domaine dans l ordre de cotnraintes que ca va imposer croissant
        domaineFinal = []
        while len(domaineBase) > 0:
            indexMin = totalContraintesVoisionsRegion.index(min(totalContraintesVoisionsRegion))
            domaineFinal.append(domaineBase[indexMin])
            domaineBase.pop(indexMin)
            totalContraintesVoisionsRegion.pop(indexMin)

        return bonneRegion, domaineFinal


def getDomaine(region, heuristique):
    # j ai pas compris si on fisait tjrs les couleurs dans l ordre ou aps, mais du coup appart pour 5.5 on "reflchi" pas
    return couleurs


def etatFinal(etat):
    # il suffit de verifier si toute region a une couleur pour savoir si c est final
    # si toute region a une couleur on sait que c est valide, car on a fait le teste en creant le graph (a chaque etape)
    for i in range(nombreRegions):
        if etat[i][-1] == "=":
            return False
    return True


def validationEtat(nouveauEtat, index):
    # on recoit un etat ainsi que l information de la region qu on vient de colorier
    # s il y a un probleme c est avc la nouvelle
    # on regarde avc qui cette zone a des contraintes
    # et on verifie que les regions sont de couleurs differentes
    contraintesLocal = contraintes[index]
    for i in range(len(contraintesLocal)):
        if contraintesLocal[i] == 1:
            if nouveauEtat[index][-1] == nouveauEtat[i][-1]:
                return False
    return True


def backtracking(etatS):
    # choisir l heuristique
    heuristique = "5.2"
    # heuristique = "5.3"
    # heuristique = "5.4"
    # heuristique = "5.5"

    # on verifie si c est un etat final (solution)
    if not etatFinal(etatS):

        # si heuristique = 5.5 le domaine est prefait par la fonction retorune heuristique, donc y a 2 chemins
        if heuristique == "5.5":
            regionChoisi, domaineRegionChoisi = retourneHeuristique(etatS, heuristique)
            indexRegionChoisi = listeRegions.index(regionChoisi)
        else:
            # on choisit une zone grace a l heuristique de la zone
            regionChoisi = retourneHeuristique(etatS, heuristique)
            # on a besoinde l index de la region
            indexRegionChoisi = listeRegions.index(regionChoisi)
            # le domaine est tjrs RED - GREEN - BLUE , car on a pas d heuristique de courleur (sauf pour 5.5)
            domaineRegionChoisi = getDomaine(regionChoisi, heuristique)

        # pour chaque possibilite on tente de mettre la courleur, et on teste si c est possiblie
        for i in domaineRegionChoisi:
            nouveauEtat = etatS.copy()
            # on cree ainsi le nouveau etat
            nouveauEtat[indexRegionChoisi] = nouveauEtat[indexRegionChoisi] + i
            # s il est valide on regait backtracking
            if validationEtat(nouveauEtat, indexRegionChoisi):
                backtracking(nouveauEtat)

    else:
        # si c est solution on met dans la liste globale solution
        solution.append(etatS)
        return etatS


solution = []
etatInitial = initiateState()

backtracking(etatInitial)
print()
for i in range(len(solution)):
    print(solution[i])
