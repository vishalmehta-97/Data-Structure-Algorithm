class Solution:

    '''Approach-I'''
    # def generate(self,subset,answer,s,i):
    #     if i>=len(s):
    #         answer.append(subset)
    #         return 
        
    #     self.generate(subset,answer,s,i+1)
    #     self.generate(subset+s[i],answer,s,i+1)
    #     return

    # def powerSet(self,s):
    #     answer=[]
    #     subset_str=""
    #     self.generate(subset_str,answer,s,0)
    #     answer.sort()
    #     return answer
    
    '''Approach-II  Using Bit Maniplation'''

    def powerSet(self,s):
        n=len(s)
        array=[]
        for num in range(0,2**n):
            subset=""
            for i in range(0,n):
                if (num & (1<<i)):
                    subset+=s[i]
            array.append(subset)
        # array.sort()
        return array
        

s=Solution()
string="abc"
print(s.powerSet(string))


        