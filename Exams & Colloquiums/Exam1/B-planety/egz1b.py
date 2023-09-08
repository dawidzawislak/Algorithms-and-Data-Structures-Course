from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(D)
    F = [[float("inf")]*(E+1) for _ in range(n)]

    for t in range(E+1):
        F[0][t] = t * C[0]

    if T[0][0]!= 0:
        F[T[0][0]][0] = T[0][1]

    for i in range(1, n):
        dist = D[i]-D[i-1]

        for t in range(E+1):
            if t+dist <= E:
                F[i][t] = min(F[i][t], F[i-1][t+dist])
        
        for t in range(1, E+1):
            F[i][t] = min(F[i][t], F[i][t-1] + C[i])
        
        if T[i][0] != i:
            F[T[i][0]][0] = min(F[T[i][0]][0], F[i][0]+T[i][1])

    #print(*F, sep="\n")
    #input()

    return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
