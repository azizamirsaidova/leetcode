import random 
import heapq
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt

def q1(x, y):
    """
        Q1: Given two arrays, write a python function to return the intersection of the two? 
        For example, X = [1,5,9,0] and Y = [3,0,2,9] it should return [9,0]

    """
    x = [1,5,9,0]
    y = [3,0,2,9]
    res = []
    
    for i in y:
        if i in x:
            res.append(i)
    return res

def q2(arr):
    """
        Q2: Given an array, find all the duplicates in this array? For example: input: [1,2,3,1,3,6,5] output: [1,3]
    """
    arr = [1,2,3,1,3,6,5]
    duplicate = {}
    for i in arr:
        duplicate[i] = duplicate.get(i, 0)+1

    res = []
    for key, value in duplicate.items():
        if value == 2:
            res.append(key)
    return res

def q3(arr):
    """
        Q3: Given an integer array, return the maximum product of any three numbers in the array?
    
    """

    arr = [1,2,3,1,3,6,5]
    a = heapq.nlargest(3, arr) # largerst 3 numbers for postive case
    b = heapq.nsmallest(2, arr) # for negative case
    return max(a[2]*a[1]*a[0], b[1]*b[0]*a[0])

def q4(arr):
    """
        Q4: Given an integer array, find the sum of the largest contiguous subarray within the array. For example, given the array A = [0,-1,-5,-2,3,14] it should return 17 because of [3,14]. 
        Note that if all the elements are negative it should return zero.
    """

    n = len(arr)
    k = 2
    windowSum = sum(arr[:k])
    maxSum = windowSum

    for i in range(n-k):
        windowSum = windowSum - arr[i] + arr[i+k]
        maxSum = max(maxSum, windowSum)
    return maxSum

def q6(a, b):
    """
        Compute the Euclidean Distance Between Two Series?
    """
    a = np.array((9,6,15))
    b = np.array((1,4,9))

    sum_sq = np.sum(np.sqrt(a-b))
    return np.sqrt(sum_sq)

def q7_approach1(n,k):
    """
        Q7: Given an integer n and an integer K, output a list of all of the combination of k numbers chosen from 1 to n. 
        For example, if n=3 and k=2, return [1,2],[1,3],[2,3]
    """
    comb = combinations([i for i in range(1, n+1)], k)
    res = []
    for i in comb:
        res.append(i)
    return res

def q7_approach2(n,k):
    def dfs(i, n, k, temp, ans):
        if k == 0:
            ans.append(temp[:])

        dfs(i+1, n, k, temp, ans)
        temp.append(i)
        dfs(i+1, n, k-1, temp, ans)
        temp.pop(k)
    
    ans = []
    temp = []
    dfs(0, n, k, temp, ans)
    return ans

def q8(N):
    """ 
        Q8: Write a function to generate N samples from a normal distribution and plot them on the histogram

    """

    x = np.random.random((N,))
    plt.his(x)

def q10(input_string):
    """
        Q10: Given a string, return the first recurring character in it, or “None” if there is no recurring character. 
        Example: input = "pythoninterviewquestion" , output = "n"
    """
    input_string =  "pythoninterviewquestion"
    output = "n"

    lmap = {}

    for i in input_string:
        lmap[i] = lmap.get(i,0)+1
    
    for key, value in lmap.items():
        if value > 1:
            return key
            break

def q11(x):
    """ 
        Q11: Given a positive integer X return an integer that is a factorial of X. 
        If a negative integer is provided, return -1. Implement the solution by using a recursive function.
    
    """
    if x < 0:
        return -1
    if x == 0:
        return 1
    
    if x == 1:
        return x
    else:
        return x * q11(x - 1)

input_string =  "pythoninterviewquestion"
print(q10(input_string))