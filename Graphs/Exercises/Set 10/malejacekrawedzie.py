# O(E logV) - listowa
# O(V^2) - macierzowa

# Graf gęsty ma E rzędu V^3
from queue import PriorityQueue

def f(G, E, s, t):
    E.sort(key=lambda x: x[2], reverse=True)

    print(E)
    prev_w = [float("inf")]*len(G)
    dist = [float("inf")]*len(G)
    dist[s] = 0

    for v,u,w in E:
        if dist[v] < dist[u]:
            if w < prev_w[v] and dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                prev_w[u] = w
        if dist[u] < dist[v]:
            if w < prev_w[u] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev_w[v] = w
    
    return dist[t]


def undirected_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G



E = [(0, 1, 1), (1, 2, 4), (2, 3, 3), (0, 5, 40), (5, 6, 38), (0, 7, 5), (6, 7, 8), (7, 1, 6),
     (7, 2, 16), (6, 2, 23), (6, 8, 35), (5, 4, 30), (8, 4, 20), (8, 3, 15), (4, 3, 80)]

G = undirected_weighted_graph_list(E)
print(len(G))
print(f(G,E, 1, 3))