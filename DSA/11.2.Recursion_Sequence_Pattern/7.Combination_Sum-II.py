class Solution:
    def generate(self,candy,target,i,curr_sum,subseq,ans_Array):
        if curr_sum==target:
            if subseq not in ans_Array:
                ans_Array.append(subseq.copy())
            return
        if i>=len(candy) or curr_sum>target:
            return

        subseq.append(candy[i])
        curr_sum+=candy[i]
        self.generate(candy,target,i+1,curr_sum,subseq,ans_Array)

        subseq.pop()
        curr_sum-=candy[i]
        self.generate(candy,target,i+1,curr_sum,subseq,ans_Array)
        


    def combinationSum2(self,candidates,target):
        ans_Array=[]
        subseq=[]
        curr_sum=0
        candidates.sort()
        self.generate(candidates,target,0,curr_sum,subseq,ans_Array)
        return ans_Array
            

s=Solution()
candidates=[10,1,2,7,6,1,5]
target=8
print(s.combinationSum2(candidates,target))


''' Brute Force Approach '''

class Solution:
    def generate(self,candy,target,i,curr_sum,subseq,ans_set):
        if curr_sum==target:
            ans_set.add(tuple(subseq))
            return
        if i>=len(candy) or curr_sum>target:
            return

        subseq.append(candy[i])
        self.generate(candy,target,i+1,curr_sum+candy[i],subseq,ans_set)

        subseq.pop()
        self.generate(candy,target,i+1,curr_sum,subseq,ans_set)
        
        
    def combinationSum2(self,candidates,target):
        ans_set=set()
        subseq=[]
        curr_sum=0
        candidates.sort()
        self.generate(candidates,target,0,curr_sum,subseq,ans_set)
        ans_array=[]
        for i in ans_set:
            ans_array.append(list(i))
        return ans_array
 
s=Solution()
candidates=[10,1,2,7,6,1,5]
target=8
print(s.combinationSum2(candidates,target))
        
''' Optimal Approach '''
class Solution:
    def generate(self,candy,target,index,subseq,ans_Array):
        if target==0:
            ans_Array.append(subseq.copy())
            return
        for i in range(index,len(candy)):
            if i>index and candy[i]==candy[i-1]:
                continue
            if candy[i]>target:
                break

            subseq.append(candy[i])
            self.generate(candy,target-candy[i],i+1,subseq,ans_Array)
            subseq.pop()

    def combinationSum2(self,candidates,target):
        ans_Array=[]
        subseq=[]
        candidates.sort()
        self.generate(candidates,target,0,subseq,ans_Array)
        return ans_Array
        

s=Solution()
candidates=[10,1,2,7,6,1,5]
target=8
print(s.combinationSum2(candidates,target))