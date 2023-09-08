from queue import PriorityQueue

def dijkstra_adj_list(G, s):
    n = len(G)
    distance = [float("inf")]*n
    parent = [-1]*n

    distance[s] = 0

    pq = PriorityQueue()
    pq.put((0, s))
    
    while not pq.empty():
        _, v = pq.get()
        for u, d in G[v]:
            if distance[u] > distance[v] + d:
                distance[u] = distance[v] + d
                parent[u] = v
                pq.put((distance[u], u))
    
    return distance, parent

G = [[(1, 5)], 
    [(0, 5), (2, 21), (3, 1)], 
    [(1, 21), (4, 7)], 
    [(1, 1), (4, 13), (5, 16)], 
    [(2, 7), (3, 13), (6, 4)],
    [(3, 16), (6, 1)], 
    [(4, 4), (5, 1)]]

print(dijkstra_adj_list(G, 0))

def min_dist(dist, vis, n):
    min = float("inf")
    min_index = None
    for v in range(n):
        if dist[v] < min and not vis[v]:
            min = dist[v]
            min_index = v

    return min_index


def dijkstra_adj_mat(G, s):
    n = len(G)
    dist = [float("inf")] * n
    dist[s] = 0
    visited = [False] * n
    parent = [-1]*n

    for i in range(n):
        x = min_dist(dist, visited,n)
        if x == None: break
        visited[x] = True

        for y in range(n):
            if G[x][y] > 0 and not visited[y] and dist[y] > dist[x] + G[x][y]:
                dist[y] = dist[x] + G[x][y]
                parent[y] = x

    return dist, parent

G2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print(dijkstra_adj_mat(G2, 0))