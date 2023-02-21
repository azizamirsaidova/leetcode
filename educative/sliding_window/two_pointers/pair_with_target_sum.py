
"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Since the given array is sorted, a brute-force solution could be to iterate through the array, taking one number at a time and searching for the second number through Binary Search. The time complexity of this algorithm will be 
O(N∗logN)

We can follow the Two Pointers approach. 
We will start with one pointer pointing to the beginning of the array and another pointing at the end. 
At every step, we will see if the numbers pointed by the two pointers add up to the target sum. 
If they do, we have found our pair; otherwise, we will do one of two things:

1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.
2. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.

Time Complexity: O(N), where ‘N’ is the total number of elements in the given array.
Space Complexity: O(1)

"""

def pair_with_targetsum(arr, target_sum):


  # TODO: Write your code here

    indexes = []
    left = 0 
    right = len(arr)-1

    while left < right:
        total_sum = arr[left] + arr[right]

        if total_sum == target_sum:
            return [left, right]
        if total_sum < target_sum:
            left += 1 # we need a pair with a bigger sum
        else:
            right -= 1 # we need a pair with a summer sum 
    return [-1, -1]

def pair_with_targetsum_hashmap(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            increment = [nums[target_sum - num], i]
            return increment
        else:
            nums[arr[i]] = i
    print(nums)
    return -1, -1

def main():
    #print("Target sum is: ", pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print("Target sum is: ", pair_with_targetsum_hashmap([1, 2, 3, 4, 6], 6))

main()