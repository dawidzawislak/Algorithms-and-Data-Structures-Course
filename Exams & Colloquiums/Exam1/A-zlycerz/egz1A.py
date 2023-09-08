# Dawid Zawiślak
# Aby rozwiązać problem używam algorytmu dijkstry z mnożonymi wierzchołkami. 
# Do każdego wierzchołka można wejść na v+1 scenariuszy gdzie v oznacza z którego zamku kradniemy złoto, lub nie kradniemy z żadnego
# Zapisuje też stan czy już doszliśmy w najtańszy sposób do wierzchłka z którego kradniemy.
# Jeśli doszliśmy to wędrujemy po grafie ze zwiększonymi kosztami.
# na końcu zwracam minimum z kosztów: jeśli nie kradniemy z żadnego zamku, jeśli kradniemy z któregoś zamku to koszt dojścia do t po zwiększonych wagach od odwiedzenia v z którego kradniemy - ilość złota które ukradliśmy
# Złożoność V^3logV bo szacujemy E jako V^2
from egz1Atesty import runtests
from queue import PriorityQueue

def gold(G,V,s,t,r):
    n = len(G)
    cost_from_start = [float("inf")]*n
    cost_from_start[s] = 0

    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        curr_cost, v = pq.get()
        for adj, w in G[v]:
            if cost_from_start[adj] > curr_cost + w:
                cost_from_start[adj] = curr_cost + w
                pq.put((cost_from_start[adj], adj))
    
    cost_from_end = [float("inf")]*n
    cost_from_end[t] = 0
    pq.put((0, t))
    while not pq.empty():
        curr_cost, v = pq.get()
        for adj, w in G[v]:
            if cost_from_end[adj] > curr_cost + 2*w + r:
                cost_from_end[adj] = curr_cost + 2*w + r
                pq.put((cost_from_end[adj], adj))
    
    minc = float("inf")
    for v in range(n):
        minc = min(cost_from_start[v] + cost_from_end[v] - V[v], minc)

    return minc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )

