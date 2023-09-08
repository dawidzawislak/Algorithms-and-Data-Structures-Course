# Dawid Zawiślak
# Problem z zadania sprowadza się do znalezienia maksymalnego skojarzenia w grafie dwudzielnym(wierzchołki pracowników i wierzchołki maszyn)
# Na początku dla każdego pracownika przydzielam zachłannie wolne maszyny i inkrementuje licznik dopasowań(pairs).
# Następnie dla każdego pracownika, który jeszcze nie ma przydzielonej maszyny próbuję przydzielić maszynę "przepinając" rekurencyjnie pracownika zajmującego dane stanowisko na inne - wolne. Jeśli uda się w ten sposób znaleźć nowe dopasowanie funkcja find_match zwraca 1 i inkrementuje licznik dopasowań. 
# Tablica visited_machines sprawia, że gdy "przepinamy" pracownika trafia on do innej maszyny.
# Po wywołaniu jej dla każdego z nieprzydzielonych pracowników zwracam ilość dopasowań które udało się utworzyć.
from zad6testy import runtests

def binworker( M ):
    n = len(M)
    matches = [None]*n
    matched_worker = [False]*n

    def find_match(worker, visited_machines):
        nonlocal M, matches
        
        for m in M[worker]:
            if not visited_machines[m]:
                visited_machines[m] = True
                if matches[m] == None or find_match(matches[m], visited_machines):
                    matches[m] = worker
                    return 1
        return 0

    pairs = 0

    for worker in range(n):
        for m in M[worker]:
            if matches[m] == None:
                matches[m] = worker
                matched_worker[worker] = True
                pairs += 1
                break

    for worker in range(n):
        if not matched_worker[worker]:
            visited_machines = [False]*n
            pairs += find_match(worker, visited_machines)

    return pairs

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
