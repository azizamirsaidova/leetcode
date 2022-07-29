"""

1) Create a separate array
2) Tokenize the input string using langauge methods
3) Filter through empty tokens within the array, transfer to new array
4) Reverse the array
5) Return a joined string version of the reversed array

Time Complexity: O(N) [Single-pass iteration and single string concatenation]
Space Complexity: O(N)


"""

def reverseWords(self, s: str) -> str:
    arr = [token for token in s.split() if token != ""]
    return " ".join(reversed(arr))