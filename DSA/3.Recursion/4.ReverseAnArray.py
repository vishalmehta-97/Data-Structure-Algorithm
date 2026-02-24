
'''THIS IS USING TWO PARAMETER  (Two Pointer)'''
def reverseArray(l,r):
    if l>=r :
        return
    array[l],array[r] = array[r], array[l]
    reverseArray(l+1,r-1)


array=[1,4,3,6,2,33,21,3,5,1]
reverseArray(0,len(array)-1)
print(array)



'''THIS IS USING ONLY ONE PARAMETER  (One Pointer)'''

def reverse(i):
    n=len(array)
    if i>=n//2:
        return
    array[i],array[n-i-1] = array[n-i-1], array[i]
    reverse(i+1)

array = []
n = int(input("Length: "))

for _ in range(n):
    val = int(input())
    array.append(val)

print("Old Array",array)
reverse(0)
print("Reversed Array",array)
