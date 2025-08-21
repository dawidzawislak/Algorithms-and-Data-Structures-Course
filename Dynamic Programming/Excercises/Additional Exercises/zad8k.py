from zad8ktesty import runtests 

def napraw ( s, t ):
    n = len(s)
    m = len(t)

    F = [[float("inf")]*(m) for _ in range(n)]

    if s[0] == t[0]: F[0][0] = 0
    else:
        F[0][0] = 1
        if s[0] != t[1]: F[0][1] = 2
        if s[1] != t[0]: F[1][0] = 2
        
    if s[0] == t[1]: F[0][1] = 1
    if s[1] == t[0]: F[1][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if s[i] == t[j]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i][j-1], F[i-1][j], F[i-1][j-1]) + 1 # dodawanie, usuwanie, zamiana
    
    return F[n-1][m-1]

runtests ( napraw )