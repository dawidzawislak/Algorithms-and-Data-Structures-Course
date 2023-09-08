# Kruskal algorithm for graph given as adj list
def find_mst(G):
    n = len(G)
    E = []
    for v, edges in enumerate(G):
        for e in edges:
            E.append((v,e[0], e[1]))

    E.sort(key= lambda x: x[2])

    parent = [i for i in range(n)]

    def Find(x):
        nonlocal parent

        if parent[x] != x:
            x = Find(parent[x])
        
        return x

    def Union(x, y):
        nonlocal parent
        x_root = Find(x)
        y_root = Find(y)

        if x_root != y_root:
            parent[y_root] = x_root
            return True
        return False

    mst = []
    for e in E:
        if Union(e[0], e[1]): mst.append((e[0], e[1]))

    return mst

G = [[(1,1),(4,5),(5,8)],       
     [(0,1),(2,3)],             
     [(1,3),(4,4),(3,6)],       
     [(2,6),(4,2)],             
     [(0,5),(5,7),(2,4),(3,2)], 
     [(0,8),(4,7)]]             

print(find_mst(G))