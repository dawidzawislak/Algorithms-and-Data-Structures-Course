"""
Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las składa się z n drzew rosnących na pozycjach 0, . . . , n-1. Dla każdego i ∈ {0, . . . , n-1} znany jest zysk ci, jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu John znajdzie optymalny plan wycinki.
"""

def black_forest(trees):
    n = len(trees)

    F = [-float("inf")]*n

    F[0] = trees[0]
    F[1] = max(trees[0:2])

    for i in range(2, n):
        F[i] = max(F[i-1], F[i-2]+trees[i])
    
    return F[n-1]

print(black_forest([1, 8, 3, 4, 5, 1, 2]))