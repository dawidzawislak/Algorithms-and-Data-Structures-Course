"""
Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną niemalejąco tablicę A o rozmiarze n oraz liczbę x i sprawdza, czy x występuje w A. Jeśli tak, to zwraca najmniejszy indeks, pod którym x występuje.
"""

def bin_search(A, x):
    n = len(A)
    p = 0
    q = n-1
    while p <= q:
        i = (p+q)//2
        if A[i] == x: return i
        elif A[i] < x: p = i+1
        else: q = i-1
    return None

T = [1,2,2,4,6,7,10]

print(bin_search(T,6))