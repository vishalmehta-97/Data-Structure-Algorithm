class Solution:
    def generate(self,n,para,array,open,close):
        if len(para)==2*n:
            array.append(para)
            return
        
        if open<n:
            self.generate(n,para+"(",array,open+1,close)
        if close<n and open>close:
            self.generate(n,para+")",array,open,close+1)
        
    def generateParenthesis(self,n):
        para=""
        array=[]
        self.generate(n,para,array,0,0)
        return array
s=Solution()
# n=1
n=3
print(s.generateParenthesis(n))
        