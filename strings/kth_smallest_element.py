"""
Given an array and a number k 
where k is less than size of array, 
we need to find the k’th smallest element in the given array. 
It is given that all array elements are distinct.

Input: [7, 10, 4, 3, 20, 15]
k = 3
Output: 7

Input: [7, 10, 4, 3, 20, 15]
k = 4
Output: 10

1) Sort the input array
2) Select and return the element in index k - 1

"""

import heapq


a = [7, 10, 4, 3, 20, 15]
k = 3

def simple(a, k):
    sort = sorted(a)
    return sort[k-1]

def kthSmallest(a, k):
    """
    Use the first k elements of your unsorted array and build a Heap. 
    The choice of Min/Max is up to you. 
    For example, if you are looking for the 4th smallest element, your Heap size should be 4. 
    After building the initial Heap, you introduce the remaining elements to your Heap and update it.
    At the end, you will have k value in your Heap, which are the smallest/largest elements of your unsorted array.
    
    heappush:

    heappop:
    
    """

    smallest = []

    for val in a:
        print(-val)
        if (len(smallest) < k):
            heapq.heappush(smallest, -val)
        else:
            heapq.heappushpop(smallest, -val)
    if (len(smallest) < k ):
        return None
    return -smallest[0]

print(kthSmallest(a, k))
