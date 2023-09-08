"""
Zadanie 6 (ścieżka w drzewie) Dane jest drzewo ukorzenione T , gdzie każdy wierzchołek v ma—
potencjalnie ujemną—wartość value(v). Proszę zaproponować algorytm, który znajduje wartość najbardziej
wartościowej ścieżki w drzewie T.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
        self.g = None
        self.f = None

class Node2:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        self.g = None
        self.f = None

def max_path(root):

    def g(v):
        if v == None: return 0

        if v.g == None: 
            v.g = v.val + max(g(v.left), g(v.right),0)
        
        return v.g
    
    def f(v):
        if v == None: return -float("inf")

        r = max(g(v.right), 0)
        l = max(g(v.left), 0)
        if v.f == None:
            v.f = max(v.val + r + l, f(v.right), f(v.left))
        
        return v.f

    return f(root)

def max_path_children(root):

    def g(v):
        if v == None: return 0

        if v.g == None: 
            maxv = 0
            for child in v.children:
                maxv = max(maxv, g(child))
            v.g = v.val + maxv
        
        return v.g
    
    def f(v):
        if v == None: return -float("inf")
        if v.f == None:
            g1 = 0
            g2 = 0
            maxf = -float("inf")
            for child in v.children:
                cv = g(child)
                if g1 < cv:
                    g2 = g1
                    g1 = cv
                elif g2 < cv:
                    g2 = cv
                maxf = max(maxf, f(child))
            v.f = max(v.val + g1+g2, maxf)
        
        return v.f

    return f(root)

root = Node(-4, 
            Node(10,
                Node(7,
                    Node(8,
                        Node(1,
                            Node(-5,
                                Node(-4)
                            )
                        ),
                        Node(-7, 
                            right=Node(1)
                            )
                    )
                ),
                Node(-5,
                     Node(-100),
                     Node(2,
                          Node(20),
                          Node(7)
                         )
                    )
                ),
            Node(-8)
            )

print(max_path(root))

root = Node2(20, [
    Node2(5, [
        Node2(30), 
        Node2(-20)
    ]), 
    Node2(-20, [
        Node2(1, [
            Node2(30), 
            Node2(22),
            Node2(-15)
        ]), 
    ]), 
    Node2(15),
    Node2(-10, [
        Node2(18),
        Node2(23),
        Node2(-20, [
            Node2(100)
        ]),
        Node2(-15)
    ])
])



print(max_path_children(root))