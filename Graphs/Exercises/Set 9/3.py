# widest path

from queue import PriorityQueue
from math import ceil

def create_graph(C):
    # find n
    n = 0
    for e in C:
        n = max(n, e[0], e[1])
    n += 1

    G = [[] for _ in range(n)]
    for e in C:
        G[e[0]].append((e[1], e[2]))
    
    return G


def widest_path(C, s, t):
    G = create_graph(C)
    n = len(G)
    widest_possible = [0]*n
    widest_possible[s] = float("inf")

    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        wp, v = q.get()
        wp = -wp

        for adj, w in G[v]:
            if widest_possible[adj] < max(min(widest_possible[v], w), widest_possible[adj]):
                widest_possible[adj] = max(min(widest_possible[v], w), widest_possible[adj])
                q.put((-widest_possible[adj], adj))
    
    return widest_possible[t]

def no_groups(C, s, t, K):
    return ceil(K/widest_path(C, s, t))

C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

num_tourists = 50
s = 0
t = 7
print(no_groups(C, s, t, num_tourists))