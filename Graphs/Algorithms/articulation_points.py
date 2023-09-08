def find_ap(G):
    n = len(G)

    visited = [False]*n
    discovered = [float("inf")]*n
    low = [float("inf")]*n
    parent = [None]*n
    ap = [False]*n
    time = 0

    def dfs_visit(v):
        nonlocal G, time, visited, discovered, low, parent, ap
        children_cnt = 0

        visited[v] = True

        discovered[v] = low[v] = time
        time += 1

        for adj in G[v]:
            if not visited[adj]:
                parent[adj] = v
                children_cnt += 1
                dfs_visit(adj)

                low[v] = min(low[v], low[adj])

                if parent[v] == None and children_cnt > 1:
                    ap[v] = True
                
                if parent[v] != None and low[adj] >= discovered[v]:
                    ap[v] = True
            
            elif adj != parent[v]:
                low[v] = min(low[v], discovered[adj])


    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    
    points = []
    for v, a in enumerate(ap):
        if a: points.append(v)
    
    return points

G = [[1],[0,2],[1,3],[2]]

print(find_ap(G))
