class LRUCache:
    def __init__(self, capacity: int):
        self.hash={}
        self.max_capacity=capacity

        self.head=[0,0,None,None]
        self.tail=[0,0,None,None]

        self.head[3]=self.tail
        self.tail[2]=self.head

    def deleteNode(self,node):
        node_prev=node[2]
        node_next=node[3]

        node_prev[3]=node_next
        node_next[2]=node_prev

    def insert_after_head(self,node):
        heads_next_node=self.head[3]
        heads_next_node[2]=node
        self.head[3]=node
        node[2]=self.head
        node[3]=heads_next_node


    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        node=self.hash.get(key)  ## This will give you the value of the node
        value=node[1]

        ## 2 important Function

        self.deleteNode(node)
        self.insert_after_head(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node=self.hash.get(key)
            node[1]=value
            self.deleteNode(node)
            self.insert_after_head(node)
        else:
            if len(self.hash)==capacity:
                node_to_remove=self.tail[2]
                key_to_remove=node_to_remove[0]
                self.hash.pop(key_to_remove,None)
                self.deleteNode(node_to_remove)

            # new_node=[key,value,self.head,self.head[3]]
            # heads_next_node=self.head[3]
            # heads_next_node[2]=new_node
            # self.head[3]=new_node
            new_node=[key,value,None,None]
            hash[key]=value
            self.insert_after_head(new_node)
                    

capacity=2
obj=LRUCache(capacity)
param_1=obj.get([2])
obj.put(1,1)
