# Dany jest wierzchołek v w grafie nazywamy "dobrym początkiem" jeżeli każdy inny wierzchołek można osiągnąć ścieżką skierowaną wychodzącą z tego wierzchołka v. Algorytm powinien zwrócić czy dany graf zawiera taki wierzchołek.

def IsGoodStart(G):
    n = len(G)
    time = 0
    visited = [False]*n
    process_time = [-1]*n

    def DFSVisit(G, v):
        nonlocal visited, time, process_time
        visited[v] = True
        for adj in G[v]:
            if not visited[adj]:
                DFSVisit(G, adj)
        
        time += 1
        process_time[v] = time
    
    for v in range(n):
        if not visited[v]:
            DFSVisit(G, v)
    
    for i in range(n):
        if process_time[i] == n:
            index = i
            break
    
    time  = 0
    visited = [False]*n
    DFSVisit(G, index)

    return time == n
