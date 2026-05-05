class Node: 
    def __init__(self , item):  
        self.item = item 
        self.next = None

class SLL: 
    def __init__(self):
        self.head = None

    def append(self,val) :  
        new_node = Node(val) 

        if self.head == None : 
            self.head = new_node 
        else : 
            temp = self.head 
            while temp.next is not None :
                temp = temp.next 
            temp.next = new_node
           
    
    def traversal(self) : 
        if self.head == None:
            return "LL is None"
        else :
            temp = self.head 
            while temp is not None :
                print(temp.val)
                temp = temp.next 
    
    def insert(self, pos , val) :  
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head 
            self.head = new_node 
        else : 
            curr = self.head 
            prev_node = curr 
            count = 0 
            while(curr is not None and count <pos):
                prev_node =curr 
                curr = curr.next 
                count = count +1 
            prev_node.next = new_node 
            new_node.next = curr 

    def delete(self, val) :  
        temp = self.head 
        if temp.val == val : 
            self.head = temp.next 
            return 
        else : 
            found = False 
            prev = None
            while temp is not None : 
                if temp.val == val :  
                    found =True 
                    break 
                prev = temp 
                temp = temp.next 
            
            if found ==True :
                prev.next =temp.next 
                return 
            else :
                prev("Node Not found")
  