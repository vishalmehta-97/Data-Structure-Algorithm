''' Brute Force Approach '''

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans=[-1]*len(nums1)

        for i in range(len(nums1)):
            indexi=nums2.index(nums1[i])
            for j in range(indexi+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
        return ans
    
s=Solution()
nums1=[4,1,3]
nums2=[1,3,4,2]
nums1=[4,1,2]
nums2=[1,2,3,4]
# print(s.nextGreaterElement(nums1,nums2))


                
''' Optimal Approach '''

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans=[0]*len(nums1)
        hash={}
        stack=[]

        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                hash[nums2[i]]=-1
            else:
                if stack[-1]>nums2[i]:
                    hash[nums2[i]]=stack[-1]
                else:
                    while len(stack)!=0 and (stack[-1]<=nums2[i]):
                        stack.pop()
        
                    if not stack:
                        hash[nums2[i]]=-1
                    else:
                        hash[nums2[i]]=stack[-1]

            stack.append(nums2[i])

        for i in range(len(nums1)):
            ans[i]=hash.get(nums1[i])

        return ans
        
s=Solution()
nums1=[4,1,3]
nums2=[1,3,4,2]
nums1=[4,1,2]
nums2=[1,2,3,4]
# nums2=[4,12,5,3,1,2,5,3,1,2,4,6]
print(s.nextGreaterElement(nums1,nums2))
                