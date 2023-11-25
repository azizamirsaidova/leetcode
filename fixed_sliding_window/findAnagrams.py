"""

    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

    -> create a hashmap of s, p
    -> go through s with a length of p
    -> check whether all letters of s in p, 
        if so, add its start index to new array
    return to new array
"""
import itertools

def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    sMap = {}
    pMap = {}
    anagram = []
    
    for i in p:
        pMap[i] = pMap.get(i, 0) + 1

    for i in range(0, len(s)-len(p)+1):
        if i == 0:
            for j in range(0, i+len(p)):
                sMap[s[j]] += 1
        else:
            sMap[s[j+len(p)]] += 1

        if sMap == pMap:
            anagram.append(i)
        
        sMap[s[i]] -= 1
    return anagram

            

def main():
    s = "cbaebabacd"
    p = "abc"
    findAnagrams(s, p)

if __name__ == "__main__":
    main()