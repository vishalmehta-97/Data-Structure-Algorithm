class Solution:
    def helper(self,index,ans,s):
        if index >= len(s):
            return ans
        if not s[index].isdigit():
            return ans
        ans=ans*10+int(s[index])
        return self.helper(index+1,ans,s)
        
    def myAtoi(self,s):
        ans=0
        s=s.strip()
        sign=1
        if len(s)==0:
            return 0

        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign=-1
            s=s[1:]

        ans=sign*self.helper(0,ans,s)
        
        if ans<-2**31:
            return -2**31
        elif ans>2**31-1:
            return 2**31-1
        else:
            return ans

s=Solution()

print(s.myAtoi(s="-042"))