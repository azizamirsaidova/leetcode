"""
Algorithm:
1. Traverse the list
2. Swap next and prev pointers for each node
3. Update the head pointer to point to the last node

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        curr = self.head

        # Swap next and prev for all nodes of
        # doubly linked list
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next 
            curr.next = temp

            curr = curr.prev

        if temp is not None:
            self.head = temp.prev

    def push(self, node):
        node = Node(node)
        node.next = self.head
        if self.head is not None:
            self.head.prev  = node
        
        self.head = node


    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

dll = DoubleLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)


dll.printList()
dll.reverse()
print(" ")
print("After reversing")
dll.printList()


