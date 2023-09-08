# Przewoźnik chcę przewieźć grupę k turystów z miasta A do miasta B po drodze jest wiele miast i pomiędzy różnymi miastami jężdżą autobusy o różnej pojemnośći
# Dane jest graf w postacji trójek (x, y, z), gdzie x, y to miasta między którymi istneje połączenie, a z to pojemnosc autobusu na tej trasie. Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów, tak aby każda grupa mogła przebyć trasę bez rozdzielania się. Algorytm zwraca na ile najmniej grup musi podzielić turystów(podać trase którą będą jechać **)

# Graf dany w postaci krawędzi

from math import ceil
from queue import PriorityQueue

def CreateGraph(G):
    n = 0
    maxe = 0
    for e in G:
        n = max(n, e[0], e[1])
        maxe = max(maxe, e[2])
    n += 1
    G_ = [[] for _ in range(n)]

    for e in G:
        G_[e[0]].append((e[1], e[2]))
    
    return G_, n, maxe


def f2(G, a, b, k):
    G_, n, maxe = CreateGraph(G)
    visited = [False]*n
    maxc = [0]*n
    parent = [-1]*n

    maxc[a] = float("inf")

    pq = PriorityQueue()
    pq.put((0, a))
    
    while not pq.empty():
        _, v = pq.get()
        for u, c in G_[v]:
            if maxc[u] < min(maxc[v], c):
                maxc[u] = min(maxc[v], c)
                parent[u] = v
                pq.put((maxe-maxc[u], u))
    
    path = [b]
    ptr = b
    while parent[ptr] != a:
        path.append(parent[ptr])
        ptr = parent[ptr]
    path.append(a)
    path.reverse()

    return ceil(k/maxc[b]), path


def f(G, a, b, k):
    G_, n,_ = CreateGraph(G)
    visited = [False]*n
    maxc = [0]*n
    parent = [-1]*n

    def DFSVisit(v):
        nonlocal G_, maxc, parent, visited

        visited[v] = True
        for adj, c in G_[v]:
            if visited[adj] and c <= maxc[adj]: continue
            
            maxc[adj] = c
            parent[adj] = v
            DFSVisit(adj)


    for v in range(n):
        if not visited[v]:
            DFSVisit(v)

    path = [b]
    ptr = b
    while visited[b] and parent[ptr] != a:
        path.append(parent[ptr])
        ptr = parent[ptr]
    path.append(a)
    path.reverse()

    return ceil(k/maxc[b]), path

C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

num_tourists = 100
s = 0
t = 3
print(f2(C, s, t, num_tourists))
print(f(C, s, t, num_tourists))
