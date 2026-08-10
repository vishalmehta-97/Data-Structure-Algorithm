class Solution:
    def generate(self,digits,ansArray,alphaList,ans,index):
        if len(ans)==len(str(digits)):
            ansArray.append(ans)
            return

        for i in range(len(alphaList[int(digits[index])-1])):
            self.generate(digits,ansArray,alphaList,ans+alphaList[int(digits[index])-1][i],index+1)


    def letterCombinations(self,digits):
        ansArray=[]
        alphaList=["","abc","def",
                   "ghi","jkl","mno",
                   "pqrs","tuv","wxyz"
        ]
        ans=''       
        digits=str(digits) 
        i=0
        self.generate(digits,ansArray,alphaList,ans,i)
        return ansArray
s=Solution()
print(s.letterCombinations(digits=23))
        