# class Solution:
#     def countK_curr_sumSubsequence(self,nums,target,curr_sum,count,i):
#         if curr_sum == target:
#             count[0] += 1
#             return
#         if i >= len(nums) or curr_sum>target:
#             return

#         # subseq.append(nums[i])
#         curr_sum+=nums[i]
#         self.countK_curr_sumSubsequence(nums,target,curr_sum,count,i+1)
#         # subseq.pop()
#         curr_sum-=nums[i]
#         self.countK_curr_sumSubsequence(nums,target,curr_sum,count,i+1)
#         return 

        
#     def countSubsequenceWithTargetcurr_sum(self,nums,k):
#         curr_sum=0
#         count=[0]
#         self.countK_curr_sumSubsequence(nums,k,curr_sum,count,0)
#         return count[0]


# s=Solution()
# nums=[4,9,2,5,1]
# k=10
# print(s.countSubsequenceWithTargetcurr_sum(nums,k))

''' This is the code of Printing only one subsequence of the array '''

# class Solution:
#     def countK_curr_sumSubsequence(self,nums,target,subseq,answer,curr_sum,count,i):
#         if curr_sum == target:
#             answer.append(subseq.copy())
#             count[0] += 1
#             return True
#         if i >= len(nums) or curr_sum>target:
#             return False

#         subseq.append(nums[i])
#         curr_sum+=nums[i]
#         if self.countK_curr_sumSubsequence(nums,target,subseq,answer,curr_sum,count,i+1)==True:
#             return True
#         subseq.pop()
#         curr_sum-=nums[i]
#         if self.countK_curr_sumSubsequence(nums,target,subseq,answer,curr_sum,count,i+1)==True:
#             return True
#         return False

        
#     def countSubsequenceWithTargetcurr_sum(self,nums,k):
#         curr_sum=0
#         count=[0]
#         subseq=[]
#         answer=[]
#         self.countK_curr_sumSubsequence(nums,k,subseq,answer,curr_sum,count,0)
#         return answer
        

# s=Solution()
# nums=[1,2,1]
# k=2
# print(s.countSubsequenceWithTargetcurr_sum(nums,k))

'''If you just want the Count'''

class Solution:
    def countK_curr_sumSubsequence(self,nums,target,curr_sum,i):
        if curr_sum == target:
            return 1
        if i >= len(nums) or curr_sum>target:
            return 0

        curr_sum+=nums[i]
        l=self.countK_curr_sumSubsequence(nums,target,curr_sum,i+1)
        curr_sum-=nums[i]
        r=self.countK_curr_sumSubsequence(nums,target,curr_sum,i+1)
        return l+r

        
    def countSubsequenceWithTargetcurr_sum(self,nums,k):
        curr_sum=0
        return self.countK_curr_sumSubsequence(nums,k,curr_sum,0)
        
        

s=Solution()
nums=[1,4,3,5,3,2,1]
k=6
print(s.countSubsequenceWithTargetcurr_sum(nums,k))

