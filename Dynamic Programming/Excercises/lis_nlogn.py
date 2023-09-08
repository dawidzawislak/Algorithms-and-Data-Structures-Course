"Najdłuższy rosnący podciąg w A - O(nlogn)"

def lower_bound(T, key):
    i, j = 0, len(T)-1
    while i <= j:
        p = (i+j)//2
        if T[p] == key: return p
        if T[p] > key:  
            j = p-1
        else:
            i = p+1
    return i

def lis(T):
    n = len(T)

    temp = [T[0]]
    for i in range(1, n):
        if T[i] > temp[-1]:
            temp.append(T[i])
        else:
            ind = lower_bound(temp, T[i])
            temp[ind] = T[i]
    
    return len(temp)
        

print(lis([1,7,8,4,5,6,-1,9]))
