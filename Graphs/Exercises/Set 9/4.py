from queue import PriorityQueue

def get_dist(G, s, t, alice_starting):
    n = len(G)
    dist = [float("inf")]*n
    parent = [None]*n
    q = PriorityQueue()
    dist[s] = 0
    q.put((0, s, alice_starting)) # dist, vertex, is_alice_driving, got_there

    while not q.empty():
        cd, v, alice = q.get()
        for adj, w in G[v]:
            if alice:
                if dist[adj] > cd + w:
                    dist[adj] = cd+w
                    q.put((dist[adj], adj, False))
                    parent[adj] = v
            else:
                if dist[adj] > cd:
                    dist[adj] = cd
                    q.put((dist[adj], adj, True))
                    parent[adj] = v
    
    return dist[t], parent

def alice_and_bob(G, s, t):
    starting = "Alice"
    min_d, parent = get_dist(G, s, t, True)

    bob_d, par_b = get_dist(G, s, t, False)
    if min_d > bob_d:
        min_d = bob_d
        starting = "Bob"
        parent = par_b
    
    if min_d == float("inf"):
        return "Path doesn't exist"

    path = [t]
    while parent[path[-1]] != s:
        path.append(parent[path[-1]])
    path.append(s)

    return starting, min_d, path[::-1]


def create_graph(E):
    # find n
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1

    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
    
    return G

E = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]



G = create_graph(E)

print(alice_and_bob(G, 9, 2))