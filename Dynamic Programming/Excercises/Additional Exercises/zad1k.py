from zad1ktesty import runtests

def roznica( S ):
    n = len(S)
    F = [0]*n

    F[0] = 1 if S[0] == 0 else -1

    for i in range(1,n):
        if S[i] == "1":
            F[i] = F[i-1]-1
        if S[i] == "0":
            if S[i-1] == "1" and F[i-1] < 0:
                F[i] = 1
            else:
                F[i] = F[i-1]+1

    return -1 if F[n-1] == -n else max(F)

def roznica2( S ):
    n = len(S)
    F = [[0]*n for _ in range(n)]

    for i in range(n):
        if S[i] == "1": F[i][i] = -1
        else: F[i][i] = 1

    for i in range(n):
        for j in range(i+1, n):
            if S[j] == "1":
                F[i][j] = F[i][j-1]-1
            else:
                F[i][j] = F[i][j-1]+1

    maxres = 0
    for i in range(n):
        for j in range(i, n):
            maxres = max(maxres, F[i][j])

    return maxres if maxres > 0 else -1

runtests ( roznica2 )