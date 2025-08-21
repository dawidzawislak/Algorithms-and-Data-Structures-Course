from zad12ktesty import runtests 
from queue import PriorityQueue

def autostrada( T, k ):
    n = len(T)
    
    F = [[0]*k for _ in range(n)]

    F[0][0] = T[0]
    for i in range(1, n):
        F[i][0] = F[i-1][0] + T[i]

    for ik in range(1, k):
        for i in range(ik, n):
            if i == ik: 
                F[i][ik] = max(T[0:i+1])
                continue
            minmax = float("inf")
            for x in range(1, i-ik+1):
                if max(F[i-x][ik-1], (F[i][0]-F[i-x][0])) < minmax:
                    F[i][ik] = max(F[i-x][ik-1], (F[i][0]-F[i-x][0]))
                    minmax = max(F[i-x][ik-1], (F[i][0]-F[i-x][0]))


    return F[n-1][k-1]

runtests ( autostrada,all_tests=True )