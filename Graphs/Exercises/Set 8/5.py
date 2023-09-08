from collections import deque



def binary_edges(G, s, t):
    n = len(G)
    distance = [float("inf")]*n
    distance[s] = 0

    q = deque()
    q.append(s)

    while len(q) > 0:
        v = q.popleft()
        for adj, w in G[v]:
            if distance[v]+w < distance[adj]:
                distance[adj] = distance[v]+w
                if w == 0:
                    q.appendleft(adj)
                else:
                    q.append(adj)
    
    return distance[t]


graph = [[(1, 1), (3, 1), (7, 1)],
[(0, 1), (2, 0), (4, 1), (3, 0)],
[(1, 0), (4, 0), (5, 1)],
[(0, 1), (4, 0), (7, 0), (8, 1), (1, 0)],
[(1, 1), (2, 0), (3, 0), (5, 0)],
[(2, 1), (4, 0), (8, 0), (6, 1)],
[(8, 1), (5, 1)],
[(0, 1), (3, 0), (8, 1)],
[(3, 1), (7, 1), (5, 0), (6, 1)]]

print(binary_edges(graph, 0, 8))