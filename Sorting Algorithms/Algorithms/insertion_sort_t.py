def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key


T = [123,43,34,567,76,234]
print(T)
insertion_sort(T)
print(T)