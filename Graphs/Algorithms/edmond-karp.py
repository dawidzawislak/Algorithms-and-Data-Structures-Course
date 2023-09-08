from math import inf
from collections import deque

def bfs(graph, s, t, parent):
    queue = deque()
    visited = [False] * len(graph)
    visited[s] = True 
    queue.append(s)
    while queue:
        u = queue.popleft()
        if u == t: return True
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                parent[v] = u
                if v == t: return True
                visited[v] = True
                queue.append(v)
    return visited[t]

def edmonds_karp_algorithm(G, s, t):
    if s == t: return 0
    n = len(G)
    graph = [row[:] for row in G]
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
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