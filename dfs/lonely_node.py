"""
Find All The Lonely Nodes

In a binary tree, a lonely node is a node that is the only child of its parent node. 
The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. 
Return the list in any order.

Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLonelyNodes(self, root):
        result = []
        
        self.dfs(root, result)
        
        return result
    
    def dfs(self, root, result):
        if root == None:
            return 
        
        if root.left == None and root.right:
            result.append(root.right.val)
        
        if root.right == None and root.left:
            result.append(root.left.val)
        
        self.dfs(root.left, result)
        self.dfs(root.right, result)

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right =  TreeNode(3)
    root.left.right = TreeNode(4)
    print(Solution().getLonelyNodes(root))