__author__ = 'Ivan'
#Find the most frequent element in the list
def find_most_frequent_int(array):
    for i in array:
        dictionary = {}
        for i in array:
            if not i in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1

    value_max = -1
    key_max = -1
    for x in dictionary:
        print x , 'corredponds to ' , dictionary[x]
        if(value_max < dictionary[x]):
            value_max = dictionary[x]
            key_max = x

    print 'Most common integer is: ' , key_max , ' with ' , value_max , ' appearances'

#Find pairs in an integer array whose sum is equal to a given target value
def find_pair_sum_to_target(array, target):
    dictionary = {}
    output = []
    for int in array:
        if not int in dictionary:
            dictionary[target - int] = int

        else:
            output.append(int)
            output.append(dictionary[int])
            print int , ' + ' , dictionary[int] , ' = ' , target
            return output

    print 'Found Nothing'
    return output

#Find the only element in an array that only occurs once.
def find_elements_that_occur_once(array):
    dictionary = {}
    for i in array:
        if not i in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] +=1


    for i in dictionary:
        if(dictionary[i] == 1):
            print 'Element ' , i , ' ocurrs only once!'
            return i

    print 'Found Nothing'
    return 0

#Find the common elements of 2 int arrays
def find_common_elements(array1,array2):
    result = []
    for i in array1:
        if i in array2 and i not in result :
            result.append(i)

    print result
    return result

#Fibonacci iteratively
def fibonacci_iteratively(nth):
    prevPrev = 0
    prev = 1
    result = 0


    if nth == 0:
        return 0
        print '%d' %(prevPrev)
    if nth == 1:
        return 1
        print '%d' %(prev)
    else:
        for i in range(nth):
            #print 'i = %s' %(i)
            result = prev + prevPrev
            prevPrev = prev
            prev = result
            print '%d' %(result)

#Fibonacci Recursive
def fibonacci_recurrsive(nth):
    if nth == 0:
        return 0
    if nth == 1:
        return 1
    else:
        return (fibonacci_recurrsive(nth - 1) + fibonacci_recurrsive(nth - 2))

    #Given 2 integer arrays, determine if the 2nd array is a rotated version of the 1st array.
    # Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
def determineIfRotatedArray(array1 , array2):
    if(len(array1) != len(array2)):
        return False
    length = len(array1)
    index1 = 0
    index2 = 0
    offset = 0
    while(index2 < length):
        if(array2[index2] != array1[index1]):
            index2 +=1
            offset +=1
        else:
            break

    print 'Element1: ', array1[index1] ,' Index1: ' , index1, ' and ' ,'Element2:', array2[index2] ,'Index1:', index2
        #index1+=1
    print 'Offset: ' , offset

    while(index2 < length):
        if(array1[index1] != array2[index2]):
            return False
        else:
            print'array1[index1]:', array1[index1] , ' array2[index2]:', array2[index2]
            index1 += 1
            index2 += 1
    index1 = 0
    index2 = offset

    while(index1 < offset-1):
        if(array1[index1] != array2[index2]):
            return False
        else:
            print'array1[index1]:', array1[index1] , ' array2[index2]:', array2[index2]
            index1 += 1
            index2 += 1


#Implement binary search of a sorted array of integers
def binarySearch(array ,target , low ,high):
    if(high < low): return False
    mid = (low + high)/2
    if(array[mid] == target):
        return True
    if array[mid] > target:
        return binarySearch(array, target, low, mid-1)
    elif array[mid] < target:
        return binarySearch(array, target, mid+1, high)
    else:
        return True

def ivan_isPrime_(number):
    if(number < 0):
        return False

    for x in range(2,number):
        if((number % x) == 0):
            return False
    return True

'''
     * The FizzBuzz Challenge: Display numbers from 1 to x, replacing the word 'fizz' for multiples of 3, 'buzz'
     * for multiples of 5 and 'fizzbuzz' for multiples of both 3 and 5. Th result must be:1 2 fizz 4 buzz fizz
     * 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16
     */
'''

def fizz_buzz(x):
    for i in range(1 , x , 1):
        if((i % 3 == 0) and (i%5 != 0)):
            print('fizz')
        elif((i%5 == 0) and (i%3 != 0)):
            print('buzz')
        elif((i%5 == 0) and (i%3 == 0 )):
            print('fizzbuzz')
        else:
            print(i)


    '''
       Write fibonacci iteratively and recursively (bonus: use dynamic programming)
    Implement binary search of a sorted array of integers
    Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
    Use dynamic programming to find the first X prime numbers
    Write a function that prints out the binary form of an int
    Implement parseInt
    Implement squareroot function
    Implement an exponent function (bonus: now try in log(n) time)
    Write a multiply function that multiples 2 integers without using *
    HARD: Given a function rand5() that returns a random int between 0 and 5, implement rand7()
    HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)

'''