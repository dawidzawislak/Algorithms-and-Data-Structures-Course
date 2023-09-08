def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def heapify(T, i, n):
    maxi = i
    l = left(i)
    r = right(i)
    if l < n and T[maxi] < T[l]: maxi = l
    if r < n and T[maxi] < T[r]: maxi = r

    if maxi != i:
        T[maxi], T[i] = T[i], T[maxi]
        heapify(T, maxi, n)


def heap_sort(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, i, n)

    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)

T = [3,65,4,3,2,43,1,43,5,3]
print(T)
heap_sort(T)
print(T)