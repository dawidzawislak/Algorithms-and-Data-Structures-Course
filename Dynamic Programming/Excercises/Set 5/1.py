"""
Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów oraz sumy ich profitów.
"""

def knucksack(prices, weights, max_cap):
    n = len(prices)
    # f(i,b) = max zysk po rozpatrzeniu i przedmiotów oraz gdy w plecaku zostanie b miejsca
    F = [[-1]*(max_cap+1) for _ in range(n)]

    # base case
    F[0][max_cap] = 0
    if weights[0] <= max_cap:
        F[0][max_cap-weights[0]] = prices[0]

    # relation
    for i in range(1, n):
        for b in range(max_cap+1):
            if F[i-1][b] >= 0:
                F[i][b] = F[i-1][b]

                if b-weights[i] >= 0:
                    F[i][b-weights[i]] = F[i][b]+prices[i]
    
    # original
    return max(F[n-1])

w = [12,1,4,1,2]
p = [4,2,10,1,2]

mc = 15

print(knucksack(p, w, mc))