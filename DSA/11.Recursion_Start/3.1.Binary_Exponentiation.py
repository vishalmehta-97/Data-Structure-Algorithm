''' This is an efficiany way to Calculate large Powers '''

def pow_BinaryExponentiation(x,n):
    if n==0:
        return 1

    half=pow_BinaryExponentiation(x,n//2)
    result=half*half
    if n%2==1:
        result*=x
    return result

x=2
n=1234567890
print(pow_BinaryExponentiation(x,n))
