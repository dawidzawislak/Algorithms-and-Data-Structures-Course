"""
Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Proszę podać i zaim-
plementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej
wartości T.
"""

def f(A,T):
    n = len(A)
    F = [[0]*(T+1) for _ in range(n)]
    for i in range(n):
        F[i][0] = 1
    F[0][A[0]] = 1
    
    for i in range(1, n):
        for b in range(T+1):
            if F[i-1][b] and b+A[i] <= T:
                F[i][b] = 1
                F[i][b+A[i]] = 1
    
    for i in range(n):
        if F[i][T] == 1: return True
    
    return False

tab = [1,3,5,7,8,10]
print(f(tab, 35))