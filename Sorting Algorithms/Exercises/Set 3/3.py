"""
Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać własny stos)
"""

def quick_sort(T, p, r):
    stack = [(p,r)]
    while len(stack) > 0:
        p,r = stack.pop()
        if p < r:
            q = partition(T, p, r)
            stack.append((p, q-1))
            stack.append((q+1, r))

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

T = [1,54,3,634,234,2,423]
quick_sort(T, 0, len(T)-1)

print(T)