"""
Given an array of integers and a value, 
determine if there are any three integers in the array whose sum equals the given value.

arr = [3,7, 1, 2, 8, 4, 5]

target_sum = 20

Time complexity: O(N^2).

Sort the given array.
Loop over the array and fix the first element of the possible triplet, arr[i].
Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum, 
If the sum is smaller than the required sum, increment the first pointer.
Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.
"""

arr = [1, 4, 45, 6, 10, 8]
sum = 22

def sum_three_int(arr, sum):

    asize = len(arr)
    arr.sort()

    for i in range(0, asize-2):
        a = i + 1
        b = asize - 1
        print('a', a)
        print('b', b)
        while a < b:
            if arr[i]+arr[a]+arr[b] == sum:
                print("Triplet is", arr[i],
                     ', ', arr[a], ', ', arr[b]);
                return True
            elif (arr[i]+arr[a]+arr[b] < sum):
                a += 1
            else: 
                b -= 1
    return False

print(sum_three_int(arr, sum))