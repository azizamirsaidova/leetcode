"""
1. Go root of the tree, first element of the array
2. add to array, 
3. retrieve to child node
4. pop the first element, and get the child node 

"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def bst(root):

    if root:

        print(root.val)

        bst(root.left)

        bst(root.right)

def bst_queue(root):
    # if root is None:
    #     return 
    # print("after none")
    # print(queue)

    queue = [root]
    result = []
    while len(queue) !=0:
        
        curr_node = queue.pop(0)
        if curr_node.left is not None:
            queue.append(curr_node.left)
            # print("left")
            # print(queue)

        if curr_node.right is not None:
            queue.append(curr_node.right)
            # print("right")
            # print(queue)

        bst_queue(curr_node.right, root)
    return queue

root = Node(2)
root.left = Node(1)
root.right = Node(3)

queue = [root]
# curr_node = root

print(bst_queue(root=root))

# print("BST")
# print(bst(root))

