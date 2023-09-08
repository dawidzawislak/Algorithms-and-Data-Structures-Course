from collections import deque

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

G = [[1, 2],
     [2, 3],
     [],
     [4,5],
     [],
     [],
     [3]]


def contains_hamiltionian_path(G):
    V = topological_sort(G)
    n = len(V)
    for i in range(n-1):
        if V[i+1] not in G[V[i]]:
            return False
        
    return True


print(contains_hamiltionian_path(G))