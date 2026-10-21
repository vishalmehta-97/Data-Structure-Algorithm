class Solution:
    def getDigitSum(self,num):
        total=0
        while num>0:
            total+=num%10
            num=num//10
        
        return total
    
    ''' Manual Sort Func to sort by its digit sum'''
    # def custom_sort(self,afterSorted):
    #     n = len(afterSorted)
    #     for i in range(n):
    #         for j in range(n - i - 1):
    #             sum1 = self.getDigitSum(afterSorted[j])
    #             sum2 =self.getDigitSum(afterSorted[j + 1])

    #             if sum1 > sum2 or (sum1 == sum2 and afterSorted[j] > afterSorted[j + 1]):
    #                 afterSorted[j], afterSorted[j + 1] = afterSorted[j + 1], afterSorted[j]

    #     return afterSorted
    
    def minSwaps(self, nums):
        # afterSorted=nums.copy()
        # self.custom_sort(afterSorted)

        
        def sort_key(num):     ## Python Built in Custom Sort Function
            return (self.getDigitSum(num),num)
        afterSorted=sorted(nums,key=sort_key)    
        


        hashmap={}  ## this will hold the indexes of previous elements so that after sort we can figure it out how many swaps we have to make that sort by digit sum
        for i in range(len(nums)):
            hashmap[nums[i]]=i



        swapCount=0
        for i in range(len(afterSorted)):
            expected=afterSorted[i]
            currVal=nums[i]

            if currVal==expected:
                continue 
            else:
                checkIndexOfExpected=hashmap[expected]
                nums[i],nums[checkIndexOfExpected]=nums[checkIndexOfExpected],nums[i]
                swapCount+=1
                hashmap[expected]=i
                hashmap[currVal]=checkIndexOfExpected

        return swapCount


    
s=Solution()
nums=[18,43,34,16]
print(s.minSwaps(nums))