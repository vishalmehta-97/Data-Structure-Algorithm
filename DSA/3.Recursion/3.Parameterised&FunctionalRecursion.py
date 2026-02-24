## Problem Sumitiom of N Numbers

'''Parameterised Recursion'''

def printSum(i,sum):
    if i<1:
        print(sum)
        return
    printSum(i-1,sum+i)   ## Parameterised Recursion
    

n=int(input("enter the no : "))
printSum(n,0)



'''Functional Recusion'''

def PrintNsum(n):
    if n==0:
        return 0
    return n+PrintNsum(n-1)

n=int(input("Enter the No: "))
print(PrintNsum(n))




''' Factorial Question'''


def factorial(n):
    if n==0 or n==1:
        return 1
    
    return n* factorial(n-1)


n=int(input("Enter the No: "))
print(factorial(n))