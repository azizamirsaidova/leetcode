"""
    Given an array of integers arr and two integers k and threshold, 
    return the number of sub-arrays of size k and average greater than or equal to threshold.

    Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    Output: 3
    Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

"""

def numOfSubarrays(arr, k, threshold):
    n = len(arr)
    windowSum = sum(arr[:k])
    averageSum = windowSum/k
    count = 0
    if averageSum >= threshold:
        count += 1
    
    for i in range(n-k):
        windowSum = windowSum - arr[i] + arr[i+k]
        averageSum = windowSum/k
        if averageSum >= threshold:
            count += 1
    return count

def main():
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    numOfSubarrays(arr, k, threshold)

if __name__ == "__main__":
    main()
