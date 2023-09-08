"""
Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5)
"""

def min_cnt(T,C):
    F = [float("inf")]*(T+1)

    for c in C:
        if c <= T:
            F[c] = 1

    for i in range(T+1):
        for c in C:
            if i-c >= 0:
                F[i] = min(F[i], F[i-c]+1)
    
    return F[T]

print(min_cnt(19,[2,5]))