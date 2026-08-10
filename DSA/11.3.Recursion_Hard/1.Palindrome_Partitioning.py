class Solution:
    def palindrome(self,ss):
        i=0 
        j=len(ss)-1
        while i<j:
            if ss[i]!=ss[j]:
                return False
            i+=1
            j-=1 
        return True

    def generate(self,s,ansArray,subString,index):
        if index==len(s):
            ansArray.append(subString.copy())
            return

        for i in range(index,len(s)):
            if self.palindrome(s[index:i+1])==True:
                subString.append(s[index:i+1])
                self.generate(s,ansArray,subString,i+1)
                subString.pop()

    def partition(self,s):
        ansArray=[]
        subString=[]
        self.generate(s,ansArray,subString,0)
        return ansArray

s=Solution()
ss="aab"
print(s.partition(ss))
