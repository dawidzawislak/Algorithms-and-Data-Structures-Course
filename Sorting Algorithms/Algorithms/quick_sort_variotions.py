def quick_sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        print(q)
        if q-p < r-q:
            quick_sort(T, p, q-1)
            p = q + 1
        else:
            quick_sort(T, q+1, r)
            r = q - 1


def quick_sort_iter(T):
    stack = [(0, len(T)-1)]

    while stack:
        p, r = stack.pop()
        q = partition(T, p, r)
        if q > p:
            stack.append((p, q-1))
        if q < r:
            stack.append((q+1, r))


def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p,r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i+1], T[r] = T[r], T[i+1]
    
    return i+1

T = [4,5,6,4,3,7,5,1]
print(T)
quick_sort(T, 0, len(T)-1)
#quick_sort_iter(T)
print(T)