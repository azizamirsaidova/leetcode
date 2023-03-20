"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""
num = [10, 15, 3, 7]
k = 17
val = 1
for i in range(len(num)):
    total = num[i] + num[val]
    if k != total:
        val += 1
    else:
        print("No")
    
