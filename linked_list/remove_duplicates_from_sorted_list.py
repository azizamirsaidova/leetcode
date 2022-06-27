""" Algorithm
1. Traverse the list from the head (or start) node. 
2. While traversing, compare each node with its next node. 
3. If the data of the next node is the same as the current node
then delete the next node. 
4. Before we delete a nodewe need to store the next pointer of the node """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert a new node
    # at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Given a reference to the head of a
    # list and a key, delete the first
    # occurrence of key in linked list
    # def deleteNode(self, key):
    #     curr = self.head
        
    #     # If head node itself holds the
    #     # key to be deleted
    #     if (curr is not None):
    #         if curr.data == key:
    #             self.head = curr.next
    #             curr = None
    #             return 
       
    #    # Search for the key to be deleted,
    #     # keep track of the previous node as
    #     # we need to change 'prev.next'
    #     while (curr is not None):
    #         if curr.data == key:
    #             break
    #         prev = curr
    #         curr = curr.next 
        
    #     # if key was not present in
    #     # linked list
    #     if curr == None:
    #         return 
    #     prev.next = curr.next
    #     curr = None
    
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
    
    def removeDuplicates(self):
        curr = self.head
        if curr is None:
            return 
        while curr.next is not None:
            if curr.data == curr.next.data:
                new = curr.next.next
                curr.next = None
                curr.next = new
            else:
                curr = curr.next
        return self.head

llist = LinkedList()
llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print ("Created Linked List: ")
llist.printList()

print("Linked List after removing",
             "duplicate elements:")
llist.removeDuplicates()
llist.printList()