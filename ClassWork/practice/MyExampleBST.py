from BST import *

x = [56,26,200,18,28,190,213,12,24,27]
Tree = BST()

for key in x:
    Tree.insert(key)#int


Tree.inorderedWalk()
print()

for key in x: 
    print(Tree.search(key))


print(Tree.minimum())
print(Tree.maximum())


print(Tree.successor(28))
print(Tree.predecessor(190))

Tree.insert(1)
Tree.insert(507)
Tree.insert(47)
Tree.inorderedWalk()


Tree.delete(56)
Tree.delete(190)
Tree.inorderedWalk()
