
"""
Given a string s, find the length of the longest substring t that contains at most 2 distinct characters.

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""
arr = "ccaabbb"
t = 2

def lswith_k(arr, t):
    start = 0
    freq = {}
    max_length = 0

    for end in range(len(arr)):
        right_char = arr[end]
        
        if right_char not in freq:
            freq[right_char] = 0
        freq[right_char] = 1 

        while len(freq) >= 2:
            left_char = arr[start]
            freq[left_char] -= 1
            
            if freq[left_char] == 0:
                del freq[left_char]
        
            start -= 1
        max_length = max(max_length, end-start+1)
    return max_length

def main():
    print(lswith_k(arr, t))

main()