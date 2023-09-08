"""
Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla dwuwymiarowej
wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1 , . . . , pn } przedmiotów i dla każdego
przedmiotu pi dane sa nastepujace trzy liczby:
1. v(pi ) - wartość przedmiotu,
2. w(pi ) - waga przedmiotu, oraz
3. h(pi ) - wysokość przedmiotu.
Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
jego poprawność.
"""

def knucksack_2d(V, W, H, maxw, maxh):
    n = len(V)

    F = [[[0]*(maxh+1) for _ in range(maxw+1)] for _ in range(n)] # f(i,w,h)
    parent = [[[[None]*3  for _ in range(n)] for _ in range(maxh+1)] for _ in range(maxw+1)]

    #if czy miesci sie pierwszy
    for w in range(W[0], maxw+1):
        for h in range(H[0], maxh+1):
            F[0][w][h] = V[0]
    
    for w in range(maxw+1):
        for h in range(maxh+1):
            for i in range(1, n):
                F[i][w][h] = F[i-1][w][h]
                parent[w][h][i] = (w, h, i-1)
                if w - W[i] >= 0 and h - H[i] >= 0 and F[i][w][h] < F[i-1][w-W[i]][h-H[i]]+V[i]:
                    F[i][w][h] = F[i-1][w-W[i]][h-H[i]]+V[i]
                    parent[w][h][i] = (w-W[i], h-H[i], i-1)

    maxv = 0
    maxwi, maxhi = None, None
    ind = None
    for w in range(maxw+1):
        for h in range(maxh+1):
            for i in range(n):
                if maxv < F[i][w][h]:
                    maxv = F[i][w][h]
                    maxwi, maxhi = w, h
                    ind = i
                    
    path = []
    while parent[maxwi][maxhi][ind][0] != None and parent[maxwi][maxhi][ind][1] != None and parent[maxwi][maxhi][ind][2] != None:
        w,h = parent[maxwi][maxhi][ind][0:2]
        if w != maxwi and h != maxhi:
            path.append(ind)
        maxwi, maxhi,ind = parent[maxwi][maxhi][ind]

    return maxv,path



P = [4, 10, 2, 3, 8]  #21
W = [10, 4, 1, 2, 6] # 12
H = [3, 9, 12, 4, 2] # 14

MaxW = 12
MaxH = 20

print(knucksack_2d(P, W, H, MaxW, MaxH))
