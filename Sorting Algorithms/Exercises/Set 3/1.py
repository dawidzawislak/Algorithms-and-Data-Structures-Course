"""
Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby zawsze używał najwyżej O(log n) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji partition.
"""

def quick_sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q-p < r-q:
            quick_sort(T, p, q-1)
            p = q + 1
        else:
            quick_sort(T, q+1, r)
            r = q - 1

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

T = [1,54,3,634,234,2,423]
quick_sort(T, 0, len(T)-1)

print(T)