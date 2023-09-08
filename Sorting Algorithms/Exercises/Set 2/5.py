"""
Dany jest ciąg przedziałów domkniętych [a1 , b1 ], . . . , [an , bn ]. Proszę zapropnować algorytm, który znajduje taki przedział [at , bt ], w którym w całości zawiera się jak najwięcej innych przedziałów.
"""

intervals = [(0,2), (3,5), (1,7), (5,7), (8,10), (6,11),(7,10), (8,9)]

intervals.sort(key = lambda x: x[1])
intervals.sort(key = lambda x: x[0])

print(intervals)

maxc = 0
cnt = 0
prev_int = intervals[0]
maxi = None

for i in range(1, len(intervals)):
    if intervals[i][0] >= prev_int[0] and intervals[i][1] <= prev_int[1]:
        cnt += 1
    else:
        if maxc < cnt: 
            maxc = cnt
            maxi = prev_int
        prev_int = intervals[i]
        cnt = 0

if maxc < cnt: 
    maxc = cnt
    maxi = prev_int

print(maxc, maxi)