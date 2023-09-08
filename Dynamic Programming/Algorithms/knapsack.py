def knupsack(W,P,B):
    n = len(W)
    F = [[0]*(B+1) for _ in range(n)] # F[i][b]
    parent = [[None]*(B+1) for _ in range(n)]

    for b in range(W[0], B+1):
        F[0][b] = P[0]
    
    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            parent[i][b] = b
            if b - W[i] >= 0 and F[i-1][b-W[i]]+P[i] > F[i][b]:
                F[i][b] = F[i-1][b-W[i]]+P[i]
                parent[i][b] = b-W[i]
    
    #reconstruct
    x = B
    items = []
    for i in range(n-1, -1, -1):
        if parent[i][x] != None and parent[i][x] != x:
            items.append((W[i], P[i]))
        x = parent[i][x]

    return F[n-1][B],items
       

weights = [10,23,30]
prices = [60,100,120]
max_w = 50

print(knupsack(weights, prices, max_w))