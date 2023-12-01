"""
    Reverse String
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

"""

def reverseString(s):
    return s[::-1]

def reverseString2(s):
    right = 0
    left = len(s) - 1 

    while right < left:
        s[right], s[left] = s[left], s[right]
        right += 1
        left -= 1
    return s

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    print(reverseString2(s))