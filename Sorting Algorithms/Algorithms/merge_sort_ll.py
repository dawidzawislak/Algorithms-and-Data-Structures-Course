# --- Linked List implementation ----------------------
class Node:
    def __init__(self, v):
        self.next = None
        self.val = v

def make_l(t):
    s = Node(t[0])
    first = s
    for e in t[1:]:
        s.next = Node(e)
        s = s.next
    return first

def print_l(p):
    print(p.val, end=" -> ")
    p = p.next
    while p.next != None:
        print(p.val, end=" -> ")
        p = p.next
    print(p.val)

# --- Merge Sort implementation -----------------------
def merge(l1, l2):
    if l1 == None and l2 == None:
        return None
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    head = Node(None)
    res = head
    while l1 and l2 :
        if l1.val <= l2.val:
            res.next = l1
            res = res.next
            l1 = l1.next
        elif l1.val > l2.val:
            res.next = l2
            res = res.next
            l2 = l2.next
    
    if l1:
        res.next = l1
    elif l2:
        res.next = l2
    
    return head.next

def slice(ptr):
    if ptr == 0: return None, None
    p = ptr
    while p.next:
        if p.val > p.next.val:
            q = p.next
            p.next = None
            return ptr, q
        p = p.next
    return ptr, None

def merge_sort(ptr):
    while True:
        res = Node(None)
        tail = res
        merges_cnt = 0
        while ptr:
            a, ptr = slice(ptr)
            b, ptr = slice(ptr)
            tail.next = merge(a, b)
            while tail.next:
                tail = tail.next
            merges_cnt += 1
            if merges_cnt == 1: return res
        ptr = res.next


T = [1,3,9,12,2,3,7,15]
ptr = make_l(T)
print_l(ptr)
merge_sort(ptr)
print_l(ptr)