# Dawid Zawiślak
# W rozwiązaniu zadania używam algorytmu, który w liniowym czasie(zależnym od długości przedziału p) znajduję wartość która byłaby na k-tej pozycji w posortowanej malejąco tablicy.
# Do funkcji przekazuję kolejno kopie tablicy odpowiadające przedziałom indeksów [i, i+p-1] domknięte i wyciągam z nich k-te wartości w klejnosci malejącej.
# Realizuje to za pomocą zmodyfikowanego algorytmu quick sort, który wywołuje się w pętli dopuki wyznaczony przez funkcje partiton pivot nie bedzię równy danemu kluczowi(key),
# ograniczając zmienne p i r(początku i konca analizowanych indeksów tablicy). Funkcja ta przerzuca wartosci wieksze od wartosci pivota na lewo a mniejsze na prawo.
# Kończy działanie gdy wokój danego key juz wszystkie dane są po poprawnej stronie i zwraca wartość znajdującą się w tablicy na tej pozycji.
# Wykonuje to w pętli dla i <= n-p
# Dodaje do zmiennej suma kolejne wyciągane wartości z funkcji select i zwracam jej wartość po wykonaniu algorytmu.
# Złożoność obliczeniową programu szacuje na O(n*p)
from kol1testy import runtests

def select(T, key, p, r):
    while p <= r:
        q = partition(T, p, r)
        if key == q: return T[q]
        elif key < q: r = q-1
        else: p = q+1

def qs(T,p,r):
    if p < r:
        q = partition(T, p, r)
        qs(T, p, q-1)
        qs(T, q+1, r)

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p,r):
        if T[j] >= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def ksum(T, k, p):
    n = len(T)
    suma = 0
    for i in range(0, n-p+1):
        suma += select(T[i:i+p], k-1, 0, p-1)

    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
