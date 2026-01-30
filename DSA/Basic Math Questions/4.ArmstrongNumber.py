def armstrongNumber (self, n):
    addition=0
    lst = list(map(int, str(n)))
    length=len(lst)
    orignalNo=n
    while n>0:
        
        last_digit=n%10
        addition=addition+last_digit**length
        n=n//10
        
    if orignalNo==addition:
        return True
    else:
        return False
        
            