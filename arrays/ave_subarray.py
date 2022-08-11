"""
Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Plan:

1. Calculate sum of every 5 elements of subarray
2. Divide the sum by 5

"""

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

def find_average_sum_of_subarray(arr, k):

    result = []
    for i in range(len(arr)-k+1):
        average_sum = 0.0
        for j in range(i, i+k):
            average_sum += arr[j]
        result.append(average_sum/k)
    return result

print(find_average_sum_of_subarray(arr, k))