"""

Given an integer x, return true if x is a palindrome, and false otherwise. 

Note: Converting the integer to a string is not recommended.

Input: x = 121
Output: true

Explanation: 121 reads as 121 from left to right and from right to left.

https://www.youtube.com/watch?v=yubRKwixN-U

"""

def palindrome_int_convert_str(n):
    x = str(x)
    if x[:] == x[::-1]:
        return True
    elif x[:] != x[::-1]:
        return False


def palindrome_int(x):

    if x < 0:
        return False
    
    div = 1
    while x >= 10 * div:
        div *= 10
    
    while x:
        right = x % 10
        left = x // div

        if left != right:
            return False
        
        # eliminate the already seen values
        x = (x % div) // 10
        div = div / 100
    return True 


def palindrome_int_2(x):
    if x < 0:
        return False
    
    reverseNumber = 0
    number = x

    while number > 0:
        reverseNumber = reverseNumber * 10 + number % 10
        print("Before:", number, reverseNumber)
        number = number // 10
        print("Before:", number, reverseNumber)

    return x == reverseNumber

n = 121
print(palindrome_int_2(n))
print(1//10)

