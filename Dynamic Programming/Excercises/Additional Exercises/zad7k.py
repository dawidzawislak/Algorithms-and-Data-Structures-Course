from zad7ktesty import runtests 
from collections import deque


def check_root(T, i):
    N = len(T)
    M = len(T[0])
    val  = T[0][i]
    T[0][i] = 0

    q = deque()
    q.append((0,i))
    moves = ((-1,0), (1,0), (0,-1), (0,1))
    while len(q) > 0:
        x,y = q.popleft()
        for m in moves:
            nx,ny = x+m[0], y+m[1]
            if 0 <= nx < N and 0 <= ny < M and T[nx][ny] > 0:
                val += T[nx][ny]
                T[nx][ny] = 0
                q.append((nx, ny))
    
    return val

def ogrodnik (T, D, Z, l):
    N = len(T)
    M = len(T[0])

    weights = []
    for i in D:
        if T[0][i] > 0:
            weights.append(check_root(T,i))

    values = Z
    capacity = l

    F = [[0]*(capacity+1) for _ in range(len(D))]

    for b in range(weights[0], capacity+1):
        F[0][b] = values[0]

    for i in range(1, len(D)):
        for b in range(capacity+1):
            F[i][b] = F[i-1][b]
            if b - weights[i] >= 0 and F[i-1][b - weights[i]]+values[i] > F[i][b]:
                F[i][b] = F[i-1][b - weights[i]]+values[i]

    return max(F[len(D)-1])

runtests( ogrodnik, all_tests=True )
