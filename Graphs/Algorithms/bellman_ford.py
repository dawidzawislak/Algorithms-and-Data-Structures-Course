def bellman_ford(G, s):
    n = len(G)

    E = []
    for i,v in enumerate(G):
        for e in v:
            E.append((i, e[0], e[1]))

    distance = [float("inf")]*n
    parent = [-1]*n

    distance[s] = 0

    # Relaksacje
    for i in range(n-1):
        for e in E:
            if distance[e[1]] > distance[e[0]] + e[2]:
                distance[e[1]] = distance[e[0]] + e[2]
                parent[e[1]] = e[0]
    
    # Weryfikacja(wykrywanie ujemnych cykli)
    for e in E:
        if distance[e[1]] > distance[e[0]] + e[2]:
            distance[e[1]] = -float("inf")
    
    return parent, distance


G = [[(1, 3)],
     [(2, 1)],
     [(3, 2)],
     [(1, -2), (4, 2)],
     []]

print(bellman_ford(G, 0))