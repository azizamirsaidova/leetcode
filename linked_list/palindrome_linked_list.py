class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def iSpalindrome(self):
        node = self.head
        length = 0
        stack = []

        # Add list values to comp
        while node:
            stack.append(node.data)
            node = node.next
            length += 1

        # Traverse the list by checking the values in stack
        node = self.head 
        for i in stack[::-1]:
            if (i != node.data):
                return False
            node = node.next
        return True
    
# Add values to data a
llist = LinkedList()
llist.head = Node('1')
llist.head.next = Node('3')
llist.head.next.next = Node('5')
llist.head.next.next.next = Node('3')
llist.head.next.next.next.next = Node('1')

if (llist.iSpalindrome()):
    print("It is Palindrome")
else:
    print("It is not a Palindrome")