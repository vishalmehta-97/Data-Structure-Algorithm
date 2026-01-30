def reverse(n):
    sign=-1 if n<0 else 1
    n=abs(n)

    reverseNo=0
    while(n>0):
        last_digit=n%10
        reverseNo=(reverseNo*10)+last_digit
        n=n//10
        
    reverseNo*=sign

    if reverseNo<(-21**31) or reverseNo>(2**31-1):
        return 0
    
    return reverseNo



n=int(input("Enter a no: "))
print(reverse(n))