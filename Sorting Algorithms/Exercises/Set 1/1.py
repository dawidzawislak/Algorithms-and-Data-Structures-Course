"""
Proszę zaimplementować jeden ze standardowych algorytmów sortowania tablicy działający w zasie O(n2 ) (np. sortowanie bąbelkowe, sortowanie przez wstawianie, sortowanie przez wybieranie).
"""

def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        
        T[j+1] = key
           

T = [5,4,7,3,21,6]

insertion_sort(T)

print(T)