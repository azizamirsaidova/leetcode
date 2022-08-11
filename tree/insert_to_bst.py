"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST.

Input: root = [4,2,7,1,3], val = 5
           4     
          / \
         2   7
        / \   
       1   3   
Output: [4,2,7,1,3,5]

1. If root is null -> return TreeNode(val)
2. If val > root.val -> go to insert into the right subtree
3. If val < root.val -> go to insert into the left subtree
4. Return root

Time Complexity: O(N)
Space Complexity: O(N)

"""


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val 
        self.right = right
        self.left = left

def insert_bst(self, root):
    if root is None:
        return Node(self.val)
    
    if self.val > root.val:
        insert_bst(self, root.right)
    
    if self.val < root.val:
        insert_bst(self, root.left)
    
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(insert_bst(self,root))
