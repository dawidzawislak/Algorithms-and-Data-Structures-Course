from queue import Queue

def BFS_adj_list(G, s):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
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
                parent[adj] = v
                q.put(adj)

    return visited,parent,distance


def BFS_adj_matrix(G,s):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
    distance = [float("inf")]*n

    visited[s] = True
    distance[s] = 0

    q = Queue()
    q.put(s)

    while not q.empty():
        v = q.get()
        for i in range(n):
            if i == v: continue
            if G[v][i] == 1 and not visited[i]:
                visited[i] = True
                distance[i] = distance[v]+1
                parent[i] = v
                q.put(i)
    
    return visited,parent,distance