"""
Write a function to evaluate the value of an expression in postfix notation represented 
by a string with numbers between 0 and 9 and operators separated by whitespace. 
The expression supports 4 binary operators '+', '*', '-' and '/'.

Infix: 3+4
Prefix: +3 4 
Postfix: 3 4+

UMPIRE:

Understand:
input = ["2","1","+","3","*"]
Output: 9
The expression is evaluated as follows: ((2 + 1) * 3) = 9

Match:
Stack's pop method

Plan:
1. Create a Stack which will store the numbers.
2. When you come across an operator, pop the top two elements from the stack.
3. Create a switch case which will act based on the type of the operator.
4. For each switch case, perform their operations on the two variables and push the result into the stack again.
5. At the end of the traversal, the element at the top of the stack is the result.


"""

# ip = ["2","1","+","3","*"]
ip = ["2"]
def postfix(ip):
    stack = []

    for i in ip:
        if i not in "+-/*":
            stack.append(int(i))
            continue
        
        num1 = stack.pop()
        num2 = stack.pop()

        result = 0
        if i == '+':
            result = num1 + num2
        elif i == '-':
            result = num1 - num2
        elif i == '/':
            result = int(num1 / num2)
        elif i == '*':
            result = num1 * num2
        stack.append(result)
    
    return stack.pop()
print(postfix(ip))