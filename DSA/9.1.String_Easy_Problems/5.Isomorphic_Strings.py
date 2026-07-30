''' Brute Force Approach '''

def isIsomorphic(s,t):
    if len(s)==len(t):
        hash={}
        i=0
        while i<len(s):
            if s[i] not in hash:
                if t[i] in hash.values():
                    print(hash)
                    return False
                else:
                    hash[s[i]]=t[i]
            else:
                if hash.get(s[i])!=t[i]:
                    return False
                else:
                    hash[s[i]]=t[i]
            i+=1
        print(hash )
        return True
        
    return False

s="egg"
t="add"  
s="f11"
t="b23"
s="badc"
t="baba"
s="paper"
t="title"
# print(isIsomorphic(s,t))    

''' Optimal Approach '''

def isIsomorphic_(s,t):
    if len(s)==len(t):
        hashST,hashTS={},{}

        for i in range(len(s)):
            if ((s[i] in hashST) and hashST[s[i]]!=t[i]) or ((t[i] in hashTS) and hashTS[t[i]]!=s[i]):
                return False
            hashST[s[i]]=t[i]
            hashTS[t[i]]=s[i]
        return True

s="egg"
t="add"  
s="f11"
t="b23"
s="badc"
t="baba"
s="paper"
t="title"
print(isIsomorphic_(s,t))    

'''There is one more Approach Using Arrays which is in the striver sheet soltution which is lil bit more optimal'''

