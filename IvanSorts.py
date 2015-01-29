__author__ = 'IFAN'
def bubble_sorts(array):
    print '**** BUBBLE SORT ****'
    length = len(array)
    print array
    for i in range(length):
        for j in range(length -1 , i , -1):
            if(array[j] < array[j-1]):
                bubble_swap(array, j , j-1)
                print array

def bubble_swap(arr , i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertion_sort():
    print '**** INSERTION SORT ****'

def selection_sort():
    print '**** SELECTION SORT ****'

def merge_sort(array):
    print '**** MERGE SORT ****'
    if(len(array) == 1 ): return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    #print left
    #print right
    left = merge_sort(left)
    right = merge_sort(right)

    #print 'TIME TO MERGE BITCHESSSSSS'

    return merge(left , right)

def merge(first , second):
    index1 = 0
    index2 = 0
    merged = []

    while((index1 < len(first)) and (index2 < len(second))):
        if(first[index1] < second[index2]):
            merged.append(first[index1])
            index1 += 1
        elif (second[index2] < first[index1]):
            merged.append(second[index2])
            index2 += 1
        elif(first[index1] == second[index2]):
            merged.append(first[index1])
            index1 +=1
            merged.append(second[index2])
            index2 +=1

    while(index1 < len(first)):
        merged.append(first[index1])
        index1 +=1
    while(index2 < len(second)):
        merged.append(second[index2])
        index2 +=1

    #print 'MERGED FINISHED'
    #print merged
    return merged


def heap_sort():
    print '**** HEAP SORT ****'

def quick_sort():
    print '**** QUICK SORT ****'
