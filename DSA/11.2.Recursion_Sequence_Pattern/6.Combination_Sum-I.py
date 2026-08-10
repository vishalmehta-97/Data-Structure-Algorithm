class Solution:
    def generate(self,candy,target,array,subseq,curr_sum,i):
        if curr_sum==target:
            array.append(subseq.copy())
            return
        if i>=len(candy) or curr_sum>target:
            return 

        subseq.append(candy[i])
        curr_sum+=candy[i]
        self.generate(candy,target,array,subseq,curr_sum,i)

        subseq.pop()
        curr_sum-=candy[i]
        self.generate(candy,target,array,subseq,curr_sum,i+1)

    def combinationSum(self,candidates,target):
        array=[]
        subseq=[]
        curr_sum=0
        self.generate(candidates,target,array,subseq,curr_sum,0)
        return array
    
s=Solution()
candidates=[2,3,6,7]
target=7
print(s.combinationSum(candidates,target))

''' Same code but with more cleaniness'''

class Solution:
    def generate(self,candy,target,array,subseq,i):
        if i==len(candy):
            if target==0:
                array.append(subseq.copy())
            return

        if candy[i]<=target:
            subseq.append(candy[i])
            self.generate(candy,target-candy[i],array,subseq,i)
            subseq.pop()
            
        self.generate(candy,target,array,subseq,i+1)

    def combinationSum(self,candidates,target):
        array=[]
        subseq=[]
        self.generate(candidates,target,array,subseq,0)
        return array
    
s=Solution()
candidates=[2,3,6,7]
target=7
print(s.combinationSum(candidates,target))

        