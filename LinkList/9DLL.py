class DDLNode: 
    def __init__(self,val): 
        self.val =val 
        self.next = None 
        self.prev =None 

class DoublyLinkedList: 
    def __init__(self):
        self.head = None 
    
    def insert_to_head(self,val) : 
        new_node = DDLNode(val) 
        if self.head is None : 
            self.head = new_node 
        else :  
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 

    def append(self,val) : 
        new_node = DDLNode(val) 
        if self.head is None :
            self.head = new_node 
        else : 
            curr = self.head 
            while curr.next is not None: 
                curr = curr.next 
            curr.next = new_node 
            new_node.prev = curr 
    def insert_at(self,val, pos): 
        new_node = DDLNode(val)   
        if pos == 0 : 
            self.insert_to_head(val)  
        else : 
            curr = self.head 
            count = 0 
            while curr is not None and count < pos -1:  
                if curr is None: 
                    print("Postion is out of bound") 
                    break 
                new_node.next = curr.next 
                new_node.prev = curr 
                if curr.next : 
                    curr.next.prev = new_node 
                curr.next = new_node  





node1 =DDLNode(10) 
node2 = DDLNode(20) 
node3 = DDLNode(30) 
node3.prev = node2.next 
node2.prev = node1.next 

        