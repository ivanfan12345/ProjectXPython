__author__ = 'IFAN'


def determine_if_string_has_unique_chars(str):
    dictionary = {}
    for char in str:
        if (char in dictionary):
            return False
        else:
            dictionary[char] = 1
    return True


def reverse_string(str):
    reversed_str = ''
    for i in range(len(str) - 1, -1, -1):
        reversed_str += str[i]
    print str
    print reversed_str
    return reversed_str


def determine_if_anagram(str1, str2):
    if (len(str1) != len(str2)):
        return False
    print str1
    print str2
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, len(str1), 1):
        if (str1[i] != str2[i]):
            return False
    return True


def find_first_non_repeated_char(str):
    dictionary = {}
    for char in str:
        if char in dictionary:
            return char
        else:
            dictionary[char] = 1
    print dictionary


def is_palindrome(string):
    r_str = reverse_string(string)
    print r_str
    print string
    if r_str == string:
        return True
    else:
        return False


def replace_spaces(string):
    new_string = ''
    for char in string:
        if (char == ' '):
            new_string += str('%20')
        else:
            new_string += str(char)
    print string
    print new_string
    return new_string


'''
 1.5 Implement a method to perform basic string compression using the counts of repeated characters. For example,
 the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the orig- inal string,
  your method should return the original string. pg176
'''


def string_compression(string):
    counter = 1
    char_curr = ''
    output = ""
    char_prev = string[0]
    for i in range(1, len(string) - 1, 1):
        char_curr = string[i]
        if (char_curr == char_prev):
            char_curr = string[i + 1]
            counter += 1
        else:
            output += str(char_prev)
            output += str(counter)
            char_prev = char_curr
            char_curr = string[i + 1]
            counter = 1
    output += str(char_prev)
    output += str(counter)

    print output


def rotate_array():
    lists = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    for list in lists:
        print list


# Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
def generate_square_matrix_in_spiral_order(n):
    #matrix = []
    matrix = [[0] * n for i in range(n)]
    print_matrix(matrix)


    if (n == 0):
        return matrix

    #Indexes
    begin_x = 0
    begin_y = 0
    end_x = (n-1)
    end_y = (n-1)
    current = 1

    while (current <= n * n):
        print 'current'
        #top left -> top right
        for col in range(begin_x, end_x+1, 1):
            matrix[begin_y][col] = current
            current += 1
        begin_y += 1
        print_matrix(matrix)

        #top right -> bottom right
        for row in range(begin_y, (end_y+1), 1):
            matrix[row][end_x] = current
            current += 1
        end_x -= 1
        print_matrix(matrix)

        #bottom right -> bottom left
        for col in range(end_x, begin_x-1 , -1):
            matrix[end_y][col] = current
            current+=1
        end_y -= 1
        print_matrix(matrix)

        #bottom left -> top left
        for row in range(end_y, begin_y-1, -1):
            matrix[row][begin_x] = current
            current +=1
        begin_x += 1
        print_matrix(matrix)

    print 'hello'
    for row in matrix:
        print row

def print_matrix(matrix):
    print '======================'
    for row in matrix:
        print row

'''
Arrays and Strings
Check if String is a palindrome
Check if a String is composed of all unique characters
Determine if a String is an int or a double
HARD: Find the shortest palindrome in a String
HARD: Print all permutations of a String
HARD: Given a single-line text String and a maximum width value, write the function 'String justify(String text, int maxWidth)'
that formats the input text using full-justification, i.e., extra spaces on each line are equally distributed between the words;
the first word on each line is flushed left and the last word on each line is flushed right


 1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? p
 1.2 Implement a function void reverse(char* str) in C or C++ which reverses a null- terminated string. pg 17 3
 1.3 Given two strings, write a method to decide if one is a permutation of the other. pg 174
 1.4 Write a method to replace all spaces in a string with'%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. (Note: if imple- menting in Java, please use a character array so that you can perform this opera- tion in place.)
 EXAMPLE
 Input: "Mr John Smith
 Output: "Mr%20Dohn%20Smith"
 ^ __ pg 1?5
 1.5 Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the orig- inal string, your method should return the original string. pg176
 1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
 the image by 90 degrees. Can you do this in place? pg 179
 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
 1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings,
 si and s2, write code to check if s2 is a rotation of si using only one call to isSubstring (e.g.,"waterbottle"is a rota- tion of "erbottlewat"


'''



