def longest_with_klen(E, k):
    vertices = set()
    for i in range(len(E)):
        vertices.add(E[i][0])
        vertices.add(E[i][1])
    n = max(vertices)+1
    #adj = [[] for _ in range(n)]
    adj = dict()
    adj.setdefault()
    n = 0
    for i in range(len(E)): 
        if adj[E[i][1]] == None:
            adj.setdefault(E[i][1], [])
            n += 1
        adj[E[i][1]].append((E[i][0], E[i][1] - E[i][0]))

    F = [[0]*(k+1) for _ in range(n)]

    def f(i, k):
        if k <= 0: return 0
        if F[i][k] != 0: return F[i][k]
        for v,w in adj[i]:
            F[i][k] = max(F[i][k], w+f(v, k-1))
        
        return F[i][k]
    
    maxl = 0
    for v in list(vertices):
        maxl = max(maxl, f(v,k))
    
    return maxl

E = [(0,2),(1,2), (2,4), (3,6), (4,5), (5,10), (5,9)]
k = 3

def max_length_merge(A, k):
    inf = float('inf')
    a, b, length = 0, 1, 2
    n = len(A)
    A.sort()
    for i in range (n):
        A[i] = [A[i][a],A[i][b],A[i][b]-A[i][a]]
    F = [[-inf for _ in range (n)] for _ in range (k)]
    for i in range (n):
        segment = A[i]
        F[0][i] = segment[length]

    for i in range(1,k):
        for j in range(i-1,n):
            for l in range(i-1,j):
                if A[l][b] == A[j][a]:
                    F[i][j] = max(F[i][j], F[i-1][l] + A[j][length])

    ma = -inf
    for i in range (k):
        for j in range (n):
            if F[i][j] > ma:
                ma = F[i][j]
    
    for e in A:
        print(e)
    for e in F:
        print(e)
    
    return ma

print(max_length_merge(E,k))
print(longest_with_klen(E, k))