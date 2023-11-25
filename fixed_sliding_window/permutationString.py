"""
    Permutation in String
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

"""

def permutationString1(s1, s2):
    s1Size = len(s1)
    s2Size = len(s2)
    
    for i in range(s2Size - s1Size+1):
        if sorted(s2[i:s1Size+i]) == sorted(s1):
            return True
    return False

def permutationString2(s1, s2):
    s1Size = len(s1)
    s2Size = len(s2)

    s1Map = {}
    s2Map = {}

    for i in range(s1Size):
        s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
        s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)
    
    if s1Map == s2Map:
        return True
    
    for i in range(s2Size - s1Size):
        if s2Map[s2[i]] == 1:
            del s2Map[s2[i]]
        else:
            s2Map[s2[i]] -= 1
        if s2[i+s1Size] not in s2Map:
            s2Map[s2[i+s1Size]] = 0
        s2Map[s2[i+s1Size]] += 1

        if s2Map == s1Map:
            return True
    return False

def main():
    s1 = "ab"
    s2 = "eidbaooo"
    print(permutationString1(s1, s2))
    print(permutationString2(s1, s2))

if __name__ == "__main__":
    main()
