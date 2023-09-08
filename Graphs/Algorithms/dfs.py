def dfs_adj_list(G):
    n = len(G)
    visited = [False]*n
    counter = 0 # licznik spójnych składowych

    def dfsVisit(i):
        nonlocal G, visited

        visited[i] = True
        for adj in G[i]:
            if visited[adj] == False:
                dfsVisit(adj)

    for i in range(n):
        if visited[i] == False:
            dfsVisit(i)
            counter += 1

def dfs_adj_matrix(G):
    n = len(G)
    visited = [False]*n
    counter = 0 # licznik spójnych składowych

    def dfsVisit(v):
        nonlocal G, visited

        visited[i] = True
        for i in range(n):
            if G[v][i] == 1 and visited[i] == False:
                dfsVisit(i)

    for i in range(n):
        if visited[i] == False:
            dfsVisit(i)
            counter += 1

