"""
Shortest Unsorted Subarray

Given an integer array nums, you need to find one continuous subarray that 
if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

1. Initialize LeftPtr at the start index and RightPtr at the last index
2. Iterate LeftPtr from left -> right as long as it points to elements in the increasing order. 
Break when arr[LeftPtr] < arr[index] (that's when you've spotted the first element that is out of order from left)

3. Iterate RightPtr from right -> left as long as it points to elements in the decreasing order. 
Break when arr[RightPtr] > arr[index] (that's when you've spotted the first element from right, that is out of order)

4. We now have found a candidate sub-array. Find the local min and local max in this sub array
5. Extend the sub-array from LeftPtr to the beginning of the array to include elements greater than the local min. This is to make sure that all the remaining elements to the left are indeed less than all elements in the subarray
6. Extend the sub-array from RightPtr to the end of the array to include elements smaller than the local max. This is to make sure that all the remaining elements to the right are indeed greater than all elements in the subarray

"""

import enum


arr = [1, 2, 5, 3, 7, 10, 9, 12]
def sortIndex(arr):
    #1. Initialize LeftPtr at the start index and RightPtr at the last index
    low = 0
    high = len(arr)-1

    #2. Iterate LeftPtr from left -> right as long as it points to elements in the increasing order.
    while low < len(arr)-1 and arr[low] <= arr[low+1]:
        low+=1
    
    if low == len(arr)-1:
        return 0 

    while high > 0 and arr[high] > arr[high-1]:
        high -=1

    
    for k in range(low, high):
        max_ = max(max_, arr[k])
        min_ = min(min_,arr[k])


    # extend the subarray to include any number which is bigger than the minimum of the subarray 
    while low > 0 and arr[low - 1] > min_:
      low -= 1
    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while high < len(arr) - 1 and arr[high + 1] < min_:
      high += 1

    return high - low + 1

def sort2(arr):
    #arr = [1, 2, 5, 3, 7, 10, 9, 12]
    nums = sorted(arr)
    N = len(nums)
    l, r = N, 0
    for i,n in enumerate(nums):
        l = min(l, i)
        print('left', l)
       
        r = max(r,i)
        print('right', r)

    if l==N:
        return 0
    
    result = r-l+1
    print("result", result)
    
    return result

print(sort2(arr))
