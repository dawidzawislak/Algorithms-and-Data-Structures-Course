# Dawid Zawiślak
# Dla każdego punktu liczę siłe iterując po pozostałych punktach i sprawdzając ile z nich dominuje. 
# Następnie w razie potrzeby aktualizuje zmienną w której zapisana jest maksymalna siła sprawdzonych wcześniej punktów.
# Złożoność O(n^2)

from egz2atesty import runtests

def dominance(P):
    n = len(P)
    
    maxcnt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j: continue
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                cnt += 1
        maxcnt = max(maxcnt, cnt)

    return maxcnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
