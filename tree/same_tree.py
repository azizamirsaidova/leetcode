"""
Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3] 
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

1) Recursively traverse the tree using Pre-Order traversal
    a) If the nodes from both trees are not None, and their values are equal -> Recur on their children
    b) Else -> return False
2) After trees have been fully traversed and no differences are discovered, return True

"""

a = [1,2,3]
b = [1,2,3] 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sameTree(a,b):
    if a is None and b is None:
        return True
    
    if a is not None and b is not None:
       return ((a.val == b.val) and sameTree(a.right,b.right) and sameTree(a.left,b.left))
    return False

a = Node(1)
b = Node(1)

a.left = Node(2)
a.right = Node(3)

b.left = Node(2)
b.right = Node(3)

if sameTree(a, b):
    print("Both trees are identical")
else:
    print ("Trees are not identical")
