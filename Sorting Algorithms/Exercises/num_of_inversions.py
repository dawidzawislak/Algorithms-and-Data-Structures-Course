# Dana jest tablica T. Szukamy ilosci par (i, j), t.że i < j oraz T[i] > T[j]
# 2, 1          -> 1
# 3, 1, 2       -> 2
# 3, 4, 1, 2    -> 4

# optymalnia złożoność O(nlogn)

T = [3, 4, 1, 2]

cnt = 0

def merge(T, beg, end, mid):
    global cnt
    p = beg
    q = mid+1
    T_ = []

    while p <= mid and q <= end:
        if T[p] <= T[q]:
            T_.append(T[p])
            p += 1
            
        elif T[p] > T[q]:
            T_.append(T[q])
            q += 1
            cnt += mid-p+1
            
    if p <= mid:
        T_ += T[p:mid+1]
    elif q <= end:
        T_ += T[q:end+1]

    for i in range(beg, end+1):
        T[i] = T_[i-beg]


def merge_sort(T, beg, end, mid):
    if end - beg > 1:
        merge_sort(T, beg, mid, (beg+mid)//2)
        merge_sort(T, mid+1, end, (end+mid+1)//2)
    merge(T, beg, end, mid)

merge_sort(T, 0, len(T)-1, (len(T)-1)//2)

print(cnt)