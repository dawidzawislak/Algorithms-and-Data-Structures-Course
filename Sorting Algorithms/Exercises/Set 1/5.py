"""
Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.
"""

def find_indices(A, x):
    n = len(A)

    p, q = 0, n-1

    while p < q:
        s = A[p] + A[q]
        if s == x: return p,q
        elif s < x: p += 1
        else: q -= 1
    
    return None

T = [1,3,7,10,12,15]

print(find_indices(T, 19))