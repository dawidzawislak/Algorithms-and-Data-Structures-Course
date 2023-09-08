# Dawid Zawiślak
# Na początku za pomocą BFS kumuluje paliwo z każdej plamy na jednym z jej pól(tym na które najszybciej dotrze ciężarówka po drodze).
# Następnie podejściem zachłannym wybieram z których plam zbiore paliwo i ile zatrzymań jest konieczne.
# Robie to w następujący sposób: 
# Jeśli mam paliwo to poruszam się do przodu i zapisuje ilości paliwa jakie moge zebrac z miniętych plam w kolejce priorytetowej.
# Gdy w baku jest zero paliwa sciągam z kolejki największą ilość paliwa jakie mogłem zebrać z miniętych pól i zwiększam licnik postojów.

from zad8testy import runtests
from collections import deque
from queue import PriorityQueue

def set_fuel_level(T, i):
    n = len(T)
    m = len(T[0])
    moves = ((-1,0), (1,0), (0,1), (0,-1))
    
    level = T[0][i]
    T[0][i] = 0
    q = deque()
    q.append((0, i))
    while len(q) > 0:
        x,y = q.popleft()
        for dx,dy in moves:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < n and 0 <= ny < m and T[nx][ny] > 0:
                level += T[nx][ny]
                T[nx][ny] = 0
                q.append((nx,ny))
    
    T[0][i] = level


def plan(T):
    m = len(T[0])

    for i in range(m):
        if T[0][i] > 0:
            set_fuel_level(T, i)

    counter = 0
    fuel_level = 0
    gas_station_fuels = PriorityQueue()
    for i in range(m-1):
        if T[0][i] > 0:
            gas_station_fuels.put(-T[0][i])
        if fuel_level == 0:
            counter += 1
            fuel_to_get = -gas_station_fuels.get()
            fuel_level += fuel_to_get
        fuel_level -= 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )