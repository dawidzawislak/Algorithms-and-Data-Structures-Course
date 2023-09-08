"""
Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.
"""

def f(A, T):
    n = len(A)
    # f(i,b) = max zysk po rozpatrzeniu i przedmiotów oraz gdy w plecaku jest zajęte b miejsca
    F = [[False]*(T+1) for _ in range(n)]

    # base case
    F[0][0] = True
    if A[0] <= T:
        F[0][A[0]] = True

    # relation
    for i in range(1, n):
        for b in range(T+1):
            if F[i-1][b]:
                F[i][b] = True

                if b+A[i] <= T:
                    F[i][b+A[i]] = True
    
    # original
    return F[n-1][T]

A = [12,4,4,2,2]

T = 15

print(f(A, T))