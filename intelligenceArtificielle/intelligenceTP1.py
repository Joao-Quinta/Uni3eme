import copy
#salut je suis joao, et je teste un truc
####################################################       EXERCICE 1       ####################################################
# retorune l etat resultat d un transition applique a un etat de depart
def changementEtatExo1(etat,transition):
    return [etat[0]-(transition[2]*transition[0]),etat[1]-(transition[2]*transition[1]),etat[2]+transition[2]]

def liveState(etat):
    mCote = etat[0]
    aCote = etat[1]
    if aCote > mCote > 0:
        print("missionaire dead")
        return False
    elif 3 > mCote > aCote > 0:
        print("missionaire dead")
        return False
    return True

#fonction qui retourne les transitions possibles depuis un état donné, elle vérifie si l'état recu est possible (pas mort de missionaire)
def calculTransitionPossibleExo1(etat):
    listeRes = []
    if liveState(etat):
        if etat[2] == 0:
            mDep,mArr,aDep,aArr,direction = etat[0],3 - etat[0],etat[1],3 - etat[1],1
        else:
            mDep, mArr, aDep, aArr,direction = 3 - etat[0], etat[0], 3 - etat[1], etat[1],-1
        listeRes = []
        if mDep == 0:
            for i in range (1,min(3,aDep+1)):
                listeRes.append([0, i, direction])
        elif mDep == 1:
            listeRes.append([1,0,direction])
            listeRes.append([1,1,direction])
        elif mDep == 2:
            listeRes.append([2, 0, direction])
            listeRes.append([1, 1, direction])
        elif mDep == 3:
            for i in range (1,min(3,aDep+1)):
                listeRes.append([0, i, direction])
            if aDep == 1:
                listeRes.append([2, 0, direction])
            elif aDep == 2:
                listeRes.append([1, 0, direction])
            elif aDep == 3:
                listeRes.append([1, 1, direction])
        return listeRes
    return listeRes

#cette fonction est exactement la même que dans l'exo 3, ou chaque boucle est bien commenté
def calculSolutionExo1():
    etatCourant = []
    parentEtatCourant = []
    etatInitial = [3,3,0]#seule diffèrence avec exo 3, on definit un etat initial et final
    etatFinal = [0,0,1]
    etatAVisister = [[],[]]
    etatDejaVisite = [[], []]
    etatAVisister[0].append(etatInitial.copy())
    etatAVisister[1].append([])
    while len(etatAVisister[0]) > 0:
        etatCourant = etatAVisister[0].pop()
        parentEtatCourant = etatAVisister[1].pop()
        if etatCourant == etatFinal:
            etatDejaVisite[0].append(etatCourant.copy())
            etatDejaVisite[1].append(parentEtatCourant.copy())
            break
        etatDejaVisite[0].append(etatCourant.copy())
        etatDejaVisite[1].append(parentEtatCourant.copy())
        listePossibilites = calculTransitionPossibleExo1(etatCourant)
        listeEtatCalcules = []
        for i in range(0, len(listePossibilites)):
            listeEtatCalcules.append(changementEtatExo1(etatCourant.copy(), listePossibilites[i]))
        for i in range(0, len(listeEtatCalcules)):
            if listeEtatCalcules[i] not in etatDejaVisite[0]:
                etatAVisister[0].append(listeEtatCalcules[i].copy())
                etatAVisister[1].append(etatCourant)
    cheminEtats = []
    etatCourantBacktracking = etatCourant.copy()
    parentEtatCourantBacktracking = parentEtatCourant.copy()
    while etatCourantBacktracking != etatInitial:
        cheminEtats.insert(0,etatCourantBacktracking)
        etatCourantBacktracking = parentEtatCourantBacktracking
        parentEtatCourantBacktracking = etatDejaVisite[1][etatDejaVisite[0].index(etatCourantBacktracking)]
    cheminEtats.insert(0, etatCourantBacktracking)
    print("voici le chemin en etat depuis  inicial à final :")
    print(cheminEtats)
    print()

print()
print("#############################            EXO_1 DEBUT            #############################")
print()
calculSolutionExo1()
print("#############################            EXO_1 END              #############################")
print()

####################################################       EXERCICE 2       ####################################################
# retorune l etat resultat d un transition applique a un etat de depart
def changementEtatExo2(etat,transition):
    etat[transition[1]].append(etat[transition[0]].pop())
    return etat

#fonction qui retourne les transitions possibles depuis un état donné, elle vérifie si l'état recu est possible (pas mort de missionaire)
def calculTransitionPossibleExo2(etat):
    listeRes = []
    for i in range (0,len(etat)):
        if len(etat[i]) != 0:
            x = etat[i][-1]
            for j in range (0,len(etat)):
                if len(etat[j]) == 0 or x < etat[j][-1]:
                    listeRes.append([i, j])
    return listeRes

#cette fonction est exactement la même que dans l'exo 3, ou chaque boucle est bien commenté
def calculSolutionExo2():
    etatCourant = []
    parentEtatCourant = []
    etatInitial = [[3,2,1],[],[]]#seule diffèrence avec exo 3, on definit un etat initial et final
    etatFinal = [[],[],[3,2,1]]
    etatAVisister = [[], []]
    etatDejaVisite = [[], []]
    etatAVisister[0].append(etatInitial.copy())
    etatAVisister[1].append([])
    while len(etatAVisister[0]) > 0:
        etatCourant = etatAVisister[0].pop()
        parentEtatCourant = etatAVisister[1].pop()
        if etatCourant == etatFinal:
            etatDejaVisite[0].append(etatCourant.copy())
            etatDejaVisite[1].append(parentEtatCourant.copy())
            break
        etatDejaVisite[0].append(copy.deepcopy(etatCourant))
        etatDejaVisite[1].append(copy.deepcopy(parentEtatCourant))
        listePossibilites = calculTransitionPossibleExo2(etatCourant)
        listeEtatCalcules = []
        for i in range(0, len(listePossibilites)):
            listeEtatCalcules.append(changementEtatExo2(copy.deepcopy(etatCourant), listePossibilites[i]))
        for i in range(0, len(listeEtatCalcules)):
            if listeEtatCalcules[i] not in etatDejaVisite[0]:
                etatAVisister[0].append(listeEtatCalcules[i].copy())
                etatAVisister[1].append(etatCourant)
    cheminEtats = []
    etatCourantBacktracking = etatCourant.copy()
    parentEtatCourantBacktracking = parentEtatCourant.copy()
    while etatCourantBacktracking != etatInitial:
        cheminEtats.insert(0,etatCourantBacktracking)
        etatCourantBacktracking = parentEtatCourantBacktracking
        parentEtatCourantBacktracking = etatDejaVisite[1][etatDejaVisite[0].index(etatCourantBacktracking)]
    cheminEtats.insert(0, etatCourantBacktracking)
    print("voici le chemin en etat depuis  inicial à final :")
    print(cheminEtats)
    print()


print()
print("#############################            EXO_2 DEBUT            #############################")
print()
calculSolutionExo2()
print("#############################            EXO_2 END              #############################")
print()
####################################################       EXERCICE 3       ####################################################

def calculTransitionPossible(etat):
    return []

def changementEtat(etat,transition):
    return []

def algoRechercheGeneral():
    etatCourant = []
    parentEtatCourant = []
    etatInitial = []#a definir selon probleme
    etatFinal = []#a definir selon probleme
    etatAVisister = [[], []]
    etatDejaVisite = [[], []]

    #on initialise la liste d etats à explorer, on a deux sous listes, la première les eétats, la deuxième les états parents des états à explorer
    #etatAVisiter[0][i] = etat, etatAVisiter[1][i] = le parent de l'état
    etatAVisister[0].append(etatInitial.copy())
    etatAVisister[1].append([])
    while len(etatAVisister[0]) > 0:
        #on défini l'état courant, et son parent
        etatCourant = etatAVisister[0].pop()
        parentEtatCourant = etatAVisister[1].pop()

        #si l'état courant est étal à l'état final, on a fini
        if etatCourant == etatFinal:
            break

        #si c'est pas final, alors on marque l'état courant comme déjà visité, pour pas creer des cycles dans notre exploration
        #on le fait en creeant la liste des etats deja explorés, qui a deux sous listes, la premiere l'état, et dans la deuxième le parent correspondant
        # etatDejaVisite[0][i] = etat, etatDejaVisite[1][i] = le parent de l'état
        etatDejaVisite[0].append(etatCourant.copy())
        etatDejaVisite[1].append(parentEtatCourant.copy())

        #on utilise la fonction qui caalcul les transitions possibles depuis notre etat courant
        listePossibilites = calculTransitionPossible(etatCourant)
        listeEtatCalcules = []

        #pour chaque transition possible on calcule l'état resultant suite à l'application de la transition à notre état courant
        for i in range(0, len(listePossibilites)):
            listeEtatCalcules.append(changementEtat(copy.deepcopy(etatCourant), listePossibilites[i]))

        #pour tout état qu'on peut "trouver" depuis état conrant, on vérifie qu'on l'a pas encore explorer avc un simple if (on évite ainsi les cycles)
        #s il est non visité, alors on le met dans la liste des états qu'on a a explrer, et on stock son parent aussi qui est en fait l'état courant
        for i in range(0, len(listeEtatCalcules)):
            if listeEtatCalcules[i] not in etatDejaVisite[0]:
                etatAVisister[0].append(listeEtatCalcules[i].copy())
                etatAVisister[1].append(etatCourant)

    # c est ou on va stocker le "chemin" d'états depuis l etat initial au final (on fait ici l'étape backtracking)
    cheminEtats = []

    # on initialise etat courant et parent etat courant -> on aurait pu utiliser les memes variables qu avant, c est ujuste pour différencier
    etatCourantBacktracking = etatCourant.copy()
    parentEtatCourantBacktracking = parentEtatCourant.copy()

    # tant que etat courant n esp pas l etat initial, alors on insire dans cheminEtats en position 0 l etat courant,
    # on redefini etat courant comme son parent
    # et on cherche son parent correspondant, il est dans la liste etat deja visite[1], au meme indice que son fils dans etat deja visite[0]
    # d ou l usage de index, le fils est en cheminEtats[0], on indexi cette valeur dans etatdejavisite[0] -> on a un indice,
    # qui correspond à l indice ou se trouve le parent en etatdejavisite[1]
    while etatCourantBacktracking != etatInitial:
        cheminEtats.insert(0,etatCourantBacktracking)
        etatCourantBacktracking = parentEtatCourantBacktracking
        parentEtatCourantBacktracking = etatDejaVisite[1][etatDejaVisite[0].index(etatCourantBacktracking)]

    # manque juste inserer  letat initial
    cheminEtats.insert(0,etatCourantBacktracking)


    # il y a d autres facons de trouver cet "chemin" on aurait put le stocker en entier depuis le debut pour chaque etat visite (le chemin pour atteindre chaque etat)
    # ca serait une solution plus couteuse en memoire, mais moins couteuse en temps, car on aurait directement la solution, tandis que dans ce cas il faut reparcourir des listes pour retrouver
    # dans des cas avec des grands chemins il sera preferable de perdre un petit peu de temps, pour pas perdre bcp de memoire
    print("voici le chemin en etat depuis  inicial à final :")
    print(cheminEtats)
