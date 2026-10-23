'''
searching Algorithms
1. Linear Search
2. Binary Search

Linear search :-
--> It search elements one by one(sequential search)
--> It works on sorted and unsorted array.
--> Time complexity - Best- O(1) - Average - O(n) - Worst - O(n)
'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None
arr = [10,20,50,30,40]
target = 20
result = linear_search(arr,target)
if result != -1:
    print("Elements found at index :",result)
else:
    print("Elements not found")


'''
Binary Search
--> Divide and conquer
'''
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr= [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
print("Index of target:",result)