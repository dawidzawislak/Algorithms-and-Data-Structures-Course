"""
Zadanie 5. (maximin) Rozważmy ciąg (a0 , . . . , an-1 ) liczb naturalnych. Załóżmy, że został podzielony
na k spójnych podciągów: (a0 , . . . , a`1 ), (a`1 +1 , . . . , a`2 ), . . . , (a`k-1 +1 , . . . , an-1 ). Przez wartość i-go podciągu
rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości (roz-
strzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
polega na znalezienie podziału ciągu (a0 , . . . , an-1 ) o maksymalnej wartości.
"""

def f(A, k):
    n = len(A)
    F = [[[0]*(n) for _ in range(n)] for _ in range(k+1)]

    F[1][0][0] = A[0]

    for i in range(1, n):
        for j in range(i, n):
            F[1][i][j] = F[1][i][j-1] + A[i]
    
    for i in range(n):
        for j in range(i, n-1):
            F[2][i][j+1] = min(A[j], A[j+1])

    for k in range(3, k+1):
        for l in range(k, n):
            for i in range(n-l):
                for j in range(i+l, n-l):
                    for t in range(i+1, j):
                        F[k][i][j] = max(F[k-1][i][t], F[k-1][t+1][j])
    
    print(*F, sep="\n")

    return F[k][0][n-1]

A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3
print(f(A, k))