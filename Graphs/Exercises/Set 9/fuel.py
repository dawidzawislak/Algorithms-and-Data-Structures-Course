from queue import PriorityQueue

def cheapest_travel(G, C, capacity, fuel, s, t):
    n = len(G)
    cost = [[float("inf")]*(capacity+1) for _ in range(n)]
    parent = [[(None, 0)]*(capacity+1) for _ in range(n)]

    pq = PriorityQueue()
    for i in range(0, capacity+1-fuel):
        cost[s][i] = C[s]*i
        pq.put((C[s]*i, s, fuel+i))

    while not pq.empty():
        curr_cost, v, fuel_l = pq.get()
        if v == t: break
        for adj, d in G[v]:
            fuel_level = fuel_l - d
            if fuel_level < 0: continue
            for c in range(capacity+1-fuel_level):
                f = c + fuel_level
                if cost[adj][f] > curr_cost + c*C[adj]:
                    cost[adj][f] = curr_cost + c*C[adj]
                    parent[adj][f] = (v, fuel_l)
                    pq.put((cost[adj][f], adj, f))
    

    path = []
    v = t
    f = cost[t].index(min(cost[t]))
    while v is not None:
        path.append(v)
        v, f = parent[v][f]
    

    return min(cost[t]), path[::-1]


def undirected_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G

E = [(0, 1, 5), (1, 2, 3), (0, 2, 7), (2, 3, 4), (3, 4, 6)]
C = [8, 5, 3, 2, 1]
G = undirected_weighted_graph_list(E)

s = 0
t = 4
# capacity = 12
# capacity = 15
capacity = 10
fuel = 0

print(cheapest_travel(G, C, capacity, fuel, s, t))


graph  = [[(1,2), (2,1)],
     [(2,1), (0,2)],
     [(3,2), (0,1), (1,2)],
     [(2,2)]]
p = [1,100,100,100]

print(cheapest_travel(graph, p, 100, 0, 0, 3))