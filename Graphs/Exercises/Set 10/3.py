from math import log

def contains_negative_cycle(G):
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
  
  for i in range(n):
    if distance[i][i] < 0:
      return True
  
  return False

def create_graph(K):
    n = 0
    for e in K:
        n = max(n, e[0], e[1])
    n += 1
    
    G = [[0] * n for _ in range(n)]
    for e in K:
        G[e[0]][e[1]] = log(e[2])
    return G

PLN = 0; EUR = 1; USD = 2; YEN = 3;

K = [(PLN, EUR, 4.51), (PLN, USD, 3.68), (PLN, YEN, 0.034),
     (EUR, PLN, 0.22), (EUR, USD, 0.82), (EUR, YEN, 0.0075),
     (USD, PLN, 0.27), (USD, EUR, 1.22), (USD, YEN, 0.0091),
     (YEN, PLN, 29.83), (YEN, EUR, 133,47), (YEN, USD, 109.62)]

g = create_graph(K)

print(contains_negative_cycle(g))