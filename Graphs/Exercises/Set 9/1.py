"""
(dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
stwierdza czy dany graf zawiera dobry początek.

graf silnie spojnych skladowych
top sort
"""

from collections import deque

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
    G = reverse_edges(G)

    n = len(G)
    visited = [False]*n

    def dfs_visit(v, vert):
        nonlocal G, visited
        visited[v] = True
        vert.append(v)
        for adj in G[v]:
            if not visited[adj]:
                dfs_visit(adj, vert)

    scc_tab = []

    for i in processed:
        vert = []
        if not visited[i]:
            dfs_visit(i,vert)
            scc_tab.append(vert)
    
    G = reverse_edges(G)

    return create_scc_graph(G, scc_tab)

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

    order = topological_sort(G2)

    for v in scc_t[order[0]]:
        n = len(G)
        visited = [False]*n
        counter = 0

        def dfsVisit(i):
            nonlocal G, visited, counter
            counter += 1
            visited[i] = True
            for adj in G[i]:
                if visited[adj] == False:
                    dfsVisit(adj)

        dfsVisit(v)
        if counter == n: return v
    return None

#G = [[1],[2,3],[0],[4],[5],[3]]

def topological_sort(G):
    n = len(G)
    visited = [False]*n

    sorted_graph = []

    def dfs_visit(v):
        nonlocal G, visited

        visited[v] = True
        for adj in G[v]:
            if not visited[adj]:
                dfs_visit(adj)

        sorted_graph.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)

    sorted_graph.reverse()

    return sorted_graph

def directed_graph_list(E):
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    
    G = [deque() for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
    return G

E = [(0, 3), (0, 1), (1, 2), (1, 10), (2, 3), (3, 4), (4, 2), (4, 5), (5, 2), (6, 5), (6, 9), (7, 6), (8, 7),
     (9, 8), (10, 9), (10, 0)]
G = directed_graph_list(E)

print(scc(G))