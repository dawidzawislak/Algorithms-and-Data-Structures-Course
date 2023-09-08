def count_sort(T, k):
    n = len(T)

    counts = [0]*(k+1)
    A = [None]*n

    for v in T:
        counts[v] += 1
    
    for i in range(1, k+1):
        counts[i] += counts[i-1]

    for i in range(n-1, -1, -1):
        counts[T[i]] -= 1
        A[counts[T[i]]] = T[i]
    
    for i in range(n):
        T[i] = A[i]


T = [7,8,9,4,5,6,12,1,2,3]
print(T)
count_sort(T, max(T))
print(T)


#-- Count sort for ASCI chars -----------------------
def count_sort_chr(T):
    n = len(T)
    
    counts = [0]*26
    A = [None]*n

    for v in T:
        counts[ord(v)-97] += 1
        
    for i in range(1, 26):
        counts[i] += counts[i-1]

    for i in range(n-1, -1, -1):
        index = ord(T[i])-97
        counts[index] -= 1
        A[counts[index]] = T[i]
    
    for i in range(n):
        T[i] = A[i]


T2 = ["f", "a", "e", "r", "c", "b"]
print(T2)
count_sort_chr(T2)
print(T2)