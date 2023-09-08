"""
Dana jest szachownica A o wymiarach n*n. Szachownica zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
"""

def min_cost(T):
    n = len(T)
    F = [[float("inf")]*n for _ in range(n)]

    # base
    F[0][0] = T[0][0]
    for i in range(1, n):
        F[0][i] = F[0][i-1] + T[0][i]
        F[i][0] = F[i-1][0] + T[i][0]
    
    # relation
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = min(F[i-1][j], F[i][j-1])+T[i][j]
    
    return F[n-1][n-1]

print(min_cost([
    [3, 4, 5, 2, 1],
    [7, 2, 13, 7, 8],
    [3, 1, 4, 1, 5],
    [2, 8, 11, 1, 3],
    [3, 5, 1, 3, 2]
]))