from zad3ktesty import runtests

def ksuma( T, k ):
    n = len(T)
    
    F = [float("inf")]*(n)

    for i in range(k):
        F[i] = T[i]

    for i in range(k,n):
        to_add = float("inf")
        for x in range(1, k+1):
            to_add = min(to_add, F[i-x])

        F[i] = T[i] + to_add

    return min(F[n-k:n+1])
    
runtests ( ksuma )