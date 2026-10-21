''' Brute Force Approach '''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n=len(s)
        stack=[]
        for i in range(len(s)):
            
            if s[i]=="(":
                stack.append("(")
            elif stack and stack[-1]=="(" and s[i]==")":
                stack.pop()
                n-=2

        return n
s=Solution()
ss="())"
# ss="((("
# ss="()))(("
print(s.minAddToMakeValid(ss))


''' Optimal Approach '''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count=0
        added=0

        for chr in s:
            if chr=="(":
                open_count+=1
            else:
                if open_count>0:
                    open_count-=1
                else:
                    added+=1

        return added+open_count        
s=Solution()
# ss="())"
# ss="((("
ss="()))(("
print(s.minAddToMakeValid(ss))