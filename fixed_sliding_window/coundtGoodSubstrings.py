"""

    Substrings of Size Three with Distinct Characters
    A string is good if there are no repeated characters.

    Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

    Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

    A substring is a contiguous sequence of characters in a string.

    Input: s = "xyzzaz"
    Output: 1
    Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
    The only good substring of length 3 is "xyz".

"""

def countGoodSubstrings(s):
    n = len(s)
    k = 3
    subString = s[:k]
    count = 0
    freq = {}

    if n < k:
        return 0

    for i in range(k):
        if s[i] not in freq:
            freq[s[i]] = 0
        freq[s[i]] += 1
    
    if len(freq) == k:
        count += 1
    
    for i in range(n-k):
        if freq[s[i]] == 1:
            del freq[s[i]]
        else:
            freq[s[i]] -= 1
        
        if s[i+k] not in freq:
            freq[s[i+k]] = 0
        freq[s[i+k]] += 1

        if len(freq) == k:
            count += 1
    return count
    
def main():

    s = "aababcabc"
    print(countGoodSubstrings(s))

if __name__ == "__main__":
    main()
