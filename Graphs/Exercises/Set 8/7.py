from collections import deque

def create_graph(M):
    n = len(M)
    G = [[] for _ in range(n*n)]

    offsets = ((-1,-1),(-1,1),(1,1),(1,-1),(0,-1),(0,1), (-1,0),(1,0))

    for i in range(n):
        for j in range(n):
            for off in offsets:
                ni, nj = i+off[0], j+off[1]
                if 0 <= ni < n and 0 <= nj < n:
                    if M[ni][nj] == 1:
                        G[i*n+j].append(ni*n+nj)
                    else:
                        w = M[ni][nj]
                        prev = i*n+j
                        for _ in range(w-1):
                            G.append([])
                            G[prev].append(len(G)-1)
                            prev = len(G)-1
                        G[-1].append(ni*n+nj)
                # for _, adj in enumerate(G):
                #     print(_, adj)
                # print(i, j, ni, nj)
                # input()

    return G

M = [[2, 2, 1, 5, 4],
[2, 1, 3, 1, 2],
[3, 1, 3, 5, 2],
[5, 4, 1, 5, 1],
[5, 3, 3, 4, 2]]

M2 = [[1,1],
    [1,2]]

M3 = [[5, 1, 5, 5, 1, 3, 4, 5, 1, 4, 5, 3],
[4, 4, 4, 2, 1, 1, 4, 1, 5, 3, 3, 4],
[5, 5, 3, 5, 1, 5, 5, 2, 5, 4, 1, 1],
[1, 5, 3, 1, 5, 2, 1, 3, 3, 5, 2, 1],
[1, 2, 3, 2, 5, 3, 5, 1, 3, 3, 2, 4],
[2, 2, 3, 5, 1, 4, 4, 1, 5, 1, 3, 2],
[1, 4, 2, 3, 3, 1, 1, 2, 1, 5, 2, 5],
[2, 5, 3, 4, 1, 5, 2, 5, 3, 2, 2, 1],
[2, 4, 5, 5, 5, 1, 3, 3, 1, 5, 1, 2],
[2, 4, 4, 3, 1, 2, 1, 3, 1, 2, 2, 4],
[5, 4, 3, 5, 3, 5, 1, 5, 2, 3, 1, 3],
[5, 5, 1, 3, 5, 4, 2, 3, 5, 3, 2, 3]]

def kings_path(M):
    G = create_graph(M)
    n = len(G)
    m = len(M)
    visited = [False]*n
    cost = [float("inf")]*n
    cost[0] = M[0][0]
    visited[0] = True

    q = deque()
    q.append(0)

    while len(q) > 0:
        v = q.popleft()
        if v == (m-1)*m+(m-1): 
            return cost[v]
        for adj in G[v]:
            if not visited[adj]:
                visited[adj] = True
                cost[adj] = cost[v]+1
                q.append(adj)

print(kings_path(M3))