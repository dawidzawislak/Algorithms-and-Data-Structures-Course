# Dawid Zawiślak
# Algortym szuka najpierw najkrótaszej ścieżki pomiędzy wierzchołkami s i t za pomocą BFS.
# Następnie dla każdej krawędzi znalezionej ścieżki wykonuje BFS dla grafu bez danej krawędzi i sprawdza czy jej usunięcie "rozerwało" graf pomiędzy wierzchołkami s i t, lub nowa najkrótasza ścieżka pomiędzy nimi jest dluższa od pierwotnej.
# Gdy znajdzie taką krawędź zwraca krotke zawierającą jej 2 wierzchołki. Gdy jej nie znajdzie zwraca None.
from zad4testy import runtests
from collections import deque

def longer( G, s, t ):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    d = [-1]*n

    que = deque()
    que.append(s)
    visited[s] = True
    d[s] = 0

    path_found = False

    while len(que) > 0:
        v = que.popleft()
        if v == t:
            path_found = True
            break
        for adj in G[v]:
            if not visited[adj]:
                visited[adj] = True
                parent[adj] = v
                d[adj] = d[v]+1
                que.append(adj)
            
    if not path_found: return None
    
    path = [(parent[t],t)]
    if parent[t] != s:
        while parent[path[-1][0]] != s:
            path.append((parent[path[-1][0]],path[-1][0]))
        path.append((s, path[-1][0]))

    old_dist = d[t]    
    
    for to_block in path:
        visited = [False]*n
        d[t] = -1
        que.clear()
        que.append(s)
        visited[s] = True
        d[s] = 0

        path_found = False
        
        while len(que) > 0:
            v = que.popleft()
            if v == t:
                path_found = True
                break
            for adj in G[v]:
                if visited[adj] or (v == to_block[0] and adj == to_block[1]): continue
                visited[adj] = True
                d[adj] = d[v]+1
                que.append(adj)
        
            
        if not path_found or d[t] > old_dist: 
            return to_block
                
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )