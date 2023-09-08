from queue import PriorityQueue

def find_mst(G, s=0):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    w = [float("inf")]*n

    q = PriorityQueue()
    q.put((0, s))
    w[s] = 0

    while not q.empty():
        _, v = q.get()
        for adj,wa in G[v]:
            if not visited[adj] and wa < w[adj]:
                w[adj] = wa
                parent[adj] = v
                q.put((w[adj], adj))
        visited[v] = True

    mst = []
    for i in range(0, n):
        if parent[i] != None:
            mst.append((i, parent[i]))

    return mst

G = [[(1,1),(4,5),(5,8)],   
     [(0,1),(2,3)],         
     [(1,3),(4,4),(3,6)],   
     [(2,6),(4,2)],         
     [(0,5),(5,7),(2,4),(3,2)],
     [(0,8),(4,7)]]         

print(find_mst(G,2))