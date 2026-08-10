class Solution:
    def generate(self,subset,answer,nums,i):
        if i>=len(nums):
            # if subset not in answer:  # to check duplicates
            answer.append(subset.copy())
            return 
        subset.append(nums[i])
        self.generate(subset,answer,nums,i+1)
        subset.pop()
        self.generate(subset,answer,nums,i+1)
        return

    def subsetsWithDup(self,nums):
        answer=[]
        subset=[]
        self.generate(subset,answer,nums,0)
        return answer


s=Solution()
nums=[1,2,2]
print(s.subsetsWithDup(nums))


        