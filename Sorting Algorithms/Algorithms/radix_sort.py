def count_sort_num(T, div):
    n = len(T)
    
    counts = [0]*10
    A = [None]*n

    for v in T:
        digit = (v%div) // (div//10)
        counts[digit] += 1
        
    for i in range(1, 10):
        counts[i] += counts[i-1]

    for i in range(n-1, -1, -1):
        digit = (T[i]%div) // (div//10)
        counts[digit] -= 1
        A[counts[digit]] = T[i]
    
    for i in range(n):
        T[i] = A[i]

def radix_num(T, digits_num):
    div = 10
    while div < 10**(digits_num+1):
        count_sort_num(T, div)
        div *= 10


#-- Radix sort for strings -----------------------
def count_sort_chr(T, index):
    n = len(T)
    
    counts = [0]*26
    A = [None]*n

    for v in T:
        counts[ord(v[index])-97] += 1
        
    for i in range(1, 26):
        counts[i] += counts[i-1]

    for i in range(n-1, -1, -1):
        ind = ord(T[i][index])-97
        counts[ind] -= 1
        A[counts[ind]] = T[i]
    
    for i in range(n):
        T[i] = A[i]

def radix_chr(T, n):
    for i in range(n-1, -1, -1):
        count_sort_chr(T, i)

T = [123,432,234,567,876,234]
print(T)
radix_num(T, 3)
print(T)

T2 = ["asd", "vcx","aaa", "bda", "xzd", "ret", "esa"]
print(T2)
radix_chr(T2, 3)
print(T2)