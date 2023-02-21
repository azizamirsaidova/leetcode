"""

Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[]. 
The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 
and 2 is 1.
Explanation: 1 is at index 0 and 2 is at 
index 1, so the distance is 1

"""

def find_min_distance(arr, x, y):
    min_distance = 0
    for xi in range(x):
        for yi in range(y):
            min_distance = yi - xi
            #print(min_distance)
    return min_distance

def find_min_distance_unsorted(arr, x, y):
    min_distance = float('inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if ((x == arr[i] and y == arr[j]) or (y == arr[i] and x == arr[j])) and min_distance > abs(i-j):
                min_distance = abs(i-j)
        return min_distance

def main():
    arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    x = 3
    y = 6
    # print("Min distnace, ", find_min_distance(arr, x, y))
    print("Min distnace, ", find_min_distance_unsorted(arr, x, y))

main()