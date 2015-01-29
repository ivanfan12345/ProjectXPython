__author__ = 'IFAN'

class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.Tail = None

    def add_node(self,value):
        node = Node(value)
        #If the old list is none , set new node as the first node.
        if self.head == None:
            self.head = node
            self.tail - node
        else:
            self.tail.next = node
            self.head.next = node


from random import randint
'''
class Node:
    def __init__(self, value):
'''