def merge(T, p, q, r):
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


T = [3,2,4,7,6,2,1]
n = len(T)
print(T)
merge_sort(T, 0, (n-1)//2, n-1)
print(T)
