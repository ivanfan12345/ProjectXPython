# coding=utf-8
__author__ = 'IFAN'
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

def delete_node(linkedList):
    print 'delete node in linkedlist'

def ivanLinkedList():
    head = Node(1)
    head.next = Node(1)
    head.next = Node(3)
    temp.next = Node(2)
    temp.next.next =  Node(3)
    temp.next.next.next = Node(4)
    temp.next.next.next.next = Node(5)

    while(temp.next !=  None):
        print temp.data
        temp =  temp.getNext()
    print temp.data

'''
Linked List
Implement a linked list (with insert and delete functions)
Find the Nth element in a linked list
Remove the Nth element of a linked list
Check if a linked list has cycles
Given a circular linked list, find the node at the beginning of the loop. Example: A-->B-->C --> D-->E -->C, C is the node that begins the loop
Check whether a link list is a palindrome
Reverse a linked list iteratively and recursively

CTCI – Chapter 2
2.1 Write code to remove duplicates from an unsorted linked list.
2.1b     How would you solve this problem if a temporary buffer is not allowed?
2.2 Implement an algorithm to find the kth to last element of a singly linked list.
2.3 Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a- >b- >d->e
2.4 Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
2.5 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the Ts digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
Output: 2 -> 1 -> 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
Output: 9 -> 1 -> 2.That is, 912.
2.6 Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.
DEFINITION Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A ->B->C->D->E-> C [the same C as earlier]
Output: C
2.7 Implement a function to check if a linked list is a palindrome.
'''