nums=[13,46,24,52,20,9]
n=len(nums)
def recursive_bubble(nums,n):
    if n==1:
        print(nums)
        return
    for i in range(n-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    recursive_bubble(nums,n-1)
    
recursive_bubble(nums,n)