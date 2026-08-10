'''This is without consecutive 1's'''
class Solution:
    def helper(self,n,s,array):
        if len(s)==n:
            array.append(s)
            return
        
        self.helper(n,s+'0',array)
        if not s or s[-1]!='1':
            self.helper(n,s+'1',array)
    
    def generateBinaryStrings(self,n):    
        array=[]
        self.helper(n,"",array)
        return array
        

s=Solution()
n=3
print(s.generateBinaryStrings(n))

'''This is for without Consecutive 0's'''
class Solution:
    def helper(self,n,s,array):
        if len(s)==n:
            array.append(s)
            return
        
        self.helper(n,s+'1',array)
        if not s or s[-1]!='0':
            self.helper(n,s+'0',array)
    
    def generateBinaryStrings(self,n):    
        array=[]
        self.helper(n,"",array)
        return array
        

s=Solution()
n=3
print(s.generateBinaryStrings(n))
