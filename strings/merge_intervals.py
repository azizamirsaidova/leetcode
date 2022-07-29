"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5]

 A simple approach is to start from the first interval 
 and compare it with all other intervals for overlapping, 
 if it overlaps with any other interval, 
 then remove the other interval from the list 
 and merge the other into the first interval. 
 Repeat the same steps for the remaining intervals after the first. 
 This approach cannot be implemented in better than O(n^2) time.


1. Sort the intervals based on the increasing order of starting time.
2. Push the first interval into a stack.
3. For each interval do the following:
4. If the current interval does not overlap with the top of the stack then, push the current interval into the stack.
5. If the current interval overlap with the top of the stack then, update the stack top with the ending time of the current interval.
6. The end stack contains the merged intervals. 


"""

def mergeIntervals(intervals):

     # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    print(intervals.sort())
    # insert first interval into stack
    stack.append(intervals[0])

    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    print("The Merged Intervals are :", end=" ")
    for i in range(len(stack)):
        print(stack[i], end=" ")
  
  
arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
mergeIntervals(arr)

