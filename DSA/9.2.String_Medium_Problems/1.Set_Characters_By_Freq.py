''' Brute Force Approach '''

def frequencySort(s):
    freq =[[chr(i), 0] for i in range(123)]
    for char in s:
        freq[ord(char)][1]+=1
    freq.sort(key=lambda x:x[1],reverse=True)

    ans=''
    for ch,f in freq:
        if f!=0:
            # while f>0:
            #     ans+=ch
            #     f-=1
            ans+=ch*f
    return ans


s="tree"
# s="cccaaa"
# s="Aabb"
# print(frequencySort(s))


''' Better Approach '''

import heapq

def frequencySort_(s):
    ascii=[0]*123
    
    for char in s:
        ascii[ord(char)]+=1

    heap=[]
    for i in range(len(ascii)):
        if ascii[i]!=0:
            heapq.heappush(heap,(-ascii[i],chr(i)))
    
    ans=''
    for i in range(len(heap)):
        freq,ch=heapq.heappop(heap)
        freq=-freq
        while freq>0:
            ans+=ch
            freq-=1
    return ans

s="tree"
s="cccaaa"
s="Aabb"
# print(frequencySort_(s))


'''Optimal Approach (Bucket Sorting)'''

def frequencySort_opt(s):
    hash={}
    for chr in s:
        hash[chr]=hash.get(chr,0)+1

    bucket=[[] for _ in range(len(s)+1)]

    for key,value in hash.items():
        bucket[value].append(key)
    print(bucket)
    ans=''
    for i in range(len(bucket)-1,-1,-1):
        if len(bucket[i])!=0:
            for j in range(len(bucket[i])):
                ans+=bucket[i][j]*i    
    return ans

s="tree"
s="cccaaa"
s="Aabb"
print(frequencySort_opt(s))






