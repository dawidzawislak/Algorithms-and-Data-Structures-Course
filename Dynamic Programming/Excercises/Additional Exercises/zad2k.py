from zad2ktesty import runtests

def palindrom( S ):
    n = len(S)

    F = [[False]*n for _ in range(n)]
    
    for i in range(n):
        F[i][i] = True
    
    for l in range(2, n):
        for i in range(n-l+1):
            j = i + l-1

            if S[i] == S[j]:
                if l == 2:
                    F[i][j] = True
                else:
                    F[i][j] = F[i+1][j-1]
            else:
                F[i][j] = False
    
    maxl = 0
    maxi = -1
    for i in range(n):
        for j in range(i+1, n):
            if F[i][j] and j+1-i > maxl:
                maxl = j+1-i
                maxi = i
                
    return S[maxi:maxi+maxl]


runtests ( palindrom )