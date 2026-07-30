''' Brute Force '''
def rotateString(s,goal):
    if len(s)!=len(goal):
        return False
    
    for i in range(len(s)):
        rotated=s[i:]+s[:i]

        if goal==rotated:
            return True
    return False
    


s="abcde"
goal="cdeab"
print(rotateString(s,goal))

''' Optimal Approach '''

def rotateString_(s,goal):
    if len(s)!=len(goal):
        return False
    s+=s
    if goal in s:
        return True 
    return False
   

s="abcde"
goal="cdeab"
print(rotateString_(s,goal))