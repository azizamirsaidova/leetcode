"""
    Valid Palindrome
    
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

"""


def isPalindrome(s):
    left = 0
    right = len(s) - 1 
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1 
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def isPalindrome2(s):
    left = 0
    right = len(s) - 1 
    
    while left < right:
        # skip the non alphanumerical characters both left and right side
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -=1 
        # if string on the left matches with right continue the search, unless return False
        elif s[left].lower() == s[right].lower():
            left += 1
            right -=1 
        else:
            return False
    
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome2(s))
