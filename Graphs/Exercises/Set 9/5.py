from queue import PriorityQueue

def min_cost_fuel(G, C, capacity, fuel, s, t):
    n = len(G)

    cost = [[float("inf")]*(capacity+1) for _ in range(n)]
    parent = [[[None]*2 for _ in range(capacity+1)] for _ in range(n)]

    q = PriorityQueue()
    for c in range(capacity+1):
        if c-fuel > 0:
            cost[s][c] = (c-fuel)*C[s]
            q.put(((c-fuel)*C[s], s, c))
    
    while not q.empty():
        curr_cost, v, fuel_lvl = q.get()

        for adj, w in G[v]:
            fuel_level = fuel_lvl - w
            if fuel_level < 0: continue

            for new_cap in range(fuel_level, capacity+1):
                to_tank = new_cap - fuel_level

                if cost[adj][new_cap] > curr_cost + to_tank*C[adj]:
                    cost[adj][new_cap] = curr_cost + to_tank*C[adj]
                    parent[adj][new_cap] = (v, fuel_lvl)
                    q.put((curr_cost + to_tank*C[adj], adj, new_cap))

    def path(v, f, p):
        nonlocal parent
        if v == s: 
            return p
        else:
            p.append((parent[v][f][0], parent[v][f][1]))
            return path(parent[v][f][0], parent[v][f][1], p)
    
    minc = min(cost[t])

    p = [(t,None)]
    path(t,cost[t].index(minc), p)
    p.reverse()
    return minc, [x[0] for x in p]


def undirected_weighted_graph_list(E):
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
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
capacity = 10
fuel = 0


print(min_cost_fuel(G, C, capacity, fuel, s, t))

graph  = [[(1,2), (2,1)],
     [(2,1), (0,2)],
     [(3,2), (0,1), (1,2)],
     [(2,2)]]
p = [1,100,100,100]

print(min_cost_fuel(graph, p, 100, 0, 0, 3))


C2 = [5, 7, 3, 5, 2, 1, 8, 10, 6]

s2 = 0
t2 = 3
# capacity = 12
# capacity = 15
capacity2 = 14
fuel2 = 5

print(min_cost_fuel(G, C2, capacity2, fuel2, s2, t2))