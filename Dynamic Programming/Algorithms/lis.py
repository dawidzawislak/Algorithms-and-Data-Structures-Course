def lis(T):
    n = len(T)

    dp = [1]*n
    parent = [None]*n

    for i in range(1,n):
        for j in range(i):
            if T[i] > T[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    return max(dp), parent, dp.index(max(dp))

T = [2,1,4,3,1,5,2,7,8,3]
maxl,parent,ind = lis(T)

p = [T[ind]]
curr = ind
while parent[curr] != None:
    p.append(T[parent[curr]])
    curr = parent[curr]

p.reverse()

print(maxl, p)