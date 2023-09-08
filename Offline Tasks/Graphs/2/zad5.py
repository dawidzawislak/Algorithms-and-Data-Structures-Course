# Dawid Zawiślak
# Najpierw przekształcam dane wejściowe G na liste sąsiadów i dodaje do tego grafu ścieżkę łączącą wszystkie osobliwości z wagami krawędzi 0.
# Następnie stosuje algorytm Dijkstry alby odnaleźć najkrótszą ścieżkę pomiedzy wierzchołkami a i b, zwracem jej długość. Gdy połaczenie między nimi nie istnieje zwracam None.
from zad5testy import runtests
from queue import PriorityQueue

def get_distance(G, n, start, end):
    distance = [float("inf")]*n
    visited = [False]*n

    distance[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))
    
    while not pq.empty():
        _, v = pq.get()
        if v == end: return distance[end]
        for d, u in G[v]:
            if not visited[u] and distance[u] > distance[v] + d:
                distance[u] = distance[v] + d
                pq.put((distance[u], u))
        visited[v] = True
    
    return None

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]

    for (u, v, d) in E:
        G[u].append((d, v))
        G[v].append((d, u))
    
    for i in range(len(S)-1):
        G[S[i]].append((0, S[i+1]))
        G[S[i+1]].append((0, S[i]))

    return get_distance(G, n, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )