class Solution:

    def merge(self,array,low,mid,high):
        merged_list=[]
        l=low
        r=mid+1
        while l<=mid and r<=high:
            if array[l]<=array[r]:
                merged_list.append(array[l])
                l+=1
        
            else:
                merged_list.append(array[r])
                r+=1

        while l<=mid:
            merged_list.append(array[l])
            l+=1

        while r<=high:
            merged_list.append(array[r])
            r+=1

        for i in range(len(merged_list)):
            arr[low+i]=merged_list[i]

    def merge_sort(self,array,low,high):
        if low>=high:
            return
        
        mid=(low+high)//2
        
        self.merge_sort(array,low,mid)
        self.merge_sort(array,mid+1,high)
        self.merge(array,low,mid,high)



arr=[3,1,2,4,1,5,2,6,4]
sol=Solution()
sol.merge_sort(arr,0,len(arr)-1)
print(arr)