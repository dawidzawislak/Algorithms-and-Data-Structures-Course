# Dawid Zawiślak
# Najpierw przestawiam wyrazy w tablicy, aby każdy wyraz rozpoczynał się od litery będącej wcześniej w alfabecie(co ustawia odwrócone wyrazy w dobrą stronę).
# Następnie sortuje wszystkie wyrazy w tablicy za pomocą algorytmy QuickSort.
# Na końcu przechodzę liniowo po posortowanej tablicy i szukam najdłuższego ciągu tych samych wyrazów.

# Złożoność obliczeniowa: O(N + n*logn)

from zad3testy import runtests

def quickSort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        quickSort(T, p, q)
        quickSort(T, q + 1, r)


def partition(T, p, r):
    pivot = T[p]
    
    l, h = p-1, r+1

    while True:
        l += 1
        while T[l] < pivot:
            l += 1

        h -= 1
        while T[h] > pivot:
            h -= 1

        if l < h: 
            T[l], T[h] = T[h], T[l]
        else:
            return h

def strong_string(T):
    for i in range(len(T)):
        j = 0
        wl = len(T[i])
        while j < wl//2:
            if T[i][j] < T[i][wl-1-j]: break
            elif T[i][j] > T[i][wl-1-j]:
                temp = T[i][::-1]
                T[i] = temp
                break
            j += 1
    

    quickSort(T, 0, len(T)-1)

    maxc = 1
    cnt = 1
    for i in range(1, len(T)):
        if T[i] == T[i-1]:
            cnt += 1
        else:
            if maxc < cnt:
                maxc = cnt
            cnt = 1
    
    if maxc < cnt:
        maxc = cnt

    return maxc

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )