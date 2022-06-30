"""
Algorithm:
1. Class Node for node description
2. Class DoubleLinkedList for head, tail, 
3. Insert function to, 
 - create node 
 - insert first node, 
 - add node at the last position.
4. Reverse function by swapping
"""
from tempfile import tempdir


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        node = DoubleLinkedList(value)
        if self.head == None:
            self.head = node
            self.tail = node
        return 

        self.tail.next = temp
        node.prev
