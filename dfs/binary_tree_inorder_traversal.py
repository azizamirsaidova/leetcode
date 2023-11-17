"""
Pre-order Traversal: 
1. get node's value
2. print left subtree
3. print right subtree

In-order Traversal: 
1. print left subtree
2. get node's value
3. print right subtree

Post-order Traversal: 
1. print left subtree
2. print right subtree
3. get node's value

Given the root of a binary tree, return the inorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [1,3,2]
"""


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root == None:
            return root
        
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left =  TreeNode(3)
    print(Solution().inorderTraversal(root))
