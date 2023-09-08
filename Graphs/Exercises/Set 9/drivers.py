from queue import PriorityQueue

def drivers(G, s, t):
    n = len(G)
    distance = [[float("inf")]*2 for _ in range(n)]
    visited = [[False]*2 for _ in range(n)]
    parent = [[-1]*2 for _ in range(n)]

    distance[s][0] = 0
    distance[s][1] = 0

    pq = PriorityQueue()
    pq.put((0, s, 0, 0))
    pq.put((0, s, 1, 1))

    while not pq.empty():
        _, v, ala, started = pq.get()
        visited[v][started] = True
        for u, d in G[v]:
            if not visited[u][started] and distance[u][started] > distance[v][started]+d*(d*((ala+1)%2)):
                distance[u][started] = distance[v][started]+(d*((ala+1)%2))
                parent[u][started] = v
                pq.put((distance[u][started], u, (ala+1)%2, started))

    
    if distance[t][0] < distance[t][1]: i = 0
    else: i = 1
    print(distance[t][0], distance[t][1])
    path = [t]
    ptr = t
    while parent[ptr][i] != s:
        path.append(parent[ptr][i])
        ptr = parent[ptr][i]
    path.append(s)
    path.reverse()
    return "Ala" if i == 0 else "Bob", distance[t][i],path
    


E = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

def CreateGraph(G):
    n = 0
    for e in G:
        n = max(n, e[0], e[1])
    n += 1
    G_ = [[] for _ in range(n)]

    for e in G:
        G_[e[0]].append((e[1], e[2]))
    
    return G_

G = CreateGraph(E)

print(drivers(G, 0, 7))