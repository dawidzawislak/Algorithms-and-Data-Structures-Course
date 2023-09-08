def domkniecie_przechodnie_mat(G):
  inf = float("inf")
  n = len(G)
  distance = [[inf for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if G[i][j] != 0:
        distance[i][j] = G[i][j]
    distance[i][i] = 0

  for t in range(n):
    for x in range(n):
      for y in range(n):
        distance[x][y] = min(distance[x][y], distance[x][t] + distance[t][y])
  
  for x in range(n):
    for y in range(n):
       if distance[x][y] == inf: distance[x][y] = 0
       elif distance[x][y] > 0:  distance[x][y] = 1

  return distance

def domkniecie_przechodnie_adj_list(G):
    n = len(G)
    H = [[0]*n for _ in range(n)]
    visited = [0]*n
    fromv = 1

    def dfs(start, v):
       nonlocal fromv
       visited[v] = fromv
       for adj in G[v]:
          if visited[adj] != fromv:
            H[start][adj] = 1
            dfs(start, adj)
    
    for i in range(n):
       dfs(i, i)
       fromv += 1
    
    return H


def directed_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append(e[1])
    return G

def directed_graph_matrix(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[0] * n for _ in range(n)]  # False means no edge
    for e in E:
        G[e[0]][e[1]] = 1
    return G

E = [(0, 1), (1, 5), (0, 2), (2, 4), (2, 3), (3, 4), (4, 5), (3, 5), (3, 6), (6, 5)]

G_mat = directed_graph_matrix(E)
G_adj = directed_graph_list(E)

print(*domkniecie_przechodnie_mat(G_mat), sep="\n")
print()
print(*domkniecie_przechodnie_adj_list(G_adj), sep="\n")