"""
(najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?
"""

def topological_sort(G):
    n = len(G)
    visited = [False]*n

    sorted_graph = []

    def dfs_visit(v):
        nonlocal G, visited

        visited[v] = True
        for adj,_ in G[v]:
            if not visited[adj]:
                dfs_visit(adj)

        sorted_graph.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)

    sorted_graph.reverse()

    return sorted_graph

def shortest_path_DAG(G, s):
    n = len(G)
    order = topological_sort(G)

    distance = [float("inf")]*n
    distance[s] = 0

    ind = 0

    while order[ind] != s:
        ind += 1
    
    for i in range(ind, n):
        for adj, w in G[order[i]]:
            if distance[adj] > distance[order[i]] + w:
                distance[adj] = distance[order[i]] + w
    
    return distance

def directed_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
    return G



E = [(0, 1, 5), (0, 7, -2), (1, 6, 7), (1, 2, 8), (3, 2, 3), (4, 3, 2), (5, 4, 1), (5, 2, 4), (6, 5, -10),
     (6, 9, 6), (6, 8, -3), (7, 8, 4), (7, 6, 12), (8, 9, 0), (9, 4, -5)]

G = directed_weighted_graph_list(E)

print(shortest_path_DAG(G, 0))
