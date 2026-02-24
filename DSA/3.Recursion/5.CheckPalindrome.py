'''eg: MADAM'''

def checkPalindrome(l,r):
    if l>=r:
        return True ,"Its an Palindrome"
    # if string==" ":
    #     return True
    
    if string[l]!=string[r]:
        return False , "Its not an Palindrome"
    elif string[l]==string[r]:
        return checkPalindrome(l+1,r-1)
    

string=input("Enter The Element:").lower()
string = ''.join(c for c in string if c.isalnum())
print(checkPalindrome(0,len(string)-1))
print(string)


def checkPalindrome(l, r):
    if l >= r:
        return True
    
    if string[l] != string[r]:
        return False
    
    return checkPalindrome(l+1, r-1)


string = input("Enter: ").lower()

# remove non-alphanumeric characters
string = ''.join(c for c in string if c.isalnum())

print(checkPalindrome(0, len(string)-1))
