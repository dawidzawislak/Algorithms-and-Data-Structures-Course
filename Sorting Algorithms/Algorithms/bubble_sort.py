def bubble_sort(T):
    n = len(T)
    for i in range(n-1):
        for j in range(i+1, n):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]


T = [6,3,2,8,6765,34,1]
print(T)
bubble_sort(T)
print(T)