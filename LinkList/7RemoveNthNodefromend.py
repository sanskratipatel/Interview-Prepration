class LLL:
    def RemoveNhNode(self, n): 
        length = 0 
        temp = self.head 
        while temp is not None:
            temp = temp.next 
            length = length+1 
        if length == n :  
            new_jead = self.head.next  
            del self.head 
            print(new_jead) 
        
        pos = length=n 
        count = 1 
        temp = self.head
        while (count < pos) : 
            temp = temp.next 
            count =count+1 
        temp.next = temp.next.next 
        del temp 
    
    def optimal_solution(self,n) : 
        temp = self.head 
        next_po = self.head 
        n =2 
        for i in range(0 , n) : 
            next_po = next_po.next 
        if next_po is None: 
            new_node = self.head.next
            del head 
            return new_node 
        while next_po.next is not None : 
            temp = temp.next 
            next_po = next_po.next 
        temp.next = temp.next.next  
        return temp.next 
    

