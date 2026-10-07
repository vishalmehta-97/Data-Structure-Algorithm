class StockSpanner:
    def __init__(self):
        self.prices=[]

    def next(self, price: int) -> int:
        self.prices.append(price)

        span=1

        for i in range(len(self.prices)-2,-1,-1):
            if self.prices[i]<=price:
                span+=1
            else:
                break
        return span

    
        
# obj = StockSpanner()

# print(obj.next(100))  
# print(obj.next(80))  
# print(obj.next(60))  
# print(obj.next(70))
# print(obj.next(60)) 
# print(obj.next(75))  
# print(obj.next(85)) 


''' Optimal Approach '''

class StockSpanner:
    def __init__(self):
        self.stack=[]
        self.index=0

    def next(self, price: int) -> int:
        span=1

        while self.stack and self.stack[-1][0]<=price:
            span+=self.stack[-1][1]
            self.stack.pop()

        self.stack.append([price,span])
        self.index+=1

        return span

obj = StockSpanner()
print(obj.next(100))  
print(obj.next(80))  
print(obj.next(60))  
print(obj.next(70))
print(obj.next(60)) 
print(obj.next(75))  
print(obj.next(85)) 