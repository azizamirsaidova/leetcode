"""
1) Create an integer variable and a boolean variable for negatives
2) Iterate the input string from left to right
    a) If the character is "-", set the negative boolean variable to True
    a) Multiply the integer variable by 10 and add the current indexed integer in the string
3) If the negative boolean variable is True, multiply by -1 and return the integer variable.

Time Complexity: O(N)
Space Complexity: O(1) [Only 2 variables made, no string concatenation]

"""

def myAtoi(self, input: str) -> int:
    output = 0
    sign = 1
    for i in range(len(input)):
        if input[i] == "-":
            sign = -1
        elif '0' <= input[i] and input[i] <= '9':
            output = (output * 10) + ord(input[i]) - ord('0')
    return output * sign