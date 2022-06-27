""" Algorithm
1. Change next pointer of kth node to NULL, 
2. the next pointer of the last node should point to previous head node, 
3. and finally, change the head to (k+1)th node. 

So we need to get hold of three nodes: 
1. kth node, 
2. (k+1)th node, 
3. and last node. 

Traverse the list from the beginning and stop at kth node. 
Store pointer to kth node. We can get (k+1)th node using kthNode->next. 
Keep traversing till the end and store a pointer to the last node also. 
Finally, change pointers as stated above.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def rotate(self, k):
        if  k == 0:
            return 
        
        curr = self.head
        count = 1
        while (count <k and curr is not None):
            curr = curr.next
            count +=1

        # If current is None, k is greater than or equal 
        # to count of nodes in linked list. Don't change
        # the list in this case
        if curr is None:
            return 

        kthNode = curr
        while curr.next is not None:
            curr = curr.next

        curr.next = self.head
        self.head = kthNode.next
        kthNode.next = None

llist = LinkedList()
llist.head = Node('10')
llist.head.next = Node('20')
llist.head.next.next = Node('30')
llist.head.next.next.next = Node('40')
llist.head.next.next.next.next = Node('50')
llist.head.next.next.next.next.next = Node('60')

print("Given linked list")
llist.printList()

llist.rotate(4)

print("Rotated linked list")
llist.printList()

