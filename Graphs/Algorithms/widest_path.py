from queue import PriorityQueue

def widest_path(G, s, t):
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
