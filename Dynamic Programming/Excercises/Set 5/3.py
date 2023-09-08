"""
Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2)).
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

# a = "akcja"
# b = "kaja"

a = [2, 1, 4, 5, 43, 32]
b = [1, 2, 4, 5, 32, 43]

print(lcs(a,b))