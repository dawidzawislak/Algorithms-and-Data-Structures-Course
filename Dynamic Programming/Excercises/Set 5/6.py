"""
Rozważmy ciąg (a0, . . . , an-1) liczb naturalnych. Załóżmy, że został podzielony na k spójnych podciągów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k-1+1, . . . , an-1). Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie polega na znalezienie podziału ciągu (a0, . . . , an-1) o maksymalnej wartości.
"""

def maxmin(T, K):
    n = len(T)
    F = [[-float("inf")]*(K+1) for I in range(n)]

    # base
    F[0][1] = T[0]
    for i in range(1, n):
        F[i][1] = F[i-1][1] + T[i]
    
    # relation
    for k in range(2, K+1):
        for i in range(k-1, n):
            for x in range(k-1, i+1):
                F[i][k] = max(F[i][k], min(F[i][1]-F[x-1][1], F[x-1][k-1]))
        
    
    return F[n-1][K]

tab = [1,3,7,2,13]

print(maxmin(tab, 3))