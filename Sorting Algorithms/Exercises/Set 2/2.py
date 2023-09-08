"""
1) Proszę zaimplementować algorytm MergeSort sortujący tablicę, opierający się na złączaniu serii naturalnych.

2) Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].
"""


num_of_inversions = 0

def merge(T, p, q, r):
    global num_of_inversions
    p1 = p
    p2 = q+1

    T_ = []

    while p1 <= q and p2 <= r:
        if T[p1] <= T[p2]:
            T_.append(T[p1])
            p1 += 1
        else:
            T_.append(T[p2])
            p2 += 1
            num_of_inversions += q-p1+1
    
    if p1 <= q:
        T_ += T[p1:q+1]
    elif p2 <= r:
        T_ += T[p2:r+1]

    for i in range(p, r+1):
        T[i] = T_[i-p]


def merge_sort(T, p, q, r):
    if r - p > 1:
        merge_sort(T, p, (p+q)//2, q)
        merge_sort(T, q+1, (r+q+1)//2, r)
    merge(T, p, q, r)


# 2, 1          -> 1
# 3, 1, 2       -> 2
# 3, 4, 1, 2    -> 4

T = [3,4,1,2]
n = len(T)
print(T)
merge_sort(T, 0, (n-1)//2, n-1)
print(T)
print(num_of_inversions)