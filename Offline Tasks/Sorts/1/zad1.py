# Dawid Zawiślak
# Funkcja ceasar( s ) na wejściu otrzymuje napis i zwraca długość najdłuższego zanalezionego w nim palindromu o nieparzystej długości
# Realizuje to w następujący sposób:
# Ustawia wskaźnik środka potencjalnego palindromu na środek napisu, następnie sprawdza kolejno lewą i prawą stronę.
# Zewnętrzne pętle przestawiają wskaźnik środka potencjalnego palindromu(wykonują się dopuki nie będzie już możliwe znalezienie dłuższego palindromu). 
# Wewnątrz sprawdzam czy obrany środek może byc nowym najdłuższym palindromem porównując znaki oddalone od środka o odległość taką jak w najdłuższym palindromie + 1(zmienna off).
# Jeśli się zgadzają sprawdzam znaki na odpowiadających pozycjach zaczynając od obranego środka palindromu. Jeśli znaleziony palindrom okaże się najdłuższy aktualizuje zmienne maxl i off.

# Złożoność obliczeniowa O(n^2)

from zad1testy import runtests

def ceasar( s ):
    n = len(s)

    maxl = 1
    off = 1

    # left side
    i = n // 2
    while i - off >= 0:
        l = 1

        if s[i-off] == s[i+off]:
            if i+1 < n-i:
                lim = i+1
            else:
                lim = n-i
            j = 1
            for j in range(1, lim):
                if s[i+j] == s[i-j]:
                    l += 2
                else:
                    break
        else:
            i -= 1
            continue
        
        if l > maxl:
            maxl = l
            off = (maxl+1) // 2
        
        i -= 1

    # right side
    i = n // 2 + 1
    while i + off < n:
        l = 1

        if s[i-off] == s[i+off]:
            if i+1 < n-i:
                lim = i+1
            else:
                lim = n-i
            j = 1
            for j in range(1, lim):
                if s[i+j] == s[i-j]:
                    l += 2
                else:
                    break
        else:
            i += 1
            continue
        
        if l > maxl:
            maxl = l
            off = (maxl+1) // 2
        
        i += 1

    return maxl

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )