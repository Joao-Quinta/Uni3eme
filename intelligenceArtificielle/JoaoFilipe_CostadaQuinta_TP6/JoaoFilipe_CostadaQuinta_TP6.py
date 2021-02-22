import math


class Node:
    def __init__(self, value, isFinal, isMax, name):
        self.value = value
        self.isFinal = isFinal
        self.isMax = isMax
        self.name = name


def alphabeta(node, alpha, beta):
    if node.isFinal:
        return node.value

    elif not node.isMax:
        value = math.inf
        for fils in node.value:
            value = min(value, alphabeta(fils, alpha, beta))
            if alpha >= value:
                return value
            beta = min(beta, value)

    else:
        value = -math.inf
        for fils in node.value:
            value = max(value, alphabeta(fils, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
    return value


# init nodes
x = False
y = not x
T = Node(-4, True, x, "T")
U = Node(3, True, x, "U")
V = Node(-5, True, x, "V")
W = Node(-2, True, x, "W")
X = Node(6, True, x, "X")
Y = Node(7, True, x, "Y")

H = Node([T, U, V], False, y, "H")
J = Node([W, X, Y], False, y, "J")
K = Node(2, True, y, "K")
L = Node(-1, True, y, "L")
M = Node(-1, True, y, "M")
N = Node(4, True, y, "N")
O = Node(2, True, y, "O")
P = Node(6, True, y, "P")
Q = Node(-5, True, y, "Q")
R = Node(-2, True, y, "R")
S = Node(-2, True, y, "S")

D = Node([H, J], False, x, "D")
E = Node([K, L, M], False, x, "E")
F = Node([N, O, P], False, x, "F")
G = Node([Q, R, S], False, x, "G")

B = Node([D, E], False, y, "B")
C = Node([F, G], False, y, "C")

A = Node([B, C], False, x, "A")

print(alphabeta(A, -math.inf, math.inf))
