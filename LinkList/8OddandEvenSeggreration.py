class OddandEvenSeggregate :  
    def seggoddandeven(self) : 
        if self.head is None or self.head.next is None : 
            return 
        values = [] 
        temp = self.head 

        while temp is not None and temp.next is not None: 
            values.append(temp.val) 
            temp = temp.next.next 

        temp = self.head.next  
        while temp and temp.next :
            values.append(temp.val) 
            temp = temp.next.next 
        
        temp = self.head 
        index = 0
        while temp is not None : 
            temp.val =values[index] 
            index = index +1 
            temp =temp.next 
        return self.head
 
    def optimal_space(self) : 
        odd = self.head
        even = self.head.next  
        even_head = even
        while even is not None and even.next is not None :  
            odd.next = odd.next.next  
            odd = odd.next 
            even.next = even.next.next  
            even = even.next 

        odd.next = even_head 
        return self.head


