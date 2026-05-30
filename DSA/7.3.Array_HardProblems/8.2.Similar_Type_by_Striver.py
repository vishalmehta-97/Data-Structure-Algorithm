'''Brute Approach'''

def sortedArray(nums1,nums2):
    n=len(nums1)
    m=len(nums2)
    i=j=0
    array=[]

    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            array.append(nums1[i])
            i+=1
        else:
            array.append(nums2[j])
            j+=1

    while i<n:
        array.append(nums1[i])
        i+=1

    while j<m:
        array.append(nums2[j])
        j+=1
    
    for i in range(len(array)):

        if i<n:
            nums1[i]=array[i]
        else:
            nums2[i-n]=array[i]
    
    return nums1,nums2

nums1=[1,3,5,7]
nums2=[0,2,6,8,9]
# print(sortedArray(nums1,nums2))


'''Optimal Approach 1 '''

def sortedArray_optimal_1(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    i=n-1
    j=0

    while i>=0 and j<m:
        if nums1[i]>nums2[j]:
            nums1[i],nums2[j]=nums2[j],nums1[i]
            i-=1
            j+=1
        else:
            break

    nums1.sort()
    nums2.sort()

    return nums1,nums2


nums1=[1,3,5,7]
nums2=[0,2,6,8,9]
# print(sortedArray_optimal_1(nums1,nums2))


'''Optimal Approach 2'''

def sortedArray_optimal_2(nums1,nums2):
    n=len(nums1)
    m=len(nums2)

    length=n+m
    gap=(length//2)+(length%2)
    while gap>0:
        i=0
        j=gap+i

        while j<length:
            if i<n and j>=n:
                if nums1[i]>nums2[j-n]:
                    nums1[i],nums2[j-n]=nums2[j-n],nums1[i]

            elif i>=n:
                if nums2[i-n]>nums2[j-n]:
                    nums2[i-n],nums2[j-n]=nums2[j-n],nums2[i-n]
            
            else:
                if nums1[i]>nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]
        
            i+=1
            j+=1

        if gap==1:
            break
        else:
            gap=(gap//2)+(gap%2)

    return nums1,nums2
            

nums1=[1,3,5,7]
nums2=[0,2,6,8,9]
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
print(sortedArray_optimal_2(nums1,nums2))
