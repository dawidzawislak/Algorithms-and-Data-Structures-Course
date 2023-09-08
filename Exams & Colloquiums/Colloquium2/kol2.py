# Dawid Zawiślak
# Najpierw zamieniam reprezentację grafu na listę krawędzi. Następnie sortuję ją po wagach rosnąco.
# Następnie próbuję za pomocą algorytmu Kruskala znaleźć minimalne drzewo rozpinające ale tak aby wszystkie krawędzie w nim zawarte były kolejnymi ze zbioru posortowanych po wagach krawędzi. W ten sposób wszystkie krawędzie które nie znajdą się w drzewie będą miały wagi mniejsze od m lub większe od M. Jeśli uda się znaleźć takie drzewo zwracam sumę wag krawędzi w nim zawartych, a jeśli w takiej iteracji algrytmu Kruskala nie uda się znaleźć drzewa spełniającego warunki powtarzam działanie, ale startując od kolejnej krawędzi ze zbioru posortowanych. Jeśli nie znajdę takiego drzewa i krawędzi do przetestowania z kolejnej iteracji zostanię mniej niż V-1 zwracam None.

# Złożoność obliczeniowa:
# 1) Tworzenie i sortowanie grafu krawędzi: O(ElogE)
# 2) Algorytm Kruskala O(Vlog*E), bo przerywam jego działanie jeśli dodam V - natrafie na pierwszy cykl
# Kruskala wywołuję maksymalnie około E-V razy (start od kożdej możliwej krawędzi ale tak aby pozostało V-1 krawędzi)
#   - O((E-V)Vlog*E) = O(EVlog*E)
# Złożoność mojego rozwiązania szacuję na O(EVlog*E)

from kol2testy import runtests

def create_E(G):
    E = []
    for v in range(len(G)):
        for adj,w in G[v]:
            E.append((v,adj,w))
    
    for i in range(len(E)):
        E[i] = (min(E[i][0], E[i][1]), max(E[i][0], E[i][1]), E[i][2])
    E.sort()
    prev = E[0]
    E2 = [E[0]]
    for i in range(1, len(E)):
        if prev != E[i]:
            E2.append(E[i])
            prev = E[i]
    
    return E2

def beautree(G):
    E = create_E(G)
    E.sort(key=lambda x : x[2])
    n = len(G)

    parent = [i for i in range(n)]
    rank = [0]*n

    def find(x):
        nonlocal parent
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        nonlocal parent, rank
        x = find(x)
        y = find(y)

        if x == y: return False

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
        return True

    s = 0
    while s < len(E) - n + 1:
        w = 0
        v_cnt = 1
        for i in range(s, len(E)):
            if union(E[i][0], E[i][1]): 
                w += E[i][2]
                v_cnt += 1
            else: break
        
        if v_cnt == n: return w
        s += 1
        parent = [i for i in range(n)]
        rank = [0]*n

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )