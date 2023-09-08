# Radosław Rolka
from zad7testy import runtests
"""
legenda: -1 - pole niedostępne,
          0 - pole nieodwiedzone
          x - ile max komnat zostało odwiedzone przed
W algorytmie zaczynamy od przepisania wartosci z lewej kolumny powiększonych o 1. Nastepnie przechodzimy w gore i dol
i sprawdzamy czy da sie ta liczbe zwiekszyc poprzez uprzednie odwiedzenie komnat z dołu/góry. Po takim przejściu ustawiamy
result jako maksymalny rezultat z przejść [góra, dół]. 
złożoność: O( n^2 )
"""
"""
def maze(map):
    n = len(map)
    result = [[0 for _ in range(n)] for _ in range(n)]
    result_directed = [[[0, 0] for _ in range(n)] for _ in range(n)]
 
    for y in range(n):
        for x in range(n):
            if map[y][x] == '#':
                result[y][x] = -1
 
    # pierwsza kolumna
    for y in range(1, n):
        if result[y-1][0] == -1:
            result[y][0] = -1
        elif result[y][0] == -1:
            continue
        else:
            result[y][0] = result[y-1][0] + 1
 
    # cala macierz
    for x in range(1, n-1):
 
        # lewo
        for y in range(n):
            if result[y][x-1] == -1 or result[y][x] == -1:
                result_directed[y][x][0] = result_directed[y][x][1] = -1
            else:
                result_directed[y][x][0] = result_directed[y][x][1] = result[y][x-1] + 1
 
        # inkrementuj w dol
        for y in range(1, n):
            if result[y][x] == -1:
                continue
            elif result_directed[y-1][x][0] == -1:
                continue
            new = result_directed[y-1][x][0] + 1
            if new > result_directed[y][x][0]:
                result_directed[y][x][0] = new
 
        # inkrementuj w gore
        for y in range(n-2, -1, -1):
            if result[y][x] == -1:
                continue
            elif result_directed[y + 1][x][1] == -1:
                continue
            new = result_directed[y + 1][x][1] + 1
            if new > result_directed[y][x][1]:
                result_directed[y][x][1] = new
 
        # ustawianie max resulta
        for y in range(n):
            result[y][x] = max(result_directed[y][x])
 
    # ostatnia kolumna
    x = n-1
    # lewo
    for y in range(n):
        if result[y][x - 1] == -1 or result[y][x] == -1:
            result_directed[y][x][0] = result_directed[y][x][1] = -1
        else:
            result_directed[y][x][0] = result_directed[y][x][1] = result[y][x] = result[y][x - 1] + 1
 
    # dol
    for y in range(1, n):
        if result[y][x] == -1:
            continue
        elif result_directed[y - 1][x][0] == -1:
            continue
        new = result_directed[y - 1][x][0] + 1
        if new > result_directed[y][x][0]:
            result[y][x] = result_directed[y][x][0] = new
 
    if result[n-1][n-1] != 0:
        return result[n-1][n-1]
    else:
        return -1
"""
def maze(map):
    n = len(map)
    result = [[0]*n for _ in range(n)]
    result_directed = [[0, 0] for _ in range(n)]
 
    for y in range(n):
        for x in range(n):
            if map[y][x] == '#':
                result[y][x] = -1
 
    # pierwsza kolumna
    for y in range(1, n):
        if result[y-1][0] == -1:
            result[y][0] = -1
        elif result[y][0] == -1:
            continue
        else:
            result[y][0] = result[y-1][0] + 1
 
    # cala macierz
    for x in range(1, n-1):
 
        # lewo
        for y in range(n):
            if result[y][x-1] == -1 or result[y][x] == -1:
                result_directed[y][0] = result_directed[y][1] = -1
            else:
                result_directed[y][0] = result_directed[y][1] = result[y][x-1] + 1
 
        # inkrementuj w dol
        for y in range(1, n):
            if result[y][x] == -1:
                continue
            elif result_directed[y-1][0] == -1:
                continue
            new = result_directed[y-1][0] + 1
            if new > result_directed[y][0]:
                result_directed[y][0] = new
 
        # inkrementuj w gore
        for y in range(n-2, -1, -1):
            if result[y][x] == -1:
                continue
            elif result_directed[y + 1][1] == -1:
                continue
            new = result_directed[y + 1][1] + 1
            if new > result_directed[y][1]:
                result_directed[y][1] = new
 
        # ustawianie max resulta
        for y in range(n):
            result[y][x] = max(result_directed[y])
 
    # ostatnia kolumna
    x = n-1
    # lewo
    for y in range(n):
        if result[y][x - 1] == -1 or result[y][x] == -1:
            result_directed[y][0] = result_directed[y][1] = -1
        else:
            result_directed[y][0] = result_directed[y][1] = result[y][x] = result[y][x - 1] + 1
 
    # dol
    for y in range(1, n):
        if result[y][x] == -1:
            continue
        elif result_directed[y - 1][0] == -1:
            continue
        new = result_directed[y - 1][0] + 1
        if new > result_directed[y][0]:
            result[y][x] = result_directed[y][0] = new
 
    if result[n-1][n-1] != 0:
        return result[n-1][n-1]
    else:
        return -1
 
 
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)