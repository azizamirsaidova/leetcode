"""
minutes: [221,1066,686,855]
limit: 1000

flies on day > i 
flight will take -> minutes 
cannot fly more than the limit minutes

"""
minutes = [221,1066,686,855]
limit = 1000
curr_limit = 0
dp = []
n = len(minutes)

# while curr_limit <= limit:
def flights(minutes, limit):
    
    max_val = []
    for i in range(n):
        #flight will take minutes[i] on day i 
        max_val.append(minutes[i]+max(minutes[i-1],minutes[i-2]))
        # if max_val[i] <= limit:
        #     max_val = max_val[i]
    return min(max_val)
    # if max_val[i] != None:
    #     if max_val[i] <= limit:
    #         print(max_val[i])
    # print(min(max_val[n-2], max_val[n-1]))

       # print(max(minutes[n-1], dp[n-2]))
        # max(dp[n-1], dp[n-2])
        # if max_val < limit: 
        #     return max_val

    # max(minutes[i-1], dp[i-2])

print(flights(minutes, limit))
#sum of them should not exceed the limit and 
#curr value it also should not exceed the limit
