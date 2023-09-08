"""
Zadanie 4. (mnożenie macierzy) Dany jest cięg macierzy A1 , A2 , . . . , An . Ktoś chce policzyć iloczyn
A1 A2 ⋯An . Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejności.
"""
n = 5
F = [[float("inf")]*n for _ in range(n)]

def cost(A):
    n = len(A)
    if n < 2: return 0
    
    F = [[float("inf")]*n for _ in range(n)]

    for i in range(n):
        F[i][i] = 0
    
    for i in range(n-1):
        F[i][i+1] = A[i][0] * A[i][1] * A[i+1][1]
    
    for l in range(2, n):
        for i in range(n-l):
            minc = F[i][i+l]
            for k in range(i, i+l):
                minc = min(minc, F[i][k]+F[k+1][i+l]+A[i][0]*A[k][1]*A[i+l][1])
            F[i][i+l] = minc

    print(*F, sep="\n")
    return F[0][n-1]


A = [(2, 3), (3, 7), (7, 10), (10, 4)]
print(cost(A))

