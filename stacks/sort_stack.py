"""
Write a program to sort a stack such that the smallest items are on top. 
You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).

The stack supports the following operations : push, pop, peek, isEmpty.

UMPIRE:

Understand:

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]


Match:
- Sort method
- Stack methods

Plan 1:
1. Create a stack 
2. If value not yet in stack,
    if curr value is less

Plan 2:
1. Create an additional temporary Stack.
2. While input stack is NOT empty do:
3. Pop an element from input stack called temp.
4. While temporary stack is NOT empty and top of temporary stack is greater than temp:
5. Pop from temporary stack and push it to the input stack.
6. Push temp in temporary stack.
7. In the end, the sorted numbers are in the temporary Stack.
"""

arr = [34, 3, 31, 98, 92, 23]

def sort_stack(arr):
    stack = []

    while len(arr) != 0:
        temp = arr.pop()

        while len(stack) != 0 and stack[len(stack)-1] > temp:
            arr.append(stack[len(stack)-1])
            stack.pop()
        
        stack.append(temp)
    
    return stack

print(sort_stack(arr))