from typing import List

''' Brute Force Approach '''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total=0
        mod=1e9+7
        for i in range(len(arr)):
            mini=arr[i]
            for j in range(i,len(arr)):
                mini=min(mini,arr[j])
                total+=mini

        return total%mod


s=Solution()
arr=[1,4,6,7,3,7,8,1]
arr=[3,1,2,4]


print(s.sumSubarrayMins(arr))


'''Brute Force Approach '''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total=0
        mod=1e9+7
        for i in range(len(arr)):
            stack=[]
            for j in range(len(arr)-i-1,-1,-1):
                if not stack:
                    stack.append(arr[j])
                    total+=arr[j]
                else:
                    if arr[j]>stack[-1]:
                        total+=stack[-1]
                    else:
                        stack.append(arr[j])
                        total+=arr[j]
        return total% mod


s=Solution()
arr=[3,1,2,4]
# print(s.sumSubarrayMins(arr))

''' Optimal Approach '''

class Solution:
    def prevSmallerEle_index(self,arr):
        stack=[]
        previous_smaller=[0]*len(arr) 

        for i in range(len(arr)):
            while stack and stack[-1][0]>arr[i]:
                stack.pop()

            if not stack:
                previous_smaller[i]=-1
            else:
                previous_smaller[i]=stack[-1][1]

            stack.append((arr[i],i))
            
        return previous_smaller            


    def nextSmallerEle_index(self,arr):
        stack=[]
        next_smaller=[0]*len(arr) 
        for i in range(len(arr)-1,-1,-1):
            while stack and stack[-1][0]>=arr[i]:
                stack.pop()

            if not stack:
                next_smaller[i]=len(arr)
            else:
                next_smaller[i]=stack[-1][1]
            stack.append((arr[i],i))  

        return next_smaller
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=1e9+7
        totalSum=0

        next_smaller=self.nextSmallerEle_index(arr)   ## this will give the index of Next Smaller Element for each Element in the array
        previous_smaller=self.prevSmallerEle_index(arr)   ## this will give the index of Previous Smaller Element for each Element in the array
        for i in range(len(arr)):
            min_total_times=(i-previous_smaller[i])*(next_smaller[i]-i)
            totalSum+=(min_total_times*arr[i]) %mod    
        print(next_smaller,previous_smaller)  

           
        return int((totalSum)%mod)


s=Solution()
arr=[1,4,6,7,3,7,8,1]
# arr=[3,1,2,4]
print(s.sumSubarrayMins(arr))