"""
Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
"""

def lider(A):
    n = len(A)
    candidate = A[0]
    cnt = 1

    for i in range(1, n-1):
        if A[i] == candidate:
            cnt += 1
        else:
            cnt -= 1
            if cnt == 0:
                candidate = A[i+1]
    
    cnt = 0
    for x in A:
        if x == candidate: cnt += 1

    return candidate if cnt > n//2 else None

print(lider([3, 2, 3, 2, 3]))