''' Brute Force Approach '''

def check_diff(s):
    hash={}
    for chr in s:
        hash[chr]=hash.get(chr,0)+1
    max_count=-1
    min_count=hash.get(s[0])
    
    for i in hash:
        max_count=max(max_count,hash.get(i))
        min_count=min(min_count,hash.get(i))
        
    return max_count-min_count
    
def beautySum(s):
    sum=0
    
    for i in range(len(s)):
        for j in range(i+2,len(s)):  ## because length of 1 and 2 will always give difference as 0
            sum+=check_diff(s[i:j+1])
    return sum
        
s="aabcbaa"
s="aabcb"
# print(beautySum(s))

''' Better Approach '''
        
def beautySum(s):
    sum=0
    for i in range(len(s)):
        # hash={}
        hash=[0]*26
        for j in range(i,len(s)):
            # hash[s[j]]=hash.get(s[j],0)+1
            hash[ord(s[j])-ord('a')]+=1
            # max_=max(hash)
            # min_=max(hash)
            max_=-1
            min_=float('inf')
            for freq in hash:
                if freq != 0:
                    max_ = max(max_, freq)
                    min_ = min(min_, freq)
            # for _ in range(len(hash)):
            #     if hash[_]!=0:
            #         if hash[_]<min_:
            #             min_=hash[_]
            sum+=(max_-min_)
    return sum

    


s="aabcbaa"
s="aabcb"
print(beautySum(s))
