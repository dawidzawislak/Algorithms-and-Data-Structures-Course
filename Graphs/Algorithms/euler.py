# --- Adj Matrix ---------------------------------------------
def is_euler_cycle(G):
    n = len(G)
    odd_cnt = 0
    start = -1
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += G[i][j]
            sum -= G[j][i]
        if sum != 0:
            odd_cnt += 1
            start = i
    
    if odd_cnt == 0: return "circuit",0
    if odd_cnt == 2: return "path",start
    return 0,-1

def euler_cycle_mat(G, dir):
    n = len(G)
    type, start = is_euler_cycle(G)
    if type == 0: return None

    path = []
    ind = [0]*n

    def dfs_visit(v):
        nonlocal ind, path, G
        while ind[v] < n:
            if v == ind[v]: 
                ind[v] += 1
                continue
            if v != ind[v] and G[v][ind[v]] == 1:
                G[v][ind[v]] = 0
                if not dir:
                    G[ind[v]][v] = 0
                dfs_visit(ind[v])
            ind[v] += 1

        path.append(v)
    
    dfs_visit(start)

    return type, path[::-1]

G = [[1,1,1,1,1],
     [1,1,1,0,0],
     [1,1,1,0,0],
     [1,0,0,1,1],
     [1,0,0,1,1]]

G = [[0,1,0,0],
     [0,0,1,0],
     [0,0,0,1],
     [1,0,0,0]]

print(euler_cycle_mat(G, True))






















# Znaleźć cykl Eulera

def contains_path_circuit(G, dir):
    n = len(G)
    degs = [0]*n
    ind = 0
    odd_cnt = 0
    start = 0
    if dir:
        for e in G:
            degs[ind] += len(e)
            for v in e:
                degs[v] -= 1
            ind += 1

        for v,d in enumerate(degs):
            if d != 0: 
                start = v
                odd_cnt += 1  
    else:
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

def DFS(G, s):
    n = len(G)
    used_edges = [[False for _ in range(n)] for _ in range(n)]
    path = []

    def DFSVisit(v):
        nonlocal G,used_edges, path
        for adj in G[v]:
            if not used_edges[v][adj]:
                used_edges[v][adj] = True
                used_edges[adj][v] = True
                DFSVisit(adj)
                
        path.append(v)

    DFSVisit(s)

    return path[::-1]


def find_cycle_adj_list(G, dir):
    type, s = contains_path_circuit(G,dir)

    if type == 0: return None
    return type, DFS(G, s)

# G = [[1], [2], [0]]   

# G = [[1,2,3],
# [0,2,3],         
# [0,1],          
# [0,1,4],          
# [3]] 

G = [[1,2,3,4],
[0,2],         
[0,1],          
[0,4],          
[0,3]]  

print(find_cycle_adj_list(G, False))
