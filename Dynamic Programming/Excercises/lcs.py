"""
Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2)).
"""

def LCS(A, B):
    n = len(A)
    m = len(B)

    L = [[0]*(m+1) for _ in range(n+1)]
    par = [[(None, None)]*(m+1) for _ in range(n+1)]

    #rel
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):

            if A[i] == B[j]:
                L[i][j] = L[i+1][j+1] + 1
                par[i][j] = (i+1, j+1)
            else:
                par[i][j] = (i+1, j)
                L[i][j] =L[i+1][j]
                if L[i][j+1] > L[i][j]:
                    L[i][j] = L[i][j+1]
                    par[i][j] = (i, j+1)
    
    
    path = []
    ptr = (0,0)
    while par[ptr[0]][ptr[1]][0] != None and par[ptr[0]][ptr[1]][1] != None:
        parent = par[ptr[0]][ptr[1]]
        if L[ptr[0]][ptr[1]] > L[parent[0]][parent[1]]:
            path.append(A[ptr[0]])
        ptr = parent

    #org
    return L[0][0], path

print(LCS("HIEROGLYPHOLOGY", "MICHAELANGELO"))

"""
Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2)).
"""

def LCS2(A, B):
    n = len(A)
    m = len(B)

    L = [[0]*m for _ in range(n)]

    for i in range(2):
        for j in range(2):
            if A[i] == B[j]: L[i][j] = 1
    
    #rel
    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    #org
    return L[n-1][m-1]

print(LCS2([1,2,3,5,7], [8,1,4,3,5]))
