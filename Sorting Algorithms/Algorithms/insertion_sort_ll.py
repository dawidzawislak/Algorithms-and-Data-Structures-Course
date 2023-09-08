# --- Linked List implementation ----------------------
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def make_l(t):
    s = Node(t[0])
    first = s
    for e in t[1:]:
        s.next = Node(e)
        s = s.next
    return first

def print_l(p):
    p = p.next
    while p.next != None:
        print(p.val, end=" -> ")
        p = p.next
    print(p.val)

def print_l_wo_guard(p):
    while p.next != None:
        print(p.val, end=" -> ")
        p = p.next
    print(p.val)


# -- Extract max from ll ------------------
def extract_max(guard_ptr: Node):
    node_b4_max = guard_ptr

    while guard_ptr.next != None:
        if guard_ptr.next.val > node_b4_max.next.val:
            node_b4_max = guard_ptr
        guard_ptr = guard_ptr.next
    
    max_node = node_b4_max.next
    node_b4_max.next = max_node.next
    max_node.next = None
    return max_node

# t = [None,1,4,5,3,7,6,5,4,3]
# ptr = make_l(t)
# print_l(ptr)
# print_l_wo_guard(extract_max(ptr))
# print_l(ptr)

def insert_sorted(guard_ptr : Node, new_node : Node):
    while guard_ptr.next != None and guard_ptr.next.val < new_node.val:
        guard_ptr = guard_ptr.next
    new_node.next = guard_ptr.next
    guard_ptr.next = new_node

# SORT
def insertion_sort(head: Node):
    A = Node(None)
    ptr = head
    while ptr.next:
        p = ptr.next
        ptr.next = p.next
        insert_sorted(A, p)

    head.next = A.next


t = [None,1,4,5,3,7,6,5,4,3]
ptr = make_l(t)
print_l(ptr)
insertion_sort(ptr)
print_l(ptr)