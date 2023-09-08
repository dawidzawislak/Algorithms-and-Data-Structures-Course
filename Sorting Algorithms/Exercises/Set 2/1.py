"""
Proszę zaimplementować:
1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LList:
    def __init__(self, T):
        self.head = Node(None)
        ptr = self.head
        for v in T:
            ptr.next = Node(v)
            ptr = ptr.next

    def print(self):
        ptr = self.head.next
        while ptr != None:
            print(ptr.val, "->", end=" ")
            ptr = ptr.next
        print()

def merge(l1, l2):
    new_list = LList([])
    ptr = new_list.head
    p = l1.next
    q = l2.next

    while p and q:
        if p.val < q.val:
            ptr.next = p
            ptr = ptr.next
            p = p.next
        else:
            ptr.next = q
            ptr = ptr.next
            q = q.next
    
    if p: ptr.next = p
    elif q: ptr.next = q

    return new_list


def print_l(l):
        while l != None:
            print(l.val, "->", end=" ")
            l = l.next
        print()

def sort_list(l):
    ptrs = [l.head.next]
    prev = l.head.next.val
    ptr = l.head.next.next
    pptr = l.head.next
    while ptr != None:
        if ptr.val < prev:
            ptrs.append(ptr)
            pptr.next = None
        
        pptr = ptr
        prev = ptr.val
        ptr = ptr.next
    
    sorted_list = LList([])
    head = Node(None)
    for li in ptrs:
        head.next = li
        sorted_list = merge(sorted_list.head, head)
    
    l.head.next = sorted_list.head.next

# l1 = LList([1,3,7,13,17,18])
# l2 = LList([1,2,5,7,15])

# merged = merge(l1.head, l2.head)
# merged.print()

l = LList([3,23,7,13,5,17,18,1])
sort_list(l)
l.print()