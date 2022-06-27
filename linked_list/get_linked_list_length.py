""" Algorithm:
    a. Iterative Approach:

    1. Initialize a count as zero
    2. Initialize a node pointer, current = head
    3. Do the following while current is not NULL
        a. current = current.next
        b. count++
    4. Return count """

class Node(object):
    # Creating a node
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

def getLength(node):

    count = 0
    while node != 0:
        count += 1
        node = node.next

    return count

linked_list = LinkedList()

# Assign data values
linked_list.head = n1
n1 = Node(val=1)
n2 = Node(val=2)
n3 = Node(val=3)

n1.next = n2
n2.next = n3
print(f"Test 2 - getLength returned: {getLength(n1)}, expected: 3")
