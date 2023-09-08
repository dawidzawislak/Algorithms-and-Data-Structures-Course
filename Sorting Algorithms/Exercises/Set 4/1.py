"""
Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb ze zbioru 0, . . . , n^2 - 1.
"""
def sort(T):
    n = len(T)
    counts = [0]*n
    temp = [0]*n

    for i in range(n):
        counts[T[i]%n] += 1

    for i in range(1, n):
        counts[i] += counts[i-1]
    
    for i in range(n-1, -1, -1):
        counts[T[i]%n] -= 1
        temp[counts[T[i]%n]] = T[i]
    
    for i in range(n):
        T[i] = temp[i]
    
    counts = [0]*n
    temp = [0]*n

    for i in range(n):
        counts[T[i]//n] += 1

    for i in range(1, n):
        counts[i] += counts[i-1]
    
    for i in range(n-1, -1, -1):
        counts[T[i]//n] -= 1
        temp[counts[T[i]//n]] = T[i]
    
    for i in range(n):
        T[i] = temp[i]

tab = [4,3,2,13,24,1,0]

sort(tab)
print(tab)