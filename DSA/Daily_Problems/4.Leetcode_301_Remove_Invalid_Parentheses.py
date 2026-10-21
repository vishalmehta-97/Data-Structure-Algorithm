class Solution:
    def solver(self,s,i,count,ss,max_slength,ansSet):
        if count<0:  ## Early Pruning
            return
        if i==len(s):
            if count==0:
                if len(ss)>max_slength[0]:
                    max_slength[0]=len(ss)
                    ansSet.clear()
                if len(ss)==max_slength[0]:
                    ansSet.add(ss)
            return


        if s[i]!='(' and s[i]!=')':
            self.solver(s,i+1,count,ss+s[i],max_slength,ansSet)            

        else:
            self.solver(s,i+1,count+(1 if s[i]=='(' else -1),ss+s[i],max_slength,ansSet)
            self.solver(s,i+1,count,ss,max_slength,ansSet)
        

    def removeInvalidParentheses(self, s: str) -> list[str]:
        i=0
        ansSet=set()
        count=0
        max_slength=[-1]
        ss=""
        self.solver(s,i,count,ss,max_slength,ansSet)
        ansList=[]
        for i in ansSet:
            ansList.append(i)
        return ansList

s=Solution()
ss="()())()"
# ss="(()"
print(s.removeInvalidParentheses(ss))