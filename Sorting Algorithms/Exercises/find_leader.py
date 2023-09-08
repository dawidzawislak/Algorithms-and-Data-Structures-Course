# Lider ciągu. 
# Dana jest tablica T i szukamy elementu, który wystepuje w tablicy wiecej niz polowa razy.
# O(n)

def lider(T):
    candidate = T[0]
    count = 1

    for i in range(1, len(T)-1):
        if T[i] == candidate:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            candidate = T[i+1]
            count = 0
    
    c = 0
    for i in range(len(T)):
        if T[i] == candidate: 
            c += 1
        
    if c <= len(T)//2: 
        return None
    return candidate

T = [3, 2, 3,2,2]
print(lider(T))
