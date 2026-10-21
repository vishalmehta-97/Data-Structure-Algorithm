import heapq

''' Brute Force Approach '''
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        priority=[]

        for i in range(len(nums1)):
            diff=abs(nums1[i]-nums2[i])
            heapq.heappush(priority,(-diff))
        k=k1+k2  

        while k!=0:
            if priority[0]==0:
                break
            ele=-(heapq.heappop(priority))
            ele-=1
            heapq.heappush(priority,(-ele))
            k-=1


        result=0
        for i in priority:
            result+=i**2

        return result

s=Solution()

nums1=[10,10,10,11,5]
nums2=[1,0,6,6,1]

k1=11
k2=27
# print(s.minSumSquareDiff(nums1,nums2,k1,k2))


''' Optimal Approach '''

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff=[0]*((10**5)+1)

        for i in range(len(nums1)):
            difference=abs(nums1[i]-nums2[i])
            diff[difference]+=1
            
        k=k1+k2  

        for i in range(len(diff)-1,0,-1):   ## o instead of -1
            if k>0:
                noOfOps=min(k,diff[i])
                diff[i]-=noOfOps
                diff[i-1]+=noOfOps
                k-=noOfOps
            else:
                break

        result=0
        for i in range(len(diff)):
            result+=(diff[i]*(i*i))
        return result
            
s=Solution()

nums1=[10,10,10,11,5]
nums2=[1,0,6,6,1]

k1=11
k2=27
print(s.minSumSquareDiff(nums1,nums2,k1,k2))
