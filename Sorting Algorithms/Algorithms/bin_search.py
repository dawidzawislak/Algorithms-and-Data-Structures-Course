def find(T, k, p, q):
    i = (p+q)//2
    if T[i] == k: return i
    elif T[i] > k: return find(T, k, p, i-1)
    else: return find(T, k, i+1, q)


T = [1,2,3,4,5,6,7,8,9,12,324,456,5675,345345,2342342,242342342]
n = len(T)

print(find(T, 3, 0, n-1))