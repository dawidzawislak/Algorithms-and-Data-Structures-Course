# Dijskstra na "zmodyfikowanym" grafie gdzie wagi krawędzi są zlogarytmowane 
# [log(ab) = log(a) + log(b)] log to f. rosnaca => najmniejsza suma da najmniejszy iloczyn
from queue import PriorityQueue
from math import log2

def dijkstra(G, s, t):
    n = len(G)
    distance = [float("inf")]*n
    visited = [False]*n
    parent = [-1]*n

    distance[s] = 0

    pq = PriorityQueue()
    pq.put((0, s))
    
    while not pq.empty():
        _, v = pq.get()
        if v == t: return parent
        for u, d in G[v]:
            d = log2(d)
            if not visited[u] and distance[u] > distance[v] + d:
                distance[u] = distance[v] + d
                parent[u] = v
                pq.put((distance[u], u))
        visited[v] = True
    
    return False


def get_path(G, s, t, parents):
    path = [t]
    while parents[path[-1]] != s: 
        path.append(parents[path[-1]])
    path.append(s)

    return path[::-1]


def f(G, s, t):
    parents = dijkstra(G, s, t)

    if not parents: return None

    path = get_path(G, s, t, parents)

    return path


graph = [[(1, 20), (2, 30)],
         [(0, 20), (3, 12), (4, 11)],
         [(0, 30), (3, 18), (5, 2700)],
         [(1, 12), (2, 18), (8, 22), ],
         [(1, 11), (6, 15)],
         [(2, 2700), (7, 19), (8, 3)],
         [(4, 15), (8, 8)],
         [(5, 19)],
         [(3, 22), (5, 3), (6, 8)]]

u, v = 0, 7

print(f(graph, u, v))