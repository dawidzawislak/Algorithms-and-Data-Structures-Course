def change(amount, coins):
    F = [[0]*(amount+1) for _ in range(len(coins))]

    for i in range(1, amount+1):
        if i % coins[0] == 0: F[0][i] = 1
    
    for k in range(amount+1):
        for i in range(1, len(coins)):
            for j in range(1, coins[i]+1):
                val = F[i-1][k]
                if k-j >= 0:
                    val = F[i-1][k-j] + F[i-1][j]
                
                F[i][k] = max(F[i][k], val)
    return F[len(coins)-1][amount]

T = [3]
k= 10

print(change(k,T))