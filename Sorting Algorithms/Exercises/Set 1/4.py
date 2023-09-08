"""
Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.
"""

def minmax(T):
    n = len(T)
    if n == 0: return None
    if n % 2 == 1: 
        mi = ma = T[n-1]
    else: 
        mi = float("inf")
        ma = -float("inf")
    
    for i in range(1, n, 2):
        min_l = T[i-1]
        max_l = T[i]
        if T[i-1] > T[i]: min_l, max_l = max_l, min_l

        mi = min(mi, min_l)
        ma = max(ma, max_l)
    
    return mi, ma
        
print(minmax([1,323,7,10,12,15,16]))

print(float("inf"))