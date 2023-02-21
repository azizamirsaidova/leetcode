"""
    Input: n = 2
    Output: 2
    
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

    n + 1, n+2 
    
    step: 4
    1. 1111
    2. 
    
    """


def climbStairs(n):
    memo = {}
    memo[1] = 1
    memo[2] = 2

    if n in memo:
        return memo[n]
    memo[n] = climbStairs(n-1, memo)+climbStairs(n-1, memo)
    return memo[n]

def main():
    n = 2
    climbStairs(n)

main()