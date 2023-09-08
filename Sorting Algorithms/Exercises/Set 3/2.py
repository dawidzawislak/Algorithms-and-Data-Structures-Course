"""
Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.
"""

import math
from io import StringIO

class Heap:
    def __init__(self):
        self.T = []

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def heapify_up(self):
        i = len(self.T)-1
        while i > 0:
            if self.T[self.parent(i)] > self.T[i]:
                self.T[self.parent(i)], self.T[i] = self.T[i], self.T[self.parent(i)]
            i = self.parent(i)
    
    def heapify_down(self):
        i = 0
        while self.left(i) < len(self.T):
            smaller_child_ind = self.left(i)
            if self.right(i) < len(self.T) and self.T[smaller_child_ind] > self.T[self.right(i)]:
                smaller_child_ind = self.right(i)
            if self.T[smaller_child_ind] < self.T[i]:
                self.T[smaller_child_ind], self.T[i] = self.T[i], self.T[smaller_child_ind]
                i = smaller_child_ind

    def extract_min(self):
        if len(self.T) == 0: return None

        val = self.T[0]
        self.T[0] = self.T[-1]
        self.T.pop()

        self.heapify_down()

        return val

    def insert(self, val):
        self.T.append(val)
        
        self.heapify_up()
    
    def print(self, total_width=60, fill=' '):
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.T):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)
        return




        

heap = Heap()

heap.insert(1)
heap.insert(5)
heap.insert(3)
heap.insert(-1)
heap.insert(10)

heap.print()
print(heap.extract_min())
print(heap.extract_min())
heap.print()