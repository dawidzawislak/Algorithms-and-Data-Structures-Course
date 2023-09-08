"""
Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn A1, A2, ..., An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący koszt mnożenia przy optymalnym doborze kolejności.
"""

def calculate_cost(A):
    n = len(A)

    F = [[float("inf")]*n for _ in range(n)]

    # Base case
    for i in range(n-1):
        F[i][i] = 0
        F[i][i+1] = A[i][0]*A[i+1][0]*A[i+1][1]
    F[n-1][n-1] = 0

    # Relation
    for l in range(2, n):
        for start in range(n-l):
            for k in range(start, start+l):
                F[start][start+l] = min(F[start][start+l], F[start][k] + F[k+1][start+l] + A[start][0]*A[k+1][0]*A[start+l][1])
    
    return F[0][n-1]

metrices = [(10, 20), (20, 3), (3, 14), (14, 5), (5,8),(8,19),(19,22),(22,3),(3,10),(10,11),(11,100),(100,5)]

print(calculate_cost(metrices))
