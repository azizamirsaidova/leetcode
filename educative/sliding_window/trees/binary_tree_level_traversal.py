
"""

1. Push the root to the queue
2. Keep iterating until the queue is empty
3. In each iteration, count the elements in the queue
4. Remove levelsiz nodes from the queue and push their value
in an array to represent the current level
5. After removing each node from the queue, insert both of its 
children into the queue
6. If the queue is not empty, repeat from step 3 for the next level.

queue = deque()
queue.append(root)
while queue != None:
    levelSize = len(queue)
    currLevel = []
    for i in range(levelSize):
        currNode = queue.popleft()
        currLevel.append(currNode)

    if currNode.left:
        queue.append(currNode.left)
    if currNode.right:
        queue.append(currNode.right)
    result.append(currLevel)
    
return result

The time complexity of the above algorithm is 
O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

The space complexity of the above algorithm will be O (N)
as we need to return a list containing the level order traversal. We will also need 
O(N) space for the queue. Since we can have a maximum of N/2
nodes at any level (this could happen only at the lowest level), therefore we will need 
space to store them in the queue.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(currentLevel)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()