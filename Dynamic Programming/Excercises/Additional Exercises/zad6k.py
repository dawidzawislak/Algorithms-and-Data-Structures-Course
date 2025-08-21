from zad6ktesty import runtests 

def haslo ( S ):
    print(S)
    n = len(S)
    F = [0]*n 
    F[0] = 1
    F[1] = 2 if int(S[0:2]) <= 26 else 1
    
    for i in range(2, n):
        if S[i-1:i+1] == "00": return 0
        if S[i] == "0" and int(S[i-1]) in [1,2]: F[i] = F[i-2]
        elif S[i-1] == "0": 
            if int(S[i-2]) > 2: return 0
            F[i] = F[i-1] 
        elif int(S[i-1:i+1]) <= 26: F[i] = F[i-1] + F[i-2]
        elif int(S[i-1:i+1]) > 26: F[i] = F[i-1]
        else: return 0
    print(F)
    return F[n-1]

runtests ( haslo )