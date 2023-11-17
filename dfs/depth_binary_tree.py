"""
Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0 
        
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1
        
        return max(left, right)

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right =  TreeNode(3)
    root.left.right = TreeNode(4)
    print(Solution().maxDepth(root))