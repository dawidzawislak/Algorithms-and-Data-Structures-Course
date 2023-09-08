"""
Proszę zaimplementować algorytm sortowania listy jednokierunkowej. W szczególności należy:
1. Zdefiniować klasę w Pythonie realizującą listę jednokierunkową.
2. Zaimplementować wstawianie do posortowanej listy.
3. Zaimplementować usuwanie maksimum z listy.
4. Zaimplementować sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyższych funkcji.
5. Zaimplementować odwracanie listy.
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
    
    def insert_to_sorted(self, head, node):
        ptr = head
        while ptr.next != None and ptr.next.val < node.val:
            ptr = ptr.next
        
        to_ins = node
        to_ins.next = ptr.next
        ptr.next = to_ins

    def extract_max(self):
        ptr = self.head
        max_node = None
        max_val = -float("inf")
        prev_max_node = None
        while ptr.next != None:
            if ptr.next.val > max_val:
                max_val = ptr.next.val
                max_node = ptr.next
                prev_max_node = ptr
            ptr = ptr.next
        
        prev_max_node.next = max_node.next
        max_node.next = None
        return max_node.val

    def sort(self):        
        ptr = self.head.next

        new_head = Node(None)

        while ptr != None:
            to_ins = ptr
            ptr = ptr.next
            self.insert_to_sorted(new_head, to_ins)
        
        self.head.next = new_head.next
    
    def reverse(self):
        p = None
        q = self.head.next
        r = q.next

        while q != None:
            q.next = p
            p = q
            q = r
            if q != None:
                r = q.next

        self.head.next = p


T = [5,1,20,4,6,23,10]
llist = LList(T)

llist.print()

llist.insert_to_sorted(llist.head, Node(12))
llist.print()

#print(llist.extract_max())
#llist.print()

llist.sort()
llist.print()

llist.reverse()
llist.print()