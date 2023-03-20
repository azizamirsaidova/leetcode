"""
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

s = ["h","e","l","l","o"]

def reverseString(s):

    left = 0 
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1
    return s 

print(reverseString(s))