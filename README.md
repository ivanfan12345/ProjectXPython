# PythonProjextX
Python 101

I ARE Python NOOB.

Solving these questions to learn the syntactical nature of the beautiful language we know and love as Python.

General
1.	Find the most frequent integer in an array
2.	Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
3.	Given 2 integer arrays, determine if the 2nd array is a rotated version of the 1st array. Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
4.	Write fibonacci iteratively and recursively (bonus: use dynamic programming)
5.	Find the only element in an array that only occurs once.
6.	Find the common elements of 2 int arrays
7.	Implement binary search of a sorted array of integers
8.	Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
9.	Use dynamic programming to find the first X prime numbers
10.	Write a function that prints out the binary form of an int
11.	Implement parseInt
12.	Implement squareroot function
13.	Implement an exponent function (bonus: now try in log(n) time)
14.	Write a multiply function that multiples 2 integers without using *
15.	HARD: Given a function rand5() that returns a random int between 0 and 5, implement rand7()
16.	HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)
Arrays and Strings
1.	Find the first non-repeated character in a String
2.	Reverse a String iteratively and recursively
3.	Determine if 2 Strings are anagrams
4.	Check if String is a palindrome
5.	Check if a String is composed of all unique characters
6.	Determine if a String is an int or a double
7.	HARD: Find the shortest palindrome in a String
8.	HARD: Print all permutations of a String
9.	HARD: Given a single-line text String and a maximum width value, write the function 'String justify(String text, int maxWidth)' that formats the input text using full-justification, i.e., extra spaces on each line are equally distributed between the words; the first word on each line is flushed left and the last word on each line is flushed right

1.	Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 
2.	Implement a function void reverse(char* str) in C or C++ which reverses a null- terminated string. 
3.	Given two strings, write a method to decide if one is a permutation of the other. 
4.	Write a method to replace all spaces in a string with'%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. (Note: if imple- menting in Java, please use a character array so that you can perform this opera- tion in place.)
 EXAMPLE
 Input: "Mr John Smith
 Output: "Mr%20Dohn%20Smith"
5.	Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the orig- inal string, your method should return the original string. 
6.	Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
7.	Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
8.	Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to isSubstring (e.g.,"waterbottle"is a rota- tion of "erbottlewat"

Linked List

1.	Implement a linked list (with insert and delete functions)
2.	Find the Nth element in a linked list
3.	Remove the Nth element of a linked list
4.	Check if a linked list has cycles
5.	Given a circular linked list, find the node at the beginning of the loop. Example: A-->B-->C --> D-->E -->C, C is the node that begins the loop
6.	Check whether a link list is a palindrome
7.	Reverse a linked list iteratively and recursively


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

Stacks and Queues 

1.	Implement a stack with push and pop functions
2.	Implement a queue with queue and dequeue functions
3.	Find the minimum element in a stack in O(1) time
4.	Write a function that sorts a stack (bonus: sort the stack in place without extra memory)
5.	Implement a binary min heap. Turn it into a binary max heap.
HARD: Implement a queue using 2 stacks


3.1 Describe how you could use a single array to implement three stacks.
          3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time. 
     3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOf Stacks that mimics this. SetOf Stacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOf Stacks. push() and SetOf Stacks. pop() should behave identically to a single stack (that is, popO should return the same values as it would if there were just a single stack).
     Implement a function popAt(int index) which performs a pop operation on a specific sub-stack. 
     3.4 In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
     (1) Only one disk can be moved at a time.
     (2) A disk is slid off the top of one tower onto the next tower.
     (3) A disk can only be placed on top of a larger disk.
     Write a program to move the disks from the first tower to the last using stacks. 
     3.5 Implement a MyQueue class which implements a queue using two stacks.
       3.6 Write a program to sort a stack in ascending order (with biggest items on top). You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. 
     3.7 An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specificanimal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.You may use the built-in LinkedList data structure.


Trees and Gaphs

1.	Implement a BST with insert and delete functions
2.	Print a tree using BFS and DFS
3.	Write a function that determines if a tree is a BST
4.	Find the smallest element in a BST
5.	Find the 2nd largest number in a BST
6.	Given a binary tree which is a sum tree (child nodes add to parent), write an algorithm to determine whether the tree is a valid sum tree
7.	Find the distance between 2 nodes in a BST and a normal binary tree
8.	Print the coordinates of every node in a binary tree, where root is 0,0
9.	Print a tree by levels
10.	Given a binary tree which is a sum tree, write an algorithm to determine whether the tree is a valid sum tree
11.	Given a tree, verify that it contains a subtree.
12.	HARD: Find the max distance between 2 nodes in a BST.
13.	HARD: Construct a BST given the pre-order and in-order traversal Strings


   4.1 Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one. 
     4.2 Given a directed graph, design an algorithm to find out whether there is a route between two nodes. 
     4.3 Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
     4.4 Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
     4.5 Implement a function to check if a binary tree is a binary search tree.
     4.6 Write an algorithm to find the'next'node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent. 
     4.7 Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree. 
     4.8 You have two very large binary trees: Tl, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide ifT2 is a subtree of Tl.
     A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.
     : :
     4.9 You are given a binary tree in which each node contains a value. Design an algo- rithm to print all paths which sum to a given value. The path does not need to start or end at the root or a leaf.
Recursion and Dynamic Programming 
      9.1 A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. 
     9.2 Imagine a robot sitting on the upper left corner of an X by Y grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot to go from (0,0) to (X,Y)?
     FOLLOW UP
     Imagine certain spots are "off limits," such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
     9.3 A magic index in an array A[0.. .n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
     
     What if the values are not distinct?
    9.4 Write a method to return all subsets of a set.
     9.5 Write a method to compute all permutations of a string.
     9.6 Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n-pairs of parentheses.
     	EXAMPLE
    	 Input: 3
    	 Output: ((())), (()()), (())(), ()(()), ()()()
     9.7 Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color. P
     9.8 Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of repre- senting n cents. 
     9.9 Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board. P
     9.10 You have a stack of n boxes, with widths w., heights hir and depths drThe boxes cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly larger than the box above it in width, height, and depth. Implement a method to build the tallest stack possible, where the height of a stack is the sum of the heights of each box. 
     9.11 Given a boolean expression consisting of the symbols 0,1, &, |, and A, and a desired boolean result value result, implement a function to count the number of ways of parenthesizing the expression such that it evaluates to result.
     EXAMPLE
     Expression: 1A01011
     Desired result: false (0)
     Output: 2 ways. 1A( (010) 11) and 1A(91 (011)).

Sorting and Searching

1.	Implement bubble sort
2.	Implement selection sort
3.	Implement insertion sort
4.	Implement merge sort
5.	Implement quick sort



 11.1 You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order. 
 11.2 Write a method to sort an array of strings so that all the anagrams are next to each other. _._ 
 11.3 Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.
 	EXAMPLE
 Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
 Output: 8 (the index of 5 in the array)
 11.4 Imagine you have a 20 GB file with one string per line. Explain how you would sort the file. 
 11.5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
 EXAMPLE
 Input: find "ball" in {"at", "", "", "", "ball", "", "", "car", tti) Output: 4
11.6 Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element. 
 11.7 A circus is designing a tower routine consisting of people standing atop one another's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.
 	EXAMPLE:
 	Input (ht,wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
 Output:The longest tower is length 6 and includes from top to bottom:
 	(56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
11.8 Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal tox). Implement the data structures and algorithms to support these operations.That is, implement the method track(int x), which is called when each number is generated, and the method getRankOfNumber(int x), which returns the number of values less than or equal to x (not including x itself).
 EXAMPLE
 Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3 getRankOfNumber(l) = 0 getRankOfNumber(3) = 1 getRankOfNumber(4) = 3
OOP
 8.1 Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.
8.2 Imagine you have a call center with three levels of employees: respondent, manager, and director. An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not free or not able to handle it, then the call should be escalated to a director. Design the classes and data struc- tures for this problem. Implement a method dispatchCall() which assigns a call to the first available employee. |
 8.3 Design a musical jukebox using object-oriented principles.
8.4 Design a parking lot using object-oriented principles.
 8.5 Design the data structures for an online book reader system. 
 8.6 Implement a jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle. You can assume that you have a fitsWith method which, when passed two puzzle pieces, returns true if the two pieces belong together. 
 8.7 Explain how you would design a chat server. In particular, provide details about the various backend components, classes, and methods. What would be the hardest problems to solve? 
 8.8 Othello is played as follows: Each Othello piece is white on one side and black on the other. When a piece is surrounded by its opponents on both the left and right sides, or both the top and bottom, it is said to be captured and its color is flipped. On your turn, you must capture at least one of your opponent's pieces. The game ends when either user has no more valid moves. The win is assigned to the person with the most pieces. Implement the object-oriented design for Othello. 
 8.9 Explain the data structures and algorithms that you would use to design an in-memory file system. Illustrate with an example in code where possible. 
 8.10 Design and implement a hash table which uses chaining (linked lists) to handle collisions
Random
 17.1 Write a function to swap a number in place (that is, without temporary vari- ables). 
 17.2 Design an algorithm to figure out if someone has won a game of tic-tac-toe. 
 17.3 Write an algorithm which computes the number of trailing zeros in n factorial. 
 17.4 Write a method which finds the maximum of two numbers. You should not use if-else or any other comparison operator.
18.1 write a function that adds two numbers. You should not use + or any arithmetic operators. 
   18.2 Write a method to shuffle a deck of cards. It must be a perfect shuffle—in other words, each of the 52! Permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.
   18.3 Write a method to randomly generates set of m integers from an array of size n. Each element must have equal probability of being chosen.
   18.4 Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive).
   EXAMPLE
   Input: 25
   Output: 9 (2,12,20,21,22,23, 24 and 25. Note that 22 counts for two 2s.) 
   18.5 You have a large text file containing words. Given any two words, find the shortest distance (in terms of number of words) between them in the file. If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution? 
   18.6 Describe an algorithm to find the smallest one million numbers in one billion numbers. Assume that the computer memory can hold all one billion numbers

