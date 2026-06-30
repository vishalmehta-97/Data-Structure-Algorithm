''' Brute Force Approach '''

def Kth_Element(nums1,nums2,k):
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

    return sorted_array[k-1]


nums1=[2,3,6,7,9]
nums2=[1,4,8,10]
k=4
# print(Kth_Element(nums1,nums2,k))


''' Better Approach '''

def Kth_Element_(nums1,nums2,k):
    n1=len(nums1)
    n2=len(nums2)

    i=j=0
    count=0
    previous_el=0

    while i<n1 and j<n2:
        if nums1[i]>nums2[j]:
            count+=1
            previous_el=nums2[j]
            j+=1
        else:
            count+=1
            previous_el=nums1[i]
            i+=1
        if count==k:
            return previous_el
    while i<n1:
        count+=1
        previous_el=nums1[i]
        i+=1
        if count==k:
            return previous_el
        
    while j<n2:
        count+=1
        previous_el=nums2[j]
        j+=1
        if count==k:
            return previous_el
        
    return -1

nums1=[2,3,6,7,9]
nums2=[1,4,8,10]
k=4
a=[2,3,6,7,9], 
b = [1, 4, 8, 10], 
k = 5  
# print(Kth_Element_(nums1,nums2,k))


''' Optimal Approach '''


def Kth_Element_opt(nums1,nums2,k):
    n1=len(nums1)
    n2=len(nums2)
    if n2<n1:
        Kth_Element_opt(nums2,nums1,k)

    low=max(0,k-n2)
    high=min(k,n1)    ## These Ranges are imp without these it will not give you the right Answer


    while low<=high:
        mid1=(low+high+1)//2
        mid2=k-mid1

        l1=float('-inf')
        l2=float('-inf')
        r1=float('inf')
        r2=float('inf')

        if mid1-1>=0: l1=nums1[mid1-1]
        if mid2-1>=0: l2=nums2[mid2-1]
        if mid1<n1: r1=nums1[mid1]
        if mid2<n2: r2=nums2[mid2]

        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        else:
            if l1>r2:
                high=mid1-1
            elif l2>r1:
                low=mid1+1
    return -1

# nums1=[1,4,8,10]
# nums2=[2,3,6,7,9]
# k=4
# nums1=[2,3,6,7,9]
# nums2=[1,4,8,10]
# k=5
k=4
nums1=[4, 4 ,7 ,8 ,8 ,9 ,9 ,10, 11, 11, 12, 13, 13]
nums1=[4, 5 ,10 ,10 ,10, 12]
print(Kth_Element_opt(nums1,nums2,k))
