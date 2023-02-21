"""
You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.


1. from left to right
2. right to left for the next level


Plan:
1. push the root to queue 
2. while queue is not empty
3. get the lengths of the queue
4. for each iteration of the lengthsize, 
    remove the lengthsize from the queue and assign to currentNode
5. and push it to the currentLevel to represent the current level of the queue 
5. push first: left and right child
        then: right and left child to the queue
"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left, self.right = None, None

def traversal(root):
    result = []

    queue = deque()
    queue.append(root)
    leftToRight = True
    while queue:
        lenSize = len(queue)
        currentLevel = deque()
        for _ in range(lenSize):
            currNode = queue.popleft()
            

            if leftToRight:
                currentLevel.append(currNode.val)
            else:
                currentLevel.appendleft(currNode.val)
            
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        
        result.append(list(currentLevel))
        # reverse the traversal direction
        leftToRight = not leftToRight
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: "+ str(traversal(root)))

main()