'''Fiboncis Series with a simple loop'''
# f=[0,1]

# n=int(input(":"))
# for i in range(2,n):
#     f.append(f[i-1]+f[i-2])

# print(f)
# print(f[n-1])



''' Multiple Recursion '''

def fibonaci(n):
    if n<=1:
        return n

    return fibonaci(n-1)+fibonaci(n-2)

    
n=int(input("Enter the Number:"))
print(fibonaci(n))