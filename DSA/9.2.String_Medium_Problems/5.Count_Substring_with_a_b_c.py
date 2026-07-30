''' Brute Force Approach '''

def count_Substring(s):
    count=0

    for i in range(len(s)):
        hash=[0]*3
        for j in range(i,len(s)):
            hash[ord(s[j])-ord('a')]=1
            if (hash[0]+hash[1]+hash[2])>=3:
                count+=len(s)-j   ## with this Optimization
                break
    return count

        
s="aaacb"
s="abcabc"
# print(count_Substring(s))

''' Optimal Approach '''

    
def count_Substring(s):
    hash=[-1]*3
    count=0
    for i in range(len(s)):
        hash[ord(s[i])-ord('a')]=i
        if hash[0]!=-1 and hash[1]!=-1 and hash[2]!=-1:
            mini=min(hash)
            count+=(1+mini)      
    return count

        
        
s="aaacb"
s="abcabc"
s="bbacba"
print(count_Substring(s))