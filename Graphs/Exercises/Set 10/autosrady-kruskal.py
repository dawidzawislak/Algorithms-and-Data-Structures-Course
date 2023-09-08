"""
Zadanie 5. (autostrady) W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć
wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ
kontynent, na którym leży państwo jest płaski położenie każdego z miast opisują dwie
√ liczby x, y, a odległość
w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len = (x1 − x2 )2 + (y1 − y2 )2 .
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel
postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy auto-
strady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaproponować
algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady."""

from math import sqrt, ceil

def highway(P):
    n = len(P)
    E = []

    for i in range(n-1):
        for j in range(i+1,n):
            E.append((i,j,ceil(sqrt((P[i][0]-P[j][0])**2 + (P[i][1]-P[j][1])**2))))

    def find(x, parent):
        if parent[x] != x: return find(parent[x], parent)
        return x

    def union(x, y, parent, rank):
        x = find(x, parent)
        y = find(y, parent)        

        if x == y: return False

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
        return True
    
    E.sort(key = lambda x: x[2], reverse=True)

    min_time = float("inf")
    p = []

    while True:
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        path = []
        joined = 1
        first = E[len(E)-1][2]
        last = 0
        for i in range(len(E)-1, -1, -1):
            if union(E[i][0], E[i][1], parent, rank):
                joined += 1
                last = E[i][2]
                path.append((P[E[i][0]],P[E[i][1]], E[i][2]))
        
        if joined != n: break

        if min_time > last-first:
            min_time = last-first
            p = path

        E.pop()

    return min_time, p


P = [(4, 4), (2, 3), (4.5, 0), (0, 0), (1, -1), (3, -2), (2, -4), (-1, 2), (-2, -2), (-4, 4), (-5, 0)]

m, p = highway(P)
print(m)
for v in p:
    print(v)