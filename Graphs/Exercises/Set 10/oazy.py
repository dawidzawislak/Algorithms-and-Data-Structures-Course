def create_graph(E, C):
    n = E[0][0]

    for e in E:
        n = max(n, e[0], e[1])
    
    n += 1

    G = [[] for _ in range(n)]

    for e in E:
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
    
    is_city = [False]*n
    for c in C:
        is_city[c] = True

    G2 = [[] for _ in range(n)]

    for i in range(n):
        if is_city[i]:
            o1, o2 = G[i]
            G2[o1].append((o2, True))
            G2[o2].append((o1, True))
        else:
            for adj in G[i]:
                if not is_city[adj]:
                    G2[i].append((adj, False))

    flag = True
    skip = False
    while flag:
        skip = False
        flag = False
        for i in range(n):
            for e in G2[i]:
                if not e[1]:
                    flag = True
                    G2[i].remove(e)
                    G2[e[0]].remove((i, False))
                    G2[i] += G2[e[0]]
                    G2[e[0]] = []
                    skip = True
            if skip: break
    
    return G2,0



def contains_path_circuit(G):
    n = len(G)
    degs = [0]*n
    ind = 0
    odd_cnt = 0
    start = 0
    
    for e in G:
        degs[ind] += len(e)
        ind += 1

    for v,d in enumerate(degs):
        if d % 2 != 0: 
            start = v
            odd_cnt += 1 
    
    if odd_cnt == 0: return "circuit",0
    if odd_cnt == 2: return "path",start
    return 0,-1

E = [(0, 1), (1, 2), (0, 10), (2, 9), (2, 14), (2, 3), (3, 8), (8, 14), (9, 14), (10, 9), (3, 4),
     (8, 7), (7, 4), (14, 7), (4, 5), (7, 6), (6, 5), (14, 6), (9, 12), (12, 14), (10, 11), (15, 6), (11,16), (16,13), (13,17), (17,15)]
C = [1, 11, 13, 12, 15, 5]



# E = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 5), (4, 7), (5, 9), (3, 9), (1, 7), (0, 7), (7, 10), (10, 11),
#      (1, 6), (6, 8)]
# C = [0, 2, 9, 4, 10, 6]

G, tm = create_graph(E, C)

for i,r in enumerate(G):
    print(i,r)

print(contains_path_circuit(G))