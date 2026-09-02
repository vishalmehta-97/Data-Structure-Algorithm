''' This Approach was also good but not able to pass all the test case because of some extra conditions '''

# class Solution:
#     def generate(self,num,target,ansArray,index,s,oppArray):
#         if index>=len(num):
#             s=s[:len(s)-1]
#             if eval(s)==target:
#                 ansArray.append(s)
#                 return ansArray
#             return
               
#         s+=num[index]        
#         for operator in oppArray:  
#             self.generate(num,target,ansArray,index+1,s+operator,oppArray)

#     def addOperators(self,num,target):
#         ansArray=[]
#         s=""
#         index=0
#         oppArray=["+","-","*"]

#         self.generate(num,target,ansArray,index,s,oppArray)
#         return list(set(ansArray))

# s=Solution()
# num="105"
# print(s.addOperators(num,target=5))


''' Optimal Approach '''

class Solution:
    def generate(self, num, target, ansArray, index, s, evaluated, residual):
        # Base case
        if index == len(num):
            if evaluated == target:
                ansArray.append(s)
            return

        # Backtracking loop
        for i in range(index, len(num)):
            # Handle leading zero
            if i > index and num[index] == "0":
                return

            # Get the current number
            currStrNumber= num[index : i + 1]
            current_num_val = int(currStrNumber)

            if index == 0:
                self.generate(num,target,ansArray,i + 1,s + currStrNumber,current_num_val,current_num_val,
                )
            else:
            
                self.generate(num,target,ansArray,i + 1,s + "+" + currStrNumber,evaluated + current_num_val,current_num_val,)
                self.generate(num,target,ansArray,i + 1,s + "-" + currStrNumber,evaluated - current_num_val,-current_num_val,)
                self.generate(num,target,ansArray,i + 1,s + "*" + currStrNumber,evaluated - residual + (residual * current_num_val),residual * current_num_val,)

    def addOperators(self, num: str, target: int):
        ansArray = []
        s = ""
        index = 0
        self.generate(num, target, ansArray, index, s, evaluated=0, residual=0)
        return ansArray


s = Solution()
num = "105"
print(s.addOperators(num, target=5))