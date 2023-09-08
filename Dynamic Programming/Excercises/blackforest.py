def max_income(C):
    n = len(C)
    if n == 1: return C[0]
    F = [0]*n
    F[0] = C[0]
    F[1] = max(C[0], C[1])

    for i in range(2, n):
        F[i] = max(F[i-2]+C[i], F[i-1])
    
    return F[n-1]



T = [8, 12, 3, 4, 7, 1, 2, 10]

print(max_income(T))
