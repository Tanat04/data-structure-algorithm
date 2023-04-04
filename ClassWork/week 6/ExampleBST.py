from BST import *

T = BST()

'''
The following code is a specific code that constructs a binary search tree
from the list x. However, it works ONLY BECAUSE the order of the list items
already allow this code to work correctly.

The code below will not work on a generic list. You will need to add
standard operations to BST for it to work on generic data.
'''

x = [56,26,200,18,28,190,213,12,24,27]
for each in x:
    Tree_Insert(T, node(each, None))

print("Printing out all the value: ")
Inorder_Tree_Walk(T.root)

Tree_Insert(T, node(44, None))

print("Search for 99: ", Tree_Search(T.root, 99))
Tree_Insert(T, node(99, None))
print("Search for 99: ", Tree_Search(T.root, 99))

print("Maximum: ", Tree_Maximum(T.root).key)
print("Minimum: ", Tree_Minimum(T.root).key)
print("Successor: ", Tree_Successor(T.root).key)
print("Predecessor: ", Tree_Predecessor(T.root).key)

print("Search for 213: ",Tree_Search(T.root, 213))
Tree_delete(T, node(213, None))
print("Search for 213: ",Tree_Search(T.root, 213))

