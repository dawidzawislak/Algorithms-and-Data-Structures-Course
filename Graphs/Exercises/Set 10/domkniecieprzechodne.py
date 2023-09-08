# O(V^3)
# Ścieżki między każdą parą wierzchołków
# G dane jako macierz sąsiedztwa

def floyd_warshall(G):
  inf = float("inf")
  n = len(G)
  distance = [[inf for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if G[i][j]  != 0:
        distance[i][j] = G[i][j]
    distance[i][i] = 0

  for t in range(n):
    for x in range(n):
      for y in range(n):
        distance[x][y] = min(distance[x][y], (distance[x][t] + distance[t][y]))
  
  for i in range(n):
    if distance[i][i] < 0:
      return False
  
  return distance

G=[[0, 1, float('inf'), 1, float('inf')],
[float('inf'), 0, float('inf'), float('inf'), float('inf')],
[float('inf'), 1, 0, float('inf'), float('inf')],
[float('inf'), float('inf'), 1, 0, 1],
[float('inf'), float('inf'), 1, float('inf'), 0]]

g_ = floyd_warshall(G)

for r in g_:
  print(r)