"""
Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1], [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił się w całości w tam, który spadł tuż przed nim.
"""

def a_ge_then_b(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


def lower_bound(T, key):
    n = len(T)
    p = 0
    q = n-1
    while p <= q:
        i = (p+q)//2
        if T[i] == key: return i
        elif a_ge_then_b(T[i], key): q = i-1
        else: p = i+1
    return i

def lis_nlogn(T):
    n = len(T)
    tab = [T[0]]

    for i in range(1, n):
        if a_ge_then_b(T[i], tab[-1]): tab.append(T[i])
        else: tab[lower_bound(tab, T[i])] = T[i]

    return n-len(tab)

ranges = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]

print(lis_nlogn(ranges))