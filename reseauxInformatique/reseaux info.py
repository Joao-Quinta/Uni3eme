import random as rnd
from math import *


def calculMarkov(epsilon, nbfois):
    state = 0
    i = 0
    listeRes = []
    print(state)
    while i<nbfois:
        if len(listeRes) < state + 1:
            listeRes.append(0)
        listeRes[state] = listeRes[state] + 1
        rand = rnd.random()
        if rand>=epsilon:
            state = state + 1
        else:
            state = 0
        i=i+1


    z=0
    listeResProba = []
    while z<len(listeRes):
        listeResProba.append(listeRes[z]/nbfois)
        z=z+1
    print(listeRes)
    print(listeResProba)

calculMarkov(0.6,1000000)