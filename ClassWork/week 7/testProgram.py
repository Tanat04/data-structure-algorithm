import random
import time

from BinarySearchTree import *

#Import Binary Search Tree
bst = BSTree()
a = []

#Creating random numbers
for i in range(16):
    a.append(random.randrange(500))
print(a)

random.shuffle(a)
print(a)

#Inserting random numbers into the tree
for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)

bst.print_BSTree()

#This is the worst case of BST
bst2 = BSTree()
for k in range(1,11):
    x = BST_Node(k)
    bst2.Tree_Insert(x)

bst2.Tree_Delete(bst2.Tree_Search(9))
bst2.print_BSTree()

#Inserting numbers in tree
def insertBst(start, end, bst):
    for k in range(start, end):
        x = BST_Node(k)
        bst.Tree_Insert(x)
    #bst.print_BSTree()

#Searching the numbers in the tree
def searchBst(n, bst):
    counter = 0 
    k = 2*n
    for i in range(n): 
        v = random.randint(0, k) 
        x = bst.Tree_Search(v)    
        if x != None: 
            counter += 1 
    print(counter)

print("Binary Search Tree:")

#Searching for 1000N case
st = time.process_time()

bst1000 = BSTree()
insertBst(1, 1000, bst1000)
searchBst(1000, bst1000)

et = time.process_time()
print(et - st,"for n = 1000\n")

#Searching for 2000N case
st = time.process_time()

bst2000 = BSTree()
insertBst(1, 2000, bst2000)
searchBst(2000, bst2000)

et = time.process_time()
print(et - st,"for n = 2000\n")

#Searching for 4000N case
st = time.process_time()

bst4000 = BSTree()
insertBst(1, 4000, bst4000)
searchBst(4000, bst4000)

et = time.process_time()
print(et - st,"for n = 4000\n")

#Searching for 8000N case
st = time.process_time()

bst8000 = BSTree()
insertBst(1, 8000, bst8000)
searchBst(8000, bst8000)

et = time.process_time()
print(et - st," for n = 8000\n")

# ---- RB Tree -----

# Inserting and deleting numbers from RB tree after inserting into it
from RedBlackTree import *

rbt = RBTree()
a = [i for i in range(5,60,5)]
print(a)
for k in a:
    x = RB_Node(k)
    rbt.RB_Insert(x)
rbt.print_RBTree()
rbt.delete(35)
rbt.print_RBTree()

# another example for RBTree
rbt2 = RBTree()
for i in range(1,11):
    x = RB_Node(i)
    rbt2.RB_Insert(x)

rbt2.print_RBTree()
rbt2.delete(9)
rbt2.print_RBTree()

#Inserting numbers in tree
def insertRBTree(start, end, rbt):
    for k in range(start, end):
        x = RB_Node(k)
        rbt.RB_Insert(x)
    #rbt.print_RBTree()

#Searching the numbers in the tree
def searchRBTree(n, rbt):
    counter = 0 
    k = 2*n    
    for i in range(n): 
        v = random.randint(0, k) 
        x = rbt.Tree_Search(v)  
        if x != rbt.NULL: 
            counter += 1 
    print(counter)

print("Red Black Tree:")
#Searching for 1000N case
st = time.process_time()

rbt1000 = RBTree()
insertRBTree(1, 1000, rbt1000)
searchRBTree(1000, rbt1000)

et = time.process_time()
print(et - st,"for n = 1000\n")

#Searching for 2000N case
st = time.process_time()

rbt2000 = RBTree()
insertRBTree(1, 2000, rbt2000)
searchRBTree(2000, rbt2000)

et = time.process_time()
print(et - st,"for n = 2000\n")

#Searching for 4000N case
st = time.process_time()

rbt4000 = RBTree()
insertRBTree(1, 4000, rbt4000)
searchRBTree(4000, rbt4000)

et = time.process_time()
print(et - st,"for n = 4000\n")

#Searching for 8000N case
st = time.process_time()

rbt8000 = RBTree()
insertRBTree(1, 8000, rbt8000)
searchRBTree(8000, rbt8000)

et = time.process_time()
print(et - st,"for n = 8000\n")