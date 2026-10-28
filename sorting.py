'''
---Types of sorting Algorithms---
1.Bubble sort:
2.Selection sort:
3.Insertion sort:
4.Merge sort:
5.Quick sort:
'''

# Bubble sort
'''
1.Bubble sort:-
-->It is a simple sorting algorithm that repeatedly compares neighboring elements and swaps them if they are in the wrong order.
Repeats until the list is sorted.'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j +1]:
                arr[j],arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [6, 4, 3, 1, 2, 5]
print("Bubble_sort:",bubble_sort(arr))

# 2.Selection sort
'''
2.Selection sort:
-->Find the smallest element in unsorted portion and swap it with the first unsorted element.'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  #update index values
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr= [4, 2, 5, 3, 1]
print("Selection_sort:",selection_sort(arr))

# 2.Insertion sort
'''
3.Insertion sort:
-->Take one element at a time and insert it into its correct position in the already sorted portion of array.'''
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [5, 2, 4, 1]
print("Insertion_sort:",insertion_sort(arr))

# 4.Merge sort
'''
4.Merge sort:
-->It is a sorting algorithm that repeatedly splits a list into smaller halves, sorts each half, 
and then merges the sorted halves back together. It runs in O(n log n) time.'''

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    # divide array into 2 parts
    mid = len(arr)//2
    left = arr[:mid]      # 0 to mid - 1
    right=arr[mid:] #mid + 1 to (n-1)
    # Recursively sort arrays
    left = merge_sort(left)
    right = merge_sort(right)
    # Merging two halves
    return merge(left, right)
# This method is mainly for comparsion of values
def merge(left, right):
    result = []
    i = 0
    j = 0
    # compare elements from both arrays
    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # Adding remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [15,11,17,24,32]
print("merge_sort:",merge_sort(arr))

# Quick sort:-
'''
4.Quick sort
-->It is a sorting algorithm that chooses a value called a pivot, partitions the other values into those smaller and larger than the pivot,
then recursively sorts each smaller and larger elements. '''

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    n=len(arr)
    index = n//2
    pivot = arr[index]
    left = [ x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = [10 ,7 ,1, 5]
print("Quick_sort:",quick_sort(arr))
