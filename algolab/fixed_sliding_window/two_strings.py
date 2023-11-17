from collections import Counter

def twoStrings(s1, s2):
    # Write your code here
    s1Map = Counter(s1)
    s2Map = Counter(s2)
    
    for char in s1Map:
        if char in s2Map:
            return "YES"
        else:
            return "NO"

s1 = ['aardvark']
s2 = ['apple']
print(twoStrings(s1, s2))
