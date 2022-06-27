class Node(object):
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new
    # node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            temp = temp.next

    def find_loop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            
            s.add(temp)

            temp = temp.next
        return False

llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(30)

llist.head.next.next.next.next = llist.head

if (llist.find_loop()):
    print("Loop is found")
else: 
    print("No Loop")
        
  
