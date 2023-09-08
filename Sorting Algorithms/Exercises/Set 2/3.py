"""
Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego górnego rogu i prawego dolnego rogu. 
Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.
"""

def area(t, b):
    return (b[0] - t[0]) * (t[1] - b[1])


def num_of_fully_filled(containers):
    maxh = max(containers, key= lambda x: x[0][1])[0][1]
    x = 21.95

    p = 0
    q = maxh

    while p <= q:
        mid = (p+q)/2

        filled = 0
        for c in containers:
            b = (c[1][0], min(mid, c[1][1]))
            t = (c[0][0], min(mid, c[0][1]))
            filled += area(t,b)

        if filled == x:
            break
        elif filled > x:
            q = mid
        else:
            p = mid


    cnt = 0
    for c in containers:
        if c[0][1] < mid:
            cnt += 1
    
    return cnt


containers = [
    ((0, 2), (1, 0)),
    ((3, 3), (5, 1)),
    ((1, 4), (6, 3)),
    ((7, 5), (8, 2)),
    ((9, 5), (10, 2)),
    ((11, 4), (13, 1)),
    ((2, 9), (4, 5)),
    ((5, 7), (11, 6)),
    ((6, 9), (7, 8)),
    ((8, 9), (9, 8)),
    ((10, 9), (11, 8))
]

print("Cnt: ", num_of_fully_filled(containers))
