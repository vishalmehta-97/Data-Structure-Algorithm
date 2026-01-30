def isPalindrome(x):
    TheNo=x
    x=abs(x)
    reverse=0
    while (x>0):
        lastdigit=x%10
        reverse=(reverse*10)+lastdigit
        x=x//10

    # if reverse<0:
    #     return False
    if reverse==TheNo:
        return True
    else:
        return False
    
print(isPalindrome())