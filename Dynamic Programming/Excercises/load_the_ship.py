def f(A, L):
    n = len(A)
    F = [[[False]*(L+1) for _ in range(L+1)] for _ in range(n)] # f(i,d,u)
    parent = [[(None, None)]*(L+1) for _ in range(L+1)]
    
    if A[0] <= L:
        F[0][L-A[0]][L] = True
        F[0][L][L-A[0]] = True

    for i in range(1, n):
        for d in range(L+1):
            for u in range(L+1):
                if d + A[i] <= L:
                    if F[i-1][d+A[i]][u]:
                        F[i][d][u] = F[i-1][d+A[i]][u]
                        parent[d][u] = (d+A[i], u)
                if u + A[i] <= L:
                    F[i][d][u] = F[i][d][u] or F[i-1][d][u+A[i]]
                    if F[i-1][d][u+A[i]]:
                        #F[i][d][u] = F[i-1][d][u+A[i]]
                        parent[d][u] = (d, u+A[i])

    mini = None
    mind = minu = float("inf")

    for d in range(L, -1, -1):
        for u in range(L, -1, -1):
            for i in range(n):
                if F[i][d][u] and mind+minu > d + u:
                    mind = d
                    minu = u
                    mini = i
    
    path = []

    while parent[mind][minu][0] != None and parent[mind][minu][1] != None:
        if parent[mind][minu][0] > mind: path.append("D")
        else: path.append("U")
        mind, minu = parent[mind][minu]

    if L > mind: path.append("D")
    else: path.append("U")

    path.reverse()

    return mini+1, path

L = 4

cars = [2,4,1,1]

print(f(cars, L))