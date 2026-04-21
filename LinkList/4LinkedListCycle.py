class LLS : 
    def cycleLinkedList(self) :
        slow = self.head 
        fast = self.head 

        while(fast is not None and fast.next is not None ):  
            slow = slow.next  
            fast = fast.next.next 
            if slow == fast :
                print("Yess") 
                break

    def cycleLinkedList1(self) :
        my_set = set()
        temp = self.head
        while(temp is not None ): 
            if temp in my_set : 
                print("Cycle ") 
            my_set.add(temp) 
            temp = temp.next