class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
        if head == None:
            return 

        curr = head
        next = None
        prev = None
        count = 0

        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            count += 1

            # next is now a pointer to (k+1)th node
            # recursively call for the list starting
            # from current. And make rest of the list as
            # next of first node
        if next is not None:
            head.next = self.reverse(next,k)
        return prev 

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end =" ")
            temp = temp.next


llist = LinkedList()
llist.head = Node('10')
llist.head.next = Node('20')
llist.head.next.next = Node('30')
llist.head.next.next.next = Node('40')
llist.head.next.next.next.next = Node('50')
llist.head.next.next.next.next.next = Node('60')

print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
 
print ("\nReversed Linked list")
llist.printList()
        