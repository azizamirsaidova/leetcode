
class LinkedListNode(object):
   def __init__(self, x):
      self.val = x
      self.next = None

def remove_elements(head: LinkedListNode, val: int) -> x):
    dummy = LinkedListNode
    dummy.next = head

    curr = dummy

    #traverse the list
    while curr.next:
        if curr.next.val == val:
            #skip/remove that node
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(2)
node4 = LinkedListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = head