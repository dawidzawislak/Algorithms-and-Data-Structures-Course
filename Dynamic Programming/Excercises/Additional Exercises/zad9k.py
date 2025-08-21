from zad9ktesty import runtests
from math import inf

def f(A, L, up,down):
    n = len(A)
    F = [[[False]*(up+1) for _ in range(down+1)] for _ in range(n)] # f(i,d,u)
    
    if down >= A[0]:
        F[0][down-A[0]][up] = True
    if up >= A[0]:
        F[0][down][up-A[0]] = True

    for i in range(1, n):
        for d in range(down+1):
            for u in range(up+1):
                if d + A[i] <= down:
                    F[i][d][u] = F[i-1][d+A[i]][u]
                if u + A[i] <= up:
                    F[i][d][u] = F[i][d][u] or F[i-1][d][u+A[i]]

    mini = None
    mind = minu = float("inf")

    for d in range(down, -1, -1):
        for u in range(up, -1, -1):
            for i in range(n):
                if F[i][d][u] and mind+minu > d + u:
                    mind = d
                    minu = u
                    mini = i
    
    return [1,mini]

def prom(P, g, d):
    return f(P, 0, g,d)

runtests ( prom )