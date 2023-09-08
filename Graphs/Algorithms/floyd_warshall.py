def floyd_warshall(G):
  inf = float("inf")
  n = len(G)
  distance = [[inf for _ in range(n)] for _ in range(n)]
  parent = [[None for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if G[i][j] != 0:
        distance[i][j] = G[i][j]
        parent[i][j] = i
    distance[i][i] = 0

  for t in range(n):
    for x in range(n):
      for y in range(n):
        d1 = distance[x][y]
        d2 = distance[x][t] + distance[t][y]
        if d1 > d2:
          distance[x][y] = d2
          parent[x][y] = parent[t][y]

  # Wykrywanie ujemnych cykli
  # for t in range(n):
  #   for x in range(n):
  #     for y in range(n):
  #       d1 = distance[x][y]
  #       d2 = distance[x][t] + distance[t][y]
  #       if d1 > d2:
  #         distance[x][y] = -inf
  #         parent[x][y] = None
  
  for i in range(n):
    if distance[i][i] < 0:
      return False
  
  return distance, parent

def reconstruct_path(distance, parent, s, t):
  inf = float("inf")
  if distance[s][t] == inf: return []

  v = t
  path = []
  while parent[s][v] != s:
    if v == None: return None
    path.append[v]
    v = parent[s][v]
  
  if parent[s][v] == None: return None
  path.append(s)
  return path