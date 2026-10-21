''' Better Approach '''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(score)
                score=0
            else:
                if s[i-1]=="(":
                    score=stack[-1]+1
                else:
                    score=stack[-1]+2*(score)
                stack.pop()
                
        return score
        
s=Solution()
ss="(())"
print(s.scoreOfParentheses(ss))


''' Optimal Approach '''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        depth=0

        for i in range(len(s)):
            if s[i]=="(":
                depth+=1
            else:
                if s[i-1]=="(":
                    score+=2**(depth-1)
                depth-=1
        return score
        
s=Solution()
ss="(())"
print(s.scoreOfParentheses(ss))
        
