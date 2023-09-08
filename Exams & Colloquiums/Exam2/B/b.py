# Dawid Zawiślak
# F(i,j) - minimalna suma odległości biurowców z pozycji X[0], . . . , X[i] do przydzielonych im działek, przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y [j]
# F(i,j) = {inf , jeśli i > j
#          {(min po wartościach F(i-1, j') dla j' takich że j' < j) + dystans z i-tego biurowca do j-tej działki  , w.p.p.
# Rozwiązanie ma złożonoość O(nm), ponieważ minumum opisanie we wzorze funkcji również obliczam dynamicznie,
# po ustaleniu wartości dla F(i,j) aktualizuje wynik w tablicy min_for_xminus1, której używam w następnej iteracji do obliczania F dla i+1
# wynik algorytmu to minimum wartości F dla i = n-1 oraz dowolnego j

from egz2btesty import runtests

def parking(X,Y):
    global t
    n = len(X)
    m = len(Y)
    F = [[float("inf")]*m for _ in range(n)]

    def dist(x, y):
        nonlocal X, Y
        return abs(X[x]-Y[y])
    
    min_for_xminus1 = [[float("inf")]*m for _ in range(n)]
    
    for i in range(m):
        F[0][i] = dist(0,i)
        if i > 0: min_for_xminus1[0][i] = min(F[0][i], min_for_xminus1[0][i-1])
        else: min_for_xminus1[0][i] = F[0][i]

    for x in range(1, n):
        for y in range(x, m):
            F[x][y] = min(F[x][y], min_for_xminus1[x-1][y-1] + dist(x, y))
            min_for_xminus1[x][y] = min(F[x][y], min_for_xminus1[x][y-1])


    return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )