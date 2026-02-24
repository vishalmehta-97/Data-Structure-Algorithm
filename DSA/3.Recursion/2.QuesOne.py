'''Problem 1= Print name n times'''
def printName(i,n):
    if i>n:
        return
    print("Vishal",end=" ")
    printName(i+1,n)

n=int(input("Enter the No:"))
printName(1,n)

print()
print()

'''Problem 2= Print Linearly 1 To n '''

def printLinear(i,n):
    if i>n:
        return
    print(i,end=" ")
    printLinear(i+1,n)
n=int(input("Enter the Number: "))
printLinear(1,n)

print()
print()

'''Problem 3= Print Linearly 1 To n but in opposite fashion '''
# 1st way to do this     # backtracking
def printLinear(i,n):
    if i>n:
        return
    printLinear(i+1,n)
    print(i,end=" ")

n=int(input("Enter the Number: "))
printLinear(1,n)

print()
print()

## 2nd way to do this
def printLinear(i,n):
    if i<1:
        return
    print(i,end=" ")
    printLinear(i-1,n)

n=int(input("Enter the Number: "))
printLinear(n,n)

print()
print()


### Backtracking

''' Problem 4 :Print 1 to N with backtracking'''

def print1toN(i,n):
    if i<1:
        return
    print1toN(i-1,n)
    print(i,end=" ")
n=int(input("Enter the no:"))
print1toN(n,n)

print()
print()


''' Problem 5 :Print N to 1 with backtracking'''

def printLinear(i,n):
    if i>n:
        return
    printLinear(i+1,n)
    print(i,end=" ")

n=int(input("Enter the Number: "))
printLinear(1,n)

print()
print()
