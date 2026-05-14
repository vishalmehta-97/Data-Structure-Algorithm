'''Brute Force'''
def majorityElementt(nums):
    n=len(nums)
    output=[]
    for i in range(n):
        # if nums[i] in output:
        #     continue
        # elif len(output)==2:
        #     break
        count=0
        if len(output)==0 or output[0]!=nums[i]:
            for j in range(n):
                if nums[i]==nums[j]:
                    count+=1
            if count>n//3:
                output.append(nums[i])
        if len(output)==2:
            break
    return output
        
nums=[3,2,3]
nums=[1,2]
nums=[2,2,2,3,3,4,4,4]
# print(majorityElementt(nums))

'''Better approach'''
def majorityElement(nums):
    n=len(nums)
    freq={}
    output=[]
    for i in nums:
        freq[i]=freq.get(i,0)+1
    # for i in freq:
        if freq.get(i)==((n//3)+1):
            output.append(i)
        if len(output)==2:
            break

    return output

nums=[3,2,3]
nums=[1,2]
nums=[2,2]
nums=[1,1,1,1,2,3,3,3]
# print(majorityElement(nums))


def majorityElement_opt(nums):
    n=len(nums)
    ele1=nums[0]
    ele2=nums[0]
    count1=0
    count2=0

    for i in range(n):
        if count1==0 and nums[i]!=ele2:
            count1=1
            ele1=nums[i]
        elif count2==0 and nums[i]!=ele1:
            count2=1
            ele2=nums[i]
        
        elif nums[i]==ele1:
            count1+=1
        elif nums[i]==ele2:
            count2+=1
        # elif nums[i]!=ele1: 
        #     count1-=1
        # elif nums[i]==ele2:
        #     count2-=
        else:
            count1-=1
            count2-=1
    output=[]
    cnt1=0
    cnt2=0
    for i in range(n):
        if nums[i]==ele1:
            cnt1+=1
        elif nums[i]==ele2:
            cnt2+=1

    if cnt1>n//3:
        output.append(ele1)
    if cnt2>n//3:
        output.append(ele2)
    return output
    
# nums=[1,1,1,1,2,3,3,3]
nums=[2,1,1,3,1,4,5,6]
nums=[3,3,1,1,1,2,2,2]
print(majorityElement_opt(nums))


