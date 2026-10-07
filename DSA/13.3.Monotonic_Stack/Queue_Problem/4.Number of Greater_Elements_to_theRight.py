''' Brute Force Approach '''
class Solution:
    def count_NGE(self, arr, indices):
        ansArray=[]
        for i in indices:
            count=0
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    count+=1
            ansArray.append(count)

        return ansArray

s=Solution()
arr=[3,4,2,7,5,8,10,6] 
indices=[0,5]
# print(s.count_NGE(arr,indices))
            

''' Optimal Approach '''

class Solution:
    def count_NGE(self, arr, indices):
        ans=[0]*len(indices)
        stack=[]
        ii=1
        count=0
        for i in range(len(arr)-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                if stack[-1]>arr[]
                stack.pop()
        
            count+=1
            stack.append(arr[i])

            if arr[i] in indices:
                if arr[i]==indices[ii]:
                    ans[ii]=count
                    ii-=1
                if ii==0:
                    return ans
s=Solution()
arr=[3,4,2,7,5,8,10,6] 
indices=[0,5]
print(s.count_NGE(arr,indices))