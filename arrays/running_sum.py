def runningSum(nums):
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(result[i-1]+nums[i])
    return result
        

def runningSum2(nums):
    l=[nums[0]]
    for i in range(1,len(nums)):
        l.append(l[i-1]+nums[i])
    return l


print(runningSum([1,2,3,4]))