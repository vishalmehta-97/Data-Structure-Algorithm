''' Brute Force Approach '''

def median_of_2Sorted_Array(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)

    i=j=0
    sorted_array=[]

    while i<n1 and j<n2:
        if nums1[i]>nums2[j]:
            sorted_array.append(nums2[j])
            j+=1
        else:
            sorted_array.append(nums1[i])
            i+=1
            
    while i<n1:
        sorted_array.append(nums1[i])
        i+=1
    while j<n2:
        sorted_array.append(nums2[j])
        j+=1

    if len(sorted_array)%2!=0:
        low=0
        high=len(sorted_array)-1
        mid=(low+high)//2
        ans=sorted_array[mid]
        return float(ans)
    else:
        low=0
        high=len(sorted_array)-1
        mid=(low+high)//2
        ans=(sorted_array[mid]+sorted_array[mid+1])/2
        return ans
        
# nums1=[1,3]
# nums2=[2]
nums1=[1,2]
nums2=[3,4]
# print(median_of_2Sorted_Array(nums1,nums2))

''' Better Approach'''

def median_of_2Sorted_Array_(nums1,nums2):

        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2

        i = j = 0
        idx_element = 0
        prev_element = 0

        for count in range((n // 2) + 1):
            prev_element = idx_element
            if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
                idx_element = nums1[i]
                i += 1
            else:
                idx_element = nums2[j]
                j += 1
        if n % 2 != 0:
            return float(idx_element)
        else:
            return (prev_element + idx_element) / 2

        
nums1=[1,3]
nums2=[2]
# nums1=[1,3,4,7,10,12]
# nums2=[2,3,6,15]

# nums1=[]
# nums2=[2,3]
nums1=[7,12,14,15]
nums2=[1,2,3,4,9,11]
nums1=[1,2]
nums2=[3,4]
print(median_of_2Sorted_Array_(nums1,nums2))

''' Optimal Approach '''

def median_of_2Sorted_Array_opt(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)
    if n1>n2:
        return median_of_2Sorted_Array_opt(nums2,nums1)    ## We have done this because of we want to work this in only short len of array so that we can reduce the time Complexity
    n=n1+n2
    low=0
    high=n1
    left=(n+1)//2

    while low<=high:
        mid=(low+high+1)//2
        mid2=left-mid

        ## Assigning default values for the cases where the mid==0 or maybe more than the len of the element
        l1=float('-inf')
        l2=float('-inf')
        r1=float('inf')
        r1=float('inf')

        if mid-1>=0: l1=nums1[mid-1]
        if mid2-1>=0: l2=nums2[mid2-1]
        if mid<n1: r1=nums1[mid]
        if mid2<n2: r2=nums2[mid2]
        
        if l1<=r2 and l2<=r1:
            if n%2==0:
                return (max(l1,l2)+min(r1,r2))/2.0
            else:
                return float(max(l1,l2))
        else:
            if l1>r2:
                high=mid-1
            elif l2>r1:
                low=mid+1
    return 0
    
nums1=[1,3]
nums2=[2]
nums1=[7,12,14,15]
nums2=[1,2,3,4,9,11]
nums1=[1,2]
nums2=[3,4]
print(median_of_2Sorted_Array_opt(nums1,nums2))