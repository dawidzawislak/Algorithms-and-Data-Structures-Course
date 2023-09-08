def find_bridges(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    disc = [-1]*n
    low = [None]*n

    time = 1

    bridges = []

    def dfs_visit(v):
        nonlocal G, visited, disc, parent, low, time
        visited[v] = True
        disc[v] = low[v] = time
        time += 1

        for adj in G[v]:
            if not visited[adj]:
                parent[adj] = v
                dfs_visit(adj)

        for adj in G[v]:
            if parent[v] != adj:        
                low[v] = min(low[adj], low[v])


    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    
    for v in range(n):
        if low[v] == disc[v] and parent[v] != None:
            bridges.append((parent[v], v))
    
    return bridges

def find_bridges_geeks(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    disc = [-1]*n
    low = [None]*n

    time = 1

    bridges = []

    def dfs_visit(v):
        nonlocal G, visited, disc, parent, low, time, bridges
        visited[v] = True
        disc[v] = low[v] = time
        time += 1

        for adj in G[v]:
            if not visited[adj]:
                parent[adj] = v
                dfs_visit(adj)
                low[v] = min(low[adj], low[v])
                if low[adj] > disc[v]:
                    bridges.append((v, adj))
            elif adj != parent[v]:
                low[v] = min(low[v], disc[adj])

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    
    return bridges

G = [[1,2],
     [0,2,6],
     [0,1,3],
     [2,4,5],
     [3,5],
     [4,3],
     [1]]

print(find_bridges(G))
print(find_bridges_geeks(G))