"""
Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1 , b1 ],
[a2 , b2 ], . . ., [an , bn ]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim.
"""

def lesser(p1, p2):
    return p1[0] >= p2[0] and p1[1] <= p2[1]

def f(P):
    n = len(P)
    F = [1]*n

    for i in range(1, n):
        for j in range(i):
            if lesser(P[i],P[j]):
                F[i] = max(F[i], F[j]+1)
    
    return n-max(F)

def lower_bound(T, key):
    i, j = 0, len(T)-1
    while i <= j:
        p = (i+j)//2
        if T[p] == key: return p
        if not lesser(T[p], key):
            j = p-1
        else:
            i = p+1
    return i

def f_nlogn(P):
    n = len(P)

    temp = [P[0]]
    for i in range(1, n):
        if not lesser(P[i], temp[-1]):
            temp.append(P[i])
        else:
            ind = lower_bound(temp, P[i])
            temp[ind] = P[i]
    
    return n-len(temp)


print(f([(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]))
print(f_nlogn([(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]))
