def dfs(G):
    n = len(G)
    processed = []
    visited = [False]*n
    t = 0

    def dfs_visit(v):
        nonlocal G, processed, visited
        visited[v] = True
        for adj in G[v]:
            if not visited[adj]:
                dfs_visit(adj)
        processed.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    
    return processed[::-1]


def reverse_edges(G):
    n = len(G)
    rev = [[] for _ in range(n)]
    for i in range(n):
        for adj in G[i]:
            rev[adj].append(i)
    
    return rev


def scc(G):
    processed = dfs(G)
    G2 = reverse_edges(G)

    n = len(G2)
    visited = [False]*n

    def dfs_visit(v, vert):
        nonlocal G2, visited
        visited[v] = True
        vert.append(v)
        for adj in G2[v]:
            if not visited[adj]:
                dfs_visit(adj, vert)

    scc_tab = []

    for i in processed:
        vert = []
        if not visited[i]:
            dfs_visit(i,vert)
            scc_tab.append(vert)
    
    return scc_tab


def create_scc_graph(G, scc_t):
    G2 = [[] for _ in range(len(scc_t))]

    scc_ind = [None]*len(G)

    for i, scc in enumerate(scc_t):
        for v in scc:
            scc_ind[v] = i
    
    for i, scc in enumerate(scc_t):
        for v in scc:
            for adj in G[v]:
                if scc_ind[adj] != i:
                    G2[i].append(scc_ind[adj])
    
    return G2

G = [[1],[2,3],[0],[4],[5],[3]]

scc_tab = scc(G)
print(scc_tab)
print(create_scc_graph(G, scc_tab))