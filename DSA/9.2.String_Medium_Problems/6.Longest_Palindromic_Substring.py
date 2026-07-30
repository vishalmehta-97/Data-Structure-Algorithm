def check_Palindrome(s):
    i=0
    j=len(s)-1

    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True


def longestPalindrome(s):
    ans=''
    length=-1
    for i in range(len(s)):
        for j in range(i,len(s)):
            if check_Palindrome(s[i:j+1]):
                if len(s[i:j+1])>length:
                    ans=s[i:j+1]
                    length=len(s[i:j+1])
                    
    return ans

s="babad"
s="cbbd"
# print(longestPalindrome(s))


''' Optimal Approach '''
        
def longestPalindrome_opt(s):
    ans_length=0
    ans=''
    for i in range(len(s)):
        
        low,high=i,i   ## When Numbers are odd
        while low>=0 and high<len(s) and s[low]==s[high]:
            if ans_length<len(s[low:high+1]):
                ans=s[low:high+1]
                ans_length=len(s[low:high+1])   ## Instead of len(s[low:high+1]) we can also use this [high-low+1]
            low-=1
            high+=1

    
        low,high=i,i+1   ## When Numbers are even
        while low>=0 and high<len(s) and s[low]==s[high]:
            if ans_length<len(s[low:high+1]):
                ans=s[low:high+1]
                ans_length=len(s[low:high+1])
            low-=1
            high+=1
    return ans

s="cbbd"
s="babad"
print(longestPalindrome_opt(s))

