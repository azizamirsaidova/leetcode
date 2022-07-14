"""
Given a string s containing characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

UMPIRE:

Understand:

Input: s = "()"
Output: true

Input: s = "(]"
Output: false

Match:

Stack's pop and push methods

Plan:

1. Create a stack to store the brackets
2. Process each bracket as an expression
3. if bracket == ')]}', 
    check element on top of stack, if element on top stack is '([{', 
        then pop out of stack and continue
    else: imply as invalid expression

4. if bracket == '([{',
    push onto a stack

5. at the end, if there is a still expression, then this implies invalid expression.


"""

exp = "([{{{"

def isValid(exp):
    stack = [exp[0]]

    if exp == '':
        return True

    for i in range(1, len(exp)):
        if exp[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        
        elif exp[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        
        elif exp[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        else:
            stack.append(exp[i])
    
    return not stack
        


print(isValid(exp))
        