import sys
sys.setrecursionlimit(10001)

class BST:
    def __init__(self): 
        self.root = None      

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None

def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)

def Tree_Search(x, k):
    if x == None:
        return None
    if k == x.key:
        return x.key
    if k < x.key:
        return Tree_Search(x.left, k)
    else:
        return Tree_Search(x.right, k)

def Tree_Minimum(x):
    while x.left != None:
        x = x.left
    return x

def Tree_Maximum(x):
    while x.right != None:
        x = x.right
    return x

def Tree_Successor(x):
    if x.right != None:
        return Tree_Minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y

def Tree_Predecessor(x):
    if x.left != None:
        return Tree_Maximum(x.left)
    y = x.p
    while y != None and x == y.left:
        x = y
        y = y.p
    return y

def Tree_Insert(Tree, value):
    y = None
    x = Tree.root
    while x != None:
        y = x
        if value.key < x.key:
            x = x.left
        else:
            x = x.right
    value.p = y
    if y == None:
        Tree.root = value
    elif value.key < y.key:
        y.left = value
    else:
        y.right = value

def Transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p
    return None

def Tree_delete(T, value):
    if value.left == None:
        Transplant(T, value, value.right)
    elif value.right == None:
        Transplant(T, value, value.left)
    else:
        y = Tree_Minimum(value.right)
        if y.p != value:
            Transplant(T, y, y.right)
            y.right = value.right
            y.right.p = y
        Transplant(T, value, y)
        y.left = value.left
        y.left.p = y
    return None