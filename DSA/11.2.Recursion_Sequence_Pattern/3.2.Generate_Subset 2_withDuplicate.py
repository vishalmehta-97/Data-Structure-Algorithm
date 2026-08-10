'''Brute Force Approach'''

# class Solution:
#     def generate(self,subset,answer,nums,i):
#         if i>=len(nums):
#             if subset not in answer:  # to check duplicates
#                 answer.append(subset.copy())
#             return 
#         subset.append(nums[i])
#         self.generate(subset,answer,nums,i+1)
#         subset.pop()
#         self.generate(subset,answer,nums,i+1)
#         return
        

#     def subsetsWithDup(self, nums):
#         answer=[]
#         subset=[]
#         nums.sort()
#         self.generate(subset,answer,nums,0)
#         return answer

# # s=Solution()
# # nums=[4,4,4,1,4]
# # nums=[1,2,2]
# # print(s.subsetsWithDup(nums))


# ''' Better Approach'''

# class Solution:
#     def generate(self,subset,answer,nums,i):
#         if i>=len(nums):
#             answer.add(tuple(subset))
#             return
                 
#         subset.append(nums[i])
#         self.generate(subset,answer,nums,i+1)
#         subset.pop()
#         self.generate(subset,answer,nums,i+1)
#         return        

#     def subsetsWithDup(self, nums):
#         answer=set()
#         subset=[]
#         nums.sort()
#         self.generate(subset,answer,nums,0)
#         answerList=[]
#         for i in answer:
#             answerList.append(list(i))

#         return answerList

# s=Solution()
# nums=[4,4,4,1,4]
# nums=[1,2,2]
# print(s.subsetsWithDup(nums))


''' Optimal Approach'''

class Solution:
    def generate(self,subseq,answerArray,nums,index):
        answerArray.append(subseq.copy())
        # if index>=len(nums):
        #     return
    
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue

            subseq.append(nums[i])
            self.generate(subseq,answerArray,nums,i+1)
            subseq.pop()
        
        
    def subsetsWithDup(self, nums):
        answerArray=[]
        nums.sort()
        self.generate([],answerArray,nums,0)
        return answerArray
        

s=Solution()
nums=[4,4,4,1,4]
nums=[1,2,2]
print(s.subsetsWithDup(nums))