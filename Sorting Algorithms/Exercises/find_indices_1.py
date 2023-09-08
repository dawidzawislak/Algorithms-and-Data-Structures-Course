#T - tablica, x - liczba | Sprawdz czy istneiją indeksy i, j t.ż. T[j] - T[i] = x

def find_ij(T, x):
    i, j = 0, 1
    n = len(T)

    while j < n and T[j] - T[i] != x:
        if T[j] - T[i] > x:
            i += 1
        else:
            j += 1
    
    return (i, j) if j < n else None


T = [1,3,8,10,12,15]
print(find_ij(T, 2))