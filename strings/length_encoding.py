"""
Given an input string, write a function that returns the run-length encoded string for the input string.

Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"

1) Pick the first character from the source string. 
2) Append the picked character to the destination string. 
3) Count the number of subsequent occurrences of the picked character and append the count to the destination string. 
4) Pick the next character and repeat steps b) c) and d) if the end of the string is NOT reached.

"""

string = "wwwwaaadexxxxxx"

def encode_string(string):
    i = 0 
    
    while i < len(string) - 1:
        count = 1
        while i < len(string) - 1 and string[i] == string[i+1]:
            count += 1
            i+=1
        i+=1
        print(string[i-1]+str(count), end = "")
        

print(encode_string(string))
