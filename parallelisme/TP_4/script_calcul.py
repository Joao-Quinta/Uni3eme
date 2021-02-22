def timeintosec(listetemps):
    res = []
    for temps in listetemps:
        val = temps[0] * 60 + temps[1]
        res.append(val)
    return res


p = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

tp2k = [[6, 38], [3, 19], [1, 42], [0, 45], [0, 26], [0, 31], [0, 29], [0, 26], [0, 24], [0, 24], [0, 21], [0, 23],
        [0, 20]]

tp3k = [[14, 28], [9, 17], [3, 18], [1, 49], [1, 6], [0, 48], [0, 41], [0, 36], [0, 30], [0, 33], [0, 36], [0, 34],
        [0, 31]]

tp4k = [[26, 28], [10, 36], [6, 16], [3, 33], [1, 56], [1, 35], [1, 27], [0, 50], [0, 48], [0, 50], [0, 48], [0, 45],
        [0, 38]]

tp2ks = timeintosec(tp2k)
tp3ks = timeintosec(tp3k)
tp4ks = timeintosec(tp4k)

print(tp2ks)
print(tp3ks)
print(tp4ks)
