"""
Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        
        if q == None and p == None:
            return True
    
        if q == None or p == None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
if __name__=="__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right =  TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right =  TreeNode(3)

    print(Solution().isSameTree(p, q))