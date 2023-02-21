
def isSubsequence(s,t):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
   
    match = 0 
    for ti in range(0, len(t)):
        if match <= len(s) -1:
            if s[match] == t[ti]:
                match +=1
    return match == len(s)
        
def main():
    s = "abc"
    t = "ahbgdc"
    isSubsequence(s,t)

main()