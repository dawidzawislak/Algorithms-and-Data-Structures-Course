# Dawid Zawiślak
# Aby zebrać najwięcej śniegu musimy zebrać śnieg z x największych obszarów, gdzie na najmniejszym z nich znajduje się więcej śniegu niż x(ilość obszarów, czyli ilość dni ile zajmie odśnieżanie). 
# Kolejność ich zbierania nie ma znaczenia, ponieważ w danych x dniach śnieg topnieje po równo na wszystkich wybranych obszarach i nie stopi ich w całości.
#
# Problem rozwiązuje za pomocą zmodyfikowanego algorytmu HeapSort, który na górę kopca odkłada kolejne największe wartości.
# Najpierw tworze kopiec z danych wejściowych, a następnie pobieram wartość max, zamieniam ją na wartość znajdującą się na dole kopca i przywracam strukture kopca(funkcja heapify dla zakresu o 1 mniejszego) - proces powtarzam.
# Kolejne wartości pomniejszone przez ilość stopionego śniegu w danym dniu(zmienna melted) dodaje do zmiennej wynikowej.
# Proces wyszukiwania i pobierania kolejnych maksymalnych wartości kończe gdy kolejna wybrana wartość jest <= od wartości zmiennej melted.
#
# Złożoność obliczeniowa: O(n*logn)

from zad2testy import runtests

def heapify(T, i, n):
    l = 2*i + 1
    r = 2*i + 2
    maxi = i

    if l < n and T[l] > T[maxi]: maxi = l

    if r < n and T[r] > T[maxi]: maxi = r
    
    if maxi != i:
        T[i], T[maxi] = T[maxi], T[i]
        heapify(T, maxi, n)

def snow( S ):
    n = len(S)
    res = 0
    melted = 0

    for i in range((n-2)//2, -1, -1):
        heapify(S, i, n)
    
    for i in range(n-1, 0, -1):
        if S[0] <= melted:
            break
        res += S[0]-melted
        S[0] = S[i]
        heapify(S, 0, i)
        melted += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
