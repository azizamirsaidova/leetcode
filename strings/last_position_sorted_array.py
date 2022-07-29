"""
#34 Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10] target = 8
Output: [3,4]

Plan:
1. Sort the arry 
2. Create for loop 
3. if val is target:
check before and after, 
and return to start and ending position

Example: https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

"""

num =  [ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
target = 6

def lastPosition(num, target):
    nums = sorted(num)
    last_po = []
    first = -1
    last = -1
    for i in range(0,len(nums)):
        if nums[i] == target:
            last_po.append(i)
        
        if nums[i] != target:
            return first, last
    return last_po
#print(lastPosition(num, target))

def firstPositionBinarySearchIterative(num, target):

    low = 0
    high = len(num) - 1
    result = -1

    while low <= high:
        mid = (low+high) // 2

        #iterate low and high
        # print("low",low)
        # print("mid",mid)
        # print("high",high) 
        
        if num[mid] < target:
            high = mid - 1
        elif num[mid] > target:
            low = mid + 1
        else:
            result = mid
            high = mid - 1
    
    return result 

def lastPositionBinarySearchIterative(num, target):

    low = 0
    high = len(num) - 1
    result = -1

    while low <= high:
        mid = (low+high) // 2
        
        if num[mid] < target:
            high = mid - 1
        elif num[mid] > target:
            low = mid + 1
        else:
            result = mid 
            low = mid + 1
    
    return result 

# print("First occurence", firstPositionBinarySearchIterative(num, target))
# print("Last occurence", lastPositionBinarySearchIterative(num, target))

def lastPostionWithIndex(num, target):
    first = num.index(target)
    last = num[::].index(target)+1
    
    if target not in num:
        return -1, -1
    # else:
    #     return first, last
print(lastPostionWithIndex(num, target))