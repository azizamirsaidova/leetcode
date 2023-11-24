"""

    Find K-Length Substrings With No Repeated Characters
    Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

    Input: s = "havefunonleetcode", k = 5
    Output: 6
    Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.




"""

def numKLenSubstrNoRepeats(s, k):
    n = len(s)
    count = 0
    freq = {}

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
    s = "havefunonleetcode"
    k = 5
    print(numKLenSubstrNoRepeats(s, k))

if __name__ == "__main__":
    main()
