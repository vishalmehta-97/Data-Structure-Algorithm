class Solution:
    def helper(self,n,s,count):
        if len(s)==n:
            count+=1
            return
        
        self.helper(n,s+'0',count)
        if not s or s[-1]!='1':
            self.helper(n,s+'1',count)
            
    def countStrings(self, n):
        count=0
        self.helper(n,"",count)
        return int(count)


s=Solution()
n=3
print(s.countStrings(n))