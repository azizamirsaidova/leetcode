"""
Given an array of integers arr, write a function absSort(arr), 
that sorts the array according to the absolute values of the numbers in arr. 
If two numbers have the same absolute value, sort them according to sign, 
where the negative numbers come before the positive numbers.

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]

PLAN:

1. go through the values in arr
2. create, low, and high arrays
"""
from collections import defaultdict

def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater = []
    lower = []
    for i in arr:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)

    return quick_sort(lower)+[pivot]+quick_sort(greater)

arr = [2, -7, -2, -2, 0]
size = len(arr)

absSorted = [abs(i) for i in arr]
absSorted = quick_sort(absSorted)

negatives = defaultdict(int)
for i in arr:
    if i < 0:
        negatives[abs(i)]+=1

result = []
for i in absSorted:
    if negatives[i]>0:
        result.append(-i)
        negatives[i]-=1
    else:
        result.append(i)
print(result)


