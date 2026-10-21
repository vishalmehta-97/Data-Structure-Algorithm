class Solution:
    def longestValidParentheses(self, s: str) -> int:
        op=0
        close=0
        maxlen=0

        for i in range(len(s)):
            if s[i]=="(":
                op+=1
            else:
                close+=1
            
            if close==op:
                maxlen=max(maxlen,op+close)
            if close>op:
                op=0
                close=0
        
        op=0
        close=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                op+=1
            else:
                close+=1

            if close==op:
                maxlen=max(maxlen,op+close)
            if op>close:
                op=0
                close=0

        return maxlen
                


s=Solution()
ss="(()"
ss=")()())"
print(s.longestValidParentheses(ss))