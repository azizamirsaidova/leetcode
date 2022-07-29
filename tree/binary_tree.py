"""
Depth First Traversals: 
(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
Breadth-First or Level Order Traversal: 1 2 3 4 5 

Example: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


Preorder (Root, Left, Right)
Preorder (Root, Right, Left)
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def inOrder(root):
    
    if root:
        inOrder(root.left)

        print(root.val)

        inOrder(root.right)

def preOrder(root):
    
    if root:

        print(root.val)

        inOrder(root.left)

        inOrder(root.right)

def posOrder(root):
    
    if root:

        inOrder(root.left)

        inOrder(root.right)

        print(root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder")
print(inOrder(root))

print("PreOrder")
print(preOrder(root))

print("PostOrder")
print(posOrder(root))


    
