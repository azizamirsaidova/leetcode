"""

1) Create an arrray
2) Set a negative flag if input value is negative
3) Iterate through the integer backwards through divide by 10 and modulus method
    a) Append element to array
4) Reverse the array and join the elements into a string
5) Return newly created string


Time Complexity: O(N) [Single-pass iteration and single string build]
Space Complexity: O(N) [Separate array of size N and return string of size N]

"""

def int_to_string(num: int) -> str:
    if num == 0:
        return "0"
    negative_flag = num < 0
    num = abs(num)
    arr = []
    while num != 0:
        arr.append(chr(num % 10 + ord('0')))
        num = num // 10
    arr.reverse()
    return "-" + "".join(arr) if negative_flag else "".join(arr) 

