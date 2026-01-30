import math
n=int(input("Enter a no: "))
count=0
while (n>0):
    last_digit=n%10
    count+=1
    n=n//10
print()
print("Total no.of digits of the number :",count)


""" Or we can do is we can use Log for this """

def digit_Concept(x):
    count=math.log10(x)+1
    print(int("Total No of Digits in the no",count))
    
# digit_Concept(43243423423)

