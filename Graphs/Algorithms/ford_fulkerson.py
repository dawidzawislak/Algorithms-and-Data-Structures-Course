from math import inf


def dfs_visit(graph, source, visited, parent):
    visited[source] = True
    for v in range(len(graph)):
        if not visited[v] and graph[source][v] != 0:
            parent[v] = source
            dfs_visit(graph, v, visited, parent)


def dfs(graph, s, t, parent):
    visited = [False] * len(graph)
    dfs_visit(graph, s, visited, parent)
    return visited[t]


def ford_fulkerson_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while dfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow