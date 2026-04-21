class LinkedList:
    def StartingPointLinkedlistCycle(self) : 
        def bruteforce (self) :
            temp = self.head 
            my_set = set() 
            while(temp is not None) :
                if temp in my_set :
                    print(temp ,"Startting point") 
                    break
                my_set.add(temp) 
                temp = temp.next 
            
        def optimizeAnswer(self) : 
            slow = self.head 
            fast = self.head 
            while(fast is not None and fast.next is not None) : 
                slow = slow.next 
                fast = fast.next.next 

                if slow == fast :
                    slow =self.head 
                    while(slow != fast) : 
                        slow = slow.next 
                        fast = fast.next 
                    print(slow , " " ,fast ) 
                    break 
                