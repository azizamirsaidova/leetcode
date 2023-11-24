"""
    Diet Plan Performance
    A dieter consumes calories[i] calories on the i-th day. 

    Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

    If T < lower, they performed poorly on their diet and lose 1 point; 
    If T > upper, they performed well on their diet and gain 1 point;
    Otherwise, they performed normally and there is no change in points.
    Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.

    Note that the total points can be negative.
    Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
    Output: 0
    Explanation: Since k = 1, we consider each element of the array separately and compare it to lower and upper.
    calories[0] and calories[1] are less than lower so 2 points are lost.
    calories[3] and calories[4] are greater than upper so 2 points are gained.

"""

def diet_plan(calories, k, lower, upper):
    n = len(calories)
    totalCalsForDay = sum(calories[:k])
    countPoints = 0
    if totalCalsForDay < lower:
            countPoints -= 1
    elif totalCalsForDay > upper:
        countPoints += 1

    for i in range(n-k):
        totalCalsForDay = totalCalsForDay - calories[i] + calories[i+k]
        if totalCalsForDay < lower:
            countPoints -= 1
        elif totalCalsForDay > upper:
            countPoints += 1
    return countPoints

def main():
    calories = [1,2,3,4,5]
    k = 1
    lower = 3
    upper = 3
    print(diet_plan(calories, k, lower, upper))

if __name__ == "__main__":
    main()