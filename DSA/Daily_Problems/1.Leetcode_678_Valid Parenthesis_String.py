class Solution:
    def mainCalculation(self,s,i,count):
        if count<0:
            return False
        if i==len(s):
            return count==0
        if s[i]=="(":
            return self.mainCalculation(s,i+1,count+1)
            
        if s[i]==")":
            return self.mainCalculation(s,i+1,count-1)

        if s[i]=="*":
            return self.mainCalculation(s,i+1,count+1) or self.mainCalculation(s,i+1,count-1) or self.mainCalculation(s,i+1,count)

        
    def checkValidString(self, s: str) -> bool:
        index=0
        return self.mainCalculation(s,index,0)
        
s=Solution()
ss="(((((()*)(*)*))())())(()())())))((**)))))(()())()"
print(s.checkValidString(ss))