from zad10ktesty import runtests
import math

def dywany ( N ):
    print(N)

    F = [float("inf")]*(N+1)
    P = [None]*(N+1)
    
    F[0] = 0
    F[1] = 1

    for i in range(2, N+1):
        x = 1
        xx = 1
        while xx <= i:
            if F[i] > 1+F[i-xx]:
                F[i] = 1+F[i-xx]
                P[i] = i-xx
                
            x += 1
            xx = x*x

    path = []
    par = N
    while P[par] != None:
        path.append(int(math.sqrt(par-P[par])))
        par = P[par]

    return path

runtests(dywany)