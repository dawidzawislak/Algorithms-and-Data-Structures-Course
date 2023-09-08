from queue import Queue

def BFS(G, s):
    n = len(G)
    visited = [False]*n
    distance = [float("inf")]*n

    visited[s] = True
    distance[s] = 0

    q = Queue()
    q.put(s)

    while not q.empty():
        v = q.get()
        for adj in G[v]:
            if not visited[adj]:
                visited[adj] = True
                distance[adj] = distance[v]+1
                q.put(adj)

    return distance

def shortest_paths(G, s):    
    dist = BFS(G, s)
    paths = []
    for i in range(len(G)):
        if i == s: continue
        paths.append((i, dist[i])) 
    
    return paths


G = [[1, 2],
    [2, 3, 5],
    [4, 3],
    [5, 4],
    [5],
    []]

print(shortest_paths(G, 0))