def mergeSorted(nums1,nums2,n,m):
    # length=len(nums1)
    i=m+n-1
    j=m-1
    k=n-1
    while j>=0 and k>=0:
        if nums2[k]>nums1[j]:
            nums1[i]=nums2[k]
            i-=1
            k-=1
        else:
            nums1[i]=nums1[j]
            i-=1
            j-=1
    while j>=0:
        nums1[i]=nums1[j]
        i-=1
        j-=1

    while k>=0:
        nums1[i]=nums2[k]
        i-=1
        k-=1

    return nums1


nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

# nums1=[1]
# m=1
# nums2=[]
# n=0


# nums1=[0]
# m=0
# nums2=[1]
# n=1
print(mergeSorted(nums1,nums2,n,m))


