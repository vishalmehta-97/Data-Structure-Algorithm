''' Brute Force O(n) Space '''

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        boolArray=[False]*(n+1)

        for i in range(len(nums)):
            if 0>=nums[i] or nums[i]>n:
                continue
            else:
                boolArray[nums[i]]=True

        for i in range(1,len(boolArray)):
            if boolArray[i]==False:
                return i


s=Solution()
nums=[3,4,-1,1]
print(s.firstMissingPositive(nums))


''' Optimal Approach '''

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        containOne=False  ## Deal with 1 Before and number which are (greater than n) or (smaller or equal to 0 make them 1 )      
        for i in range(n):
            if nums[i]==1:
                containOne=True
            if nums[i]>n or nums[i]<=0:
                nums[i]=1
        
        if containOne==False:
            return 1
        
        for i in range(n):
            value_index=abs(nums[i])
            if nums[value_index-1]<0:
                continue

            nums[value_index-1]=nums[value_index-1]*(-1)

        for i in range(n):
            if nums[i]>0:
                return i+1
        
        return n+1


s=Solution()
nums=[3,4,-1,1]
print(s.firstMissingPositive(nums))



def append_item(item, target_list=[]):
    target_list.append(item)
    return target_list
