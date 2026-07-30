''' Optimal Approach '''

def maxDepth(s):
    para_Count=0
    ans=0
    for para in s:
        if para=='(':
            para_Count+=1
            ans=max(ans,para_Count)
        elif para==')':
            para_Count-=1
    return ans


s="(1)+((2))+(((3)))"
# s="()(())((()()))"
# s="(1+(2*3)+((8)/4))+1"
print(maxDepth(s))