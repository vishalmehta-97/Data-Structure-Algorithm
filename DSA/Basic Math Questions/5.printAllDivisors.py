# def PrintAllDivisor(n):
#     list=[]
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             list.append(i)
#             count+=1
#     print(count)
#     return list

# print(PrintAllDivisor(17596824))
    
# def PrintAllDivisor(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=",")
#             count+=1
#     print()
#     print("Total No of factors/Divisors : ",count)

# PrintAllDivisor(17596824)

def PrintAllDivisor(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=",")
            count+=1
    print()
    print("Total No of factors/Divisors : ",count)

PrintAllDivisor(17596824)
