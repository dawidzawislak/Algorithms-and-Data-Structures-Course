from collections import deque

def can_fly(G, x, y, t):
    n = len(G)

    def dfs(v, h, visited):
        nonlocal G, y, t
        visited[v] = True
        if v == y: return True
        for adj, opt_h in G[v]:
            if not visited[adj] and  h-t <= opt_h <= h+t:
                return dfs(adj, h, visited)
        return False
    
    def get_path(h):
        nonlocal G, x, y, t
        parent = [None]*len(G)
        visited = [False]*len(G)
        visited[x] = True

        q = deque()
        q.append(x)
        while len(q) > 0:
            v = q.popleft()
            for adj, h_opt in G[v]:
                if not visited[adj] and h-t <= h_opt <= h+t:
                    visited[adj] = True
                    parent[adj] = v
                    q.append(adj)
                    if adj == y:
                        path = [y]
                        while parent[path[-1]] != None:
                            path.append(parent[path[-1]])
                        return path[::-1]

    for v, height in G[x]:
        for h in range(height-t, height+t+1):
            visited = [False]*n
            if dfs(v, h, visited):
                return h, get_path(h)
    
    return False

def undirected_weighted_graph_list(E):
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    return G


E = [(0, 1, 100), (1, 2, 110), (2, 3, 135), (2, 4, 120), (0, 4, 120), (4, 5, 90), (2, 5, 95), (5, 3, 90),
     (0, 7, 115), (7, 6, 120), (4, 6, 95), (5, 6, 110), (6, 3, 105)]
G = undirected_weighted_graph_list(E)

x = 6
y = 1
t = 5
print(can_fly(G, x, y, t))

