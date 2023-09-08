## QuickSort with Haore's partition
def quick_sort_h(T, p, r):
    if p < r:
        q = partition_h(T, p, r)
        quick_sort_h(T, p, q)
        quick_sort_h(T, q+1, r)

def partition_h(T, p, r):
    piv = T[(p+r)//2]

    lo, hi = p-1, r+1
    while True:
        lo += 1
        while T[lo] < piv:
            lo += 1
        
        hi -= 1
        while T[hi] > piv:
            hi -= 1
        
        if lo < hi:
            T[lo], T[hi] = T[hi], T[lo]
        else:
            return hi
        

### QuickSort with Lemuto's partition
def quick_sort_l(T, p, r):
    if p < r:
        q = partition_l(T, p, r)
        quick_sort_l(T, p, q-1)
        quick_sort_l(T, q+1, r)

def partition_l(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


### Quick for given key
def quick_sort_key_h(T, key, p, r):
    if p < r:
        q = partition_key_h(T, key, p, r)
        quick_sort_key_h(T, key, p, q)
        quick_sort_key_h(T, key, q+1, r)

def partition_key_h(T, key, p, r):
    piv = T[(p+r)//2][key]

    lo, hi = p-1, r+1
    while True:
        lo += 1
        while T[lo][key] < piv:
            lo += 1
        
        hi -= 1
        while T[hi][key] > piv:
            hi -= 1
        
        if lo < hi:
            T[lo], T[hi] = T[hi], T[lo]
        else:
            return hi

T = [(1,3),(65,4),(3,2),(43,43),(5,3)]
print(T)
quick_sort_key_h(T, 1, 0, len(T)-1)
print(T)