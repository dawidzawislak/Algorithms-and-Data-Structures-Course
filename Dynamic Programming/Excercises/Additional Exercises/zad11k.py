from zad11ktesty import runtests
from math import ceil

# def knupsack(W,P,B):
#     n = len(W)
#     F = [[0]*(B+1) for _ in range(n)] 

#     for b in range(W[0], B+1):
#         F[0][b] = P[0]
    
#     for b in range(B+1):
#         for i in range(1, n):
#             F[i][b] = F[i-1][b]
#             if b - W[i] >= 0 and F[i-1][b-W[i]]+P[i] > F[i][b]:
#                 F[i][b] = F[i-1][b-W[i]]+P[i]

#     return F[n-1][B]
       


def kontenerowiec(T):
    n = len(T)
    max_w = (sum(T)+1)//2
    
    # F = [[0]*(max_w+1) for _ in range(n)] 

    # for b in range(T[0], max_w+1):
    #     F[0][b] = T[0]
    
    # for b in range(max_w+1):
    #     for i in range(1, n):
    #         F[i][b] = F[i-1][b]
    #         if b - T[i] >= 0 and F[i-1][b-T[i]]+T[i] > F[i][b]:
    #             F[i][b] = F[i-1][b-T[i]]+T[i]

    F = [[False]*(max_w+1) for _ in range(n)] 

    F[0][0] = True
    F[0][T[0]] = True
    
    for i in range(1, n):
        for b in range(max_w+1):
            if F[i-1][b] or (b - T[i] >= 0 and F[i-1][b-T[i]]):
                F[i][b] = True

    filled_to = None
    for b in range(max_w, -1, -1):
        if F[n-1][b]: 
            filled_to = b
            break

    return abs(sum(T)-2*filled_to)

runtests ( kontenerowiec )
    