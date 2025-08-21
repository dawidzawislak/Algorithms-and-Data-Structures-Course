from zad5ktesty import runtests

def garek ( A ):
    n = len(A)
    F = [[[None]*2 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        F[i][i][0] = 0
        F[i][i][1] = A[i]
    
    for i in range(n-1):
        F[i][i+1][0] = min(A[i:i+2])
        F[i][i+1][1] = max(A[i:i+2])
    
    for l in range(2, n):
        for s in range(n-l):
            for ja in [0,1]:
                if ja == 1:
                    F[s][s+l][1] = max(F[s+1][s+l][0]+A[s], F[s][s+l-1][0]+A[s+l])
                else:
                    F[s][s+l][0] = min(F[s+1][s+l][1], F[s][s+l-1][1])

    return F[0][n-1][1]

runtests ( garek )