"""
Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie |B| = log n. Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.
"""

def map_A(A, B):
    n = len(A)
    lenB = len(B)

    mappedA = [None]*n

    for i in range(n):
        for j in range(lenB):
            if A[i] == B[j]:
                mappedA = j
    
    return mappedA


def counting_sort(T):
    n = len(T)
    counts = [0]*n
    temp = [0]*n

    for i in range(n):
        counts[T[i]] += 1

    for i in range(1, n):
        counts[i] += counts[i-1]
    
    for i in range(n-1, -1, -1):
        counts[T[i]] -= 1
        temp[counts[T[i]]] = T[i]
    
    for i in range(n):
        T[i] = temp[i]

def map_to_A(mappedA, B):
    n = len(mappedA)
    lenB = len(B)
    A = [None]*n

    for i in range(n):
        A[i] = B[mappedA[i]]
    
    return A


        