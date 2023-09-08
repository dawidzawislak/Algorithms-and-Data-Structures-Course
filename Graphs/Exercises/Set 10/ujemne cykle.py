from math import log2

def bellman_ford(E):
    n = 0

    for e in E:
        n = max(n, e[0], e[1])
    n += 1

    distance = [float("inf")]*n
    distance[0] = 0

    for i in range(n-1):
        for e in E:
            if distance[e[0]] + log2(e[2]) < distance[e[1]]:
                distance[e[1]] = distance[e[0]] + log2(e[2])
    
    for i in range(n-1):
        for e in E:
            if distance[e[0]] + log2(e[2]) < distance[e[1]]:
                return True
    
    return False


PLN = 0; EUR = 1; USD = 2; YEN = 3

K = [(PLN, EUR, 4.51), (PLN, USD, 3.68), (PLN, YEN, 0.034),
     (EUR, PLN, 0.22), (EUR, USD, 0.82), (EUR, YEN, 0.0075),
     (USD, PLN, 0.27), (USD, EUR, 1.22), (USD, YEN, 0.0091),
     (YEN, PLN, 29.83), (YEN, EUR, 133,47), (YEN, USD, 109.62)]

print(bellman_ford(K))