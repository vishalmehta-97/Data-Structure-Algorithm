''' Brute Force Approach '''

def longestCommonPrefix_(strs):
    strs.sort()

    start=strs[0]
    end=strs[len(strs)-1]

    if len(start)>len(end):
        start,end=end,start
    i=0
    while i<len(start):
        if start[i]!=end[i]:
            return start[:i]
        i+=1
    return start[:i]


str=["flower","flow","flights"]
str=["dog","racecar","car"]
str=["a"]
str=[""]
str=["",""]
print(longestCommonPrefix_(str))


'''Optimal Approach'''

def check_Prefix(anss,strr):
    n=len(anss)
    m=len(strr)
  
    if m<n:
        return check_Prefix(strr,anss)
    i=0
    # j=0
    answer=''
    while i<n:
        '''We can also use this approach (small issue is that in py string is immutable so every time python makes a new string after this answer+=...)'''
        # if anss[i]==strr[i]:
        #     answer+=anss[i]
        #     i+=1
        # else:
        #     return answer
        if anss[i]!=strr[i]:
            return anss[:i]   ## Here we are checking in the anss which was the old prefix if some index matches it will reflect there
        i+=1
    return anss
def longestCommonPrefix(str):
    if len(str)==1:
            return str[0]
    ans=str[0]
    if len(ans)==0:
        return ""
    
    for i in range(1,len(str)):
        ans=check_Prefix(ans,str[i])

    return ans

str=["flower","flow","flight"]
# str=["dog","racecar","car"]
# str=["a"]
# str=[""]
# str=["",""]
# print(longestCommonPrefix(str))


