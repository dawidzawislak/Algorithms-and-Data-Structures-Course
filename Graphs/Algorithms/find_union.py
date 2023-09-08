n = 10

rank = [0 for _ in range(n)]
parent = [i for i in range(n)]

def Find(x):
  global parent

  if parent[x] != x:
    x.parent =  Find(parent[x])
  
  return x.parent


def Union(x, y):
  global rank, parent
  x = Find(x)
  y = Find(y)

  if x != y: return False

  if rank[x] > rank[y]:
    parent[y] = x
  else:
    parent[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1
  
  return True