'''Not Optimal (2 loops)'''

def stock_Profit(arr):
    n=len(arr)
    max_profit=0
    profit=0

    for i in range(n):
        for j in range(i,n):
            profit=arr[j]-arr[i]
            if profit>max_profit:
                max_profit=profit
    return max_profit

arr=[7,1,5,3,6,4]
# print(stock_Profit(arr))

'''Brute Force (Still Not Optimal)'''

def stock_profit_brute(arr):
    max_profit=0
    n=len(arr)
    min=arr[0]
    for i in range(1,n):
        for j in range(i):
            if arr[j]<min:
                min=arr[j]
            print("min",min)
            print(arr[i])
            profit=arr[i]-min
            if profit>max_profit:
                max_profit=profit
    return max_profit
        
arr=[7,1,5,3,6,4]
# print(stock_profit_brute(arr))


def stock_optimal_profit(arr):
    max_profit=0
    n=len(arr)
    mini=arr[0]
    for i in range(1,n):
        profit=arr[i]-mini
        if profit>max_profit:
            max_profit=profit
        mini=min(mini,arr[i])
    return max_profit
        
arr=[7,1,5,3,6,4]
print(stock_optimal_profit(arr))