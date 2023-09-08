# Algorytm znajdujący min i max używający ~3n/2 porównań
def find_minmax(T):
    n = len(T)
    mi = ma = T[n-1]

    for i in range(1, n, 2):
        x, y = T[i-1], T[i]
        if x > y:
            x, y = y, x
        if x < mi: mi = x
        elif y > ma: ma = x
    
    return mi, ma


T = [2,7,1,3,8,7]
print(find_minmax(T))