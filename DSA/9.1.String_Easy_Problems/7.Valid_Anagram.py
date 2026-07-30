''' Brute Force Approach '''

def isAnagram(s,t):
    if len(s) != len(t):
        return False

    for ch in s:
        count1 = 0
        count2 = 0
        for c in s:
            if c == ch:
                count1 += 1
        for c in t:
            if c == ch:
                count2 += 1
        if count1 != count2:
            return False
    return True

s="anagram"
t="nagaram"
# s="rat"
# t="car"
# s="aa"
# t="bb"

# print(isAnagram(s,t))

''' Another Burte Force Approach '''
def isAnagram__(s,t):
    if len(s) != len(t):
        return False
    if sorted(s)==sorted(t):
        return True
    return False
    

s="anagram"
t="nagaram"
# s="rat"
# t="car"
# s="aa"
# t="bb"

# print(isAnagram__(s,t))

''' Optimal Approach '''

def isAnagram_(s,t):
    if len(s)!=len(t):
        return False
    hash={}

    for i in range(len(s)):
        hash[s[i]]=hash.get(s[i],0)+1
    for i in range(len(t)):
        hash[t[i]]=hash.get(t[i],0)-1

    for value in hash.values():
        if value!=0:
            return False
    return True

s="anagram"
t="nagaram"
# s="rat"
# t="car"
s="aa"
t="bb"

# print(isAnagram_(s,t))
'''Optimal Approach Using array'''

def isAnagram_opt(s,t):
    if len(s)!=len(t):
        return False
    freq=[0]*26

    for char in s:
        freq[ord(char)-ord('a')]+=1

    for char in t:
        freq[ord(char)-ord('a')]-=1
    
    for count in freq:
        if count!=0:
            return False
    return True


s="anagram"
t="nagaram"
# s="rat"
# t="car"
# s="aa"
# t="bb"

print(isAnagram_opt(s,t))

