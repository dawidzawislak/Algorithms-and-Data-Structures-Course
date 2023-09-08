"""
Proszę rozwiązać dwa następujące zadania:
1. Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania najdłuższego rosnącego podciągu?
2. Na wykładzie podaliśmy algorytm działający w czasie O(n2). Proszę podać algorytm o złożoności O(n log n).
"""

def lcs(A, B):
    n  = len(A)
    m = len(B)

    F = [[0]*(m) for _ in range(n)]

    if A[0] == B[0]: F[0][0] = 1

    if m < 2 or n < 2: return F[0][0]

    for i in range(n):
        if A[i] == B[0]: F[i][0] = 1
    
    for i in range(m):
        if A[0] == B[i]: F[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]: F[i][j] = F[i-1][j-1] + 1
            else: F[i][j] = max(F[i-1][j], F[i][j-1])

    return F[n-1][m-1]

def lis(T):
    T_sorted = sorted(T)

    return lcs(T, T_sorted)

def lower_bound(T, key):
    n = len(T)
    p = 0
    q = n-1
    while p <= q:
        i = (p+q)//2
        if T[i] == key: return i
        elif T[i] < key: p = i+1
        else: q = i-1
    return i

def lis_nlogn(T):
    tab = [T[0]]

    for i in range(1, len(T)):
        if T[i] > tab[-1]: tab.append(T[i])
        else: tab[lower_bound(tab, T[i])] = T[i]

    return len(tab)

T = [2,1,4,5,43,32]

tab = [1,2,4,6,7,8]

print(lis(T))
print(lis_nlogn(T))