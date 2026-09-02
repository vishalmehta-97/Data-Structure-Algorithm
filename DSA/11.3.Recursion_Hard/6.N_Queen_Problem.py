class Solution:
    def possible(self,color,edges,colorNo,node):   # We can make this function More optimal by using graph concept
        for i in range(len(color)):
            if color[i]==colorNo:
                if [i,node] in edges or [node,i] in edges:
                    return False
        return True
    
    def colorGraph(self,v,edges,m,color,node):
        if node==v:
            return True
    
        for i in range(1,m+1):
            if self.possible(color,edges,i,node):
                color[node]=i
                if self.colorGraph(v,edges,m,color,node+1):
                    return True
                color[node]=0
        return False
            
    def graphColoring(self, v, edges, m):
        color=[0]*v
        return self.colorGraph(v,edges,m,color,0)
        

s=Solution()
v=4
edges=[[0,1],
       [1,3],
       [2,3],
       [3,0],
       [0,2]]
m=3
print(s.graphColoring(v,edges,m))