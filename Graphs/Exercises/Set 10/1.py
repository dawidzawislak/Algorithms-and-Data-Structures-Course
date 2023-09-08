from queue import PriorityQueue

def create_E(G):
    E = []
    for v, e in enumerate(G):
        for adj, w in e:
            if v < adj:
                E.append((v, adj, w))
    
    return E


def shortest_path_decreasing_weights(G, s, t):
    n = len(G)

    E = create_E(G)

    dist = [float("inf")]*n
    dist[s] = 0

    E.sort(key = lambda x: x[2], reverse=True)
    
    ind = 0
    while E[ind][0] != s and E[ind][1] != s:
        ind += 1
    
    for i in range(ind, len(E)):
        v, u, w = E[i]
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
        if dist[u] > dist[v] + w:
           dist[u] = dist[v] + w
    
    return dist[t]

G = [[(1,7), (3,10), (2,9)],
     [(2,6), (0, 7), (3, 8)],
     [(1,6), (0, 9)],
     [(1,8), (0,10)]]

print(shortest_path_decreasing_weights(G, 3, 2))

