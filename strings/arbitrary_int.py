"""
Increment an arbitrary precision integer

Implement a function to increment an arbitrary precision integer 
represented in the form of an array, where each element in the array corresponds to a digit.

Input: [1,2,3]
Output: [1,2,4]
Explanation: 123 + 1 = 124

Input: [5,8,9]
Output: [5,9,0]
Explanation: 589 + 1 = 590 

"""

num = [5,8,9]

def arb_int(num):

    s = [str(i) for i in num]
    result = int("".join(s))
    result = result + 1

    digits = [int(i) for i in str(result)]
    return digits

print(arb_int(num))
