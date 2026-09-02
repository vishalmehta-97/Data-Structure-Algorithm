class Solution:
    def generate(self,s,wordDict,index):
        if index>=len(s):
            return True
        
        if s in wordDict:
            return True
             
        for i in range(index+1,len(s)+1):
            if s[index:i] in wordDict :    ## insead of checking everytime in the array we can also use unordered Set so that lookup can be done in 0(1)
                if self.generate(s,wordDict,i):
                    return True
        return False
    
    def wordBreak(self,s,wordDict):
        index=0
        return self.generate(s,wordDict,index)

ss=Solution()
s="leetcode"
wordDict=["leet","code"]
s="applepenapple"
wordDict=["pen","apple"]
s="catsandog"
wordDict=["cats","dog","sand","and","cat"]
s="goalspecial"
wordDict=["go","goal","goals","special"]
print(ss.wordBreak(s,wordDict))
        
