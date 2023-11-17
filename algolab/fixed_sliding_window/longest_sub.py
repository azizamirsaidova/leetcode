"""
Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest 

substring that contains at most two distinct characters. 

s = "eceba"
answer 3, "ece"

s = "ccaabbb"
answer 5, "aabbb"

# the longest
# two distinct chars


"""
s = "aa"
k = 1
def longest_subsequence(s, k):
    smap = {}
    max_vals = 0 
    l, r = 0, 0
    # for r in range(len(s)):
    while r < len(s):
        smap[s[r]] = smap.get(s[r], 0)+1

        while len(smap) > k:
            smap[s[l]] = smap.get(s[l], 0)-1 

            if smap[s[l]] == 0:
                del smap[s[l]]
            l += 1
        max_vals = max(max_vals, r-l+1)
        r += 1
    return max_vals

print(longest_subsequence(s, k))
