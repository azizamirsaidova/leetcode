"""
    Find K-Length Substrings With No Repeated Characters
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

"""

s = "havefunonleetcode"
k = 5

n = len(s)
smap = {}
for i in s:
    smap[i] = smap.get(i, 0)+1

print(smap)



