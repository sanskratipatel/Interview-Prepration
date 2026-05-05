class Node :
    def __init__(self , val): 
        self.val = val 
        self.prev= None
        self.next =None 

class DLL :
    def __init__(self):
        self.head = None 
    
    def insert_at_head(self,val) : 
        new_node = Node(val)
        if not self.head : 
            self.head = new_node
        else: 
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
    def append(self,val): 
        new_node = Node(val) 
        if new_node is not :
             pass