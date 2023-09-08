# Dana jest tablica T posortowana oraz liczba x
# Szukamy (i, j) takich, że T[i] + T[j] = x

# [|..................|]
#  -> jak za malo
                    # <- jak za dużo

def f(T, x):
    i, j = 0, len(T)-1
    while i < j and T[i] + T[j] != x:
        if T[i] + T[j] < x:
            i += 1
        else:
            j -= 1
    
    if i == j: return None
    return i, j


T = [1,3,8,10,12,15]
print(f(T, 27))