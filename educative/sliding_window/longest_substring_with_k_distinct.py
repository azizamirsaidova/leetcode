"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Plan:
1. Get the count of the characters
2. Get the k count of characters
3. Compare the size, and choose the max of them

"""

stri ="araaci"
k = 2

def longest_substring_with_k_distinct(stri, k):
  freq = {}
  max_length = 0
  #1. First, we will insert characters from the beginning of the string until we have K distinct characters in the HashMap.
  for end in range(len(stri)):
    right_char = stri[end]
    if right_char not in freq:
      freq[right_char] = 0
    freq[right_char] = 1

    #2. These characters will constitute our sliding window. We are asked to find the longest such window having no more than K distinct characters. 
    #We will remember the length of this window as the longest window so far.
    while len(freq)>k:
      left_char = stri[start]
      
      #3. In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than K. 
      #We will shrink the window until we have no more than K distinct characters in the HashMap. This is needed as we intend to find the longest window.
      
      freq[left_char] -= 1

      #4. While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
      if freq[left_char] == 0:
        del freq[left_char]
      start += 1
    #5. At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.
    max_length = max(max_length, end-start+1)
  return max_length

def longest_substring_with_k_distinct_2(str1, k):
# TODO: Write your code here

  start = 0
  max_length = 0
  freq = {}

  for end in range(len(str1)):
    right_char = str1[end]

    if right_char not in freq:
      freq[right_char] = 0
    freq[right_char] = 1
    print("Right char:", right_char)
    while len(freq) > k:
        left_char = str1[start]
        freq[left_char] -= 1
        
        if freq[left_char] == 0:
          del freq[left_char]
        print("Left char:", left_char)
        start += 1
    max_length = max(max_length, end-start+1)
    
  return max_length


def main():
  #print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  #print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct_2("cbbebi", 3)))



main()