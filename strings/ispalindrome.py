def is_palindrome(str1):
    
    for i in range(0, len(str1)//2):
        if str1[i] != str1[~i]:
            return False
    return True

    print(len(str1)//2)

def is_palindrome_2(str1):
    start = 0
    end = len(str1)-1

    while start >
def main():
    print("Is palindrome, ", is_palindrome('issi'))

main()