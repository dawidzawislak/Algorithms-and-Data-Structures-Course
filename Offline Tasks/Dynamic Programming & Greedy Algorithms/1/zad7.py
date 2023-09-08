# Dawid Zawiślak
# W rozwiązaniu do każdego pola na planszy przypisuje największą ilość ruchów jaką mogę wykonać aby znaleźć się na danym polu wykorzystując jedynie kolumny na lewo i kolumne w której znajduje się pole.
# Do komnaty można wejść maksymalnie raz czyli jeśli zaczniemy iść w dół nie możemy się "cofnąć" w górę i analogicznie w przeciwnym kierunku.
# Inicjalizuje wszystkie odległości w tabeli F na -1 a dla pola (0,0) na 0.
# Jako przypadek progowy ustawiam po koleji odległości na dane pola w dół w pierwszej kolumnie dopuki nie natrafie na zakmniętą komnate.
# Następnie dla każdej kolumny zaczynając od drugiej każdemu polu w niej przypisuje maksimum z {odległości z lewego pola + 1, odległości z górnego(dolnego) pola + 1 jeśli ustalam że idę w dół(górę)}
# Realizuje to w taki sposób, że jeśli na pole po lewej strone dało się dojść ustawiam rozpartywanemu polu wartość z lewej + 1, następnie patrzę na pole nad danym i jeśli odległość na nie + 1 jest większa niż aktualnie ustawiona przestawiam ją.
# Później rozważam przypadek że dochodzę na dane pole od dołu i alternatywną odległość wstawiam do tablicy pomocniczej alt_dist.
# Jeśli w ten sposób mogę dojść na dane pole przechodząc przez więcej komnat aktualizuje odległość w głównej tabeli do zpamiętywania.
# Po przejściu w taki sposób przez wszystkie kolumny zwracam wartość F[n-1][n-1]
# Złośoność obliczeniową algorytmu szacuje na O(n^2)
from zad7testy import runtests

def maze( L ):
    n = len(L)
    F = [[-1]*n for _ in range(n)]

    for i in range(n):
        if L[i][0] == "#": break
        F[i][0] = i
    
    for c in range(1,n):
        for r in range(n):
            if L[r][c] == "#": continue
            if F[r][c-1] != -1: F[r][c] = F[r][c-1]+1
            
            if r-1 >= 0 and F[r-1][c] != -1 and F[r-1][c]+1 > F[r][c]:
                F[r][c] = F[r-1][c]+1

        alt_dist = [-1]*n
        for r in range(n-1,-1,-1):
            if L[r][c] == "#": continue
            if F[r][c-1] != -1: alt_dist[r] = F[r][c-1]+1
            
            if r+1 < n and alt_dist[r+1] != -1 and alt_dist[r+1]+1 > alt_dist[r]:
                alt_dist[r] = alt_dist[r+1]+1
            
            if alt_dist[r] > F[r][c]: F[r][c] = alt_dist[r]

    return F[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
